If you've used Kafka, you've likely heard about _partitions_. Kafka allows you to partition the data in a given topic so that the processing work can be divided among multiple nodes. Thus partitioning of the data allows more data to be processed in parallel.

Kafka's default logic will attempt to evenly distribute messages into the topic's partitions. This is achieved with what is essentially a round-robin algorithm, assigning each message to a different partition; the number of partitions is definied at the topic level.

This default distribution works fine for most use cases. However, Kafka supports the ability to provide a custom partitioning algorithm.

One might choose to go the route of using custom partitions if they for instance have certain messages which would take longer to process, thus offloading those messages to specific partitions, or if maybe they are running their cluster in a way that certain nodes have specific services running on them, so that it would be more convenient for certain messages to run on the node that is running the service that will be used in further processing of the message. If you're planning to use custom partitioning this quick guide should help you.

This guide will assume you already have Kafka and zookeeper up and running, for more on that see this guide (https://kafka.apache.org/quickstart). For this guide we'll also be setting up our project using Maven, to start a project with Maven see this guide (https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html).

First off we'll start a topic with a partition from command line.

```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic custom-partitioned-topic
```

Once we have that running we can start coding. 
This is a super simple Kafka Producer that will just send out a message to our topic values 0, 1, and 2.

```
package com.mustardgrain.blog;

import java.util.*;
import org.apache.kafka.clients.producer.*;

public class CustomProducer {

    public static void main(String[] args) throws Exception{

        String topicName = "custom-partitioned-topic";

        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer","org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("partitioner.class", "com.mustardgrain.blog.CustomPartitioner");

        Producer<String, String> producer = new KafkaProducer
                <String, String>(props);

        for(int i = 0; i < 40; i++) {
            int v = i % 3;
            producer.send(new ProducerRecord<String, String>(topicName, String.valueOf(v), String.valueOf(v)));
        }
        System.out.println("Message sent successfully");
        producer.close();
        System.out.println("SimpleProducer Completed.");
    }
}
```

Now we code our partitioner. Our partitioner will take the values that we send from our producer and return the partition that that value would map to.

```
package com.mustardgrain.blog;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.*;

import java.util.List;
import java.util.Map;

public class CustomPartitioner implements Partitioner {

    public void configure(Map<String, ?> configs) {
    }

    public int partition(String topic, Object key, byte[] keyBytes, Object value, byte[] valueBytes, Cluster cluster) {
        List<PartitionInfo> partitions = cluster.partitionsForTopic(topic);
        int numPartitions = partitions.size();
        int partitionValue = Integer.valueOf((String) value);
        if (partitionValue > (numPartitions - 1))
            return numPartitions - 1;
        return partitionValue;
    }
    public void close() {}
}
```

Now running the Producer in the same directory as the Partitioner will run messages alternately through partitions 0 through 2.

The quick and dirty of it is this. If you want to create your own custom partitioner the key parts are this. In the Producer make sure you have this line while setting up your properties.

```
        props.put("partitioner.class", "package.of.the.CustomPartitioner");
```

In your code for your partitioner, make sure the class implements the Partitioner interface from the org.apache.kafka.common project. The partition method is where the magic happens. In the partition method you return the partition ID that you want to push this message to.

You can get info on your partitions in your partitioner using:

```
List<PartitionInfo> partitions = cluster.partitionsForTopic(topic);
```

You can use the information from the PartitionInfo (https://kafka.apache.org/11/javadoc/org/apache/kafka/common/PartitionInfo.html) class in your partitioning, for instance getting the number of partitions.

In order to make sure that the partitioner is working as expected you can run the following from the command line in your kafka bin directory:

```
bin/kafka-run-class.sh kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 --topic custom-partitioned-topic
```

Another thing that you can do in order to check that the message is coming through the correct partition is to use the data in your Kafka consumer. For example:
```
package com.mustardgrain.blog;

import java.util.Arrays;
import java.util.Properties;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;

public class MessageConsumerRunner {

    public static void main( String[] args ) {
        MessageConsumer consumer = new MessageConsumer();
        Thread thread = new Thread(consumer);
        thread.start();
        try {
            Thread.sleep(100000);
        } catch (InterruptedException ie) {}
    }

    private static class MessageConsumer implements Runnable {

        private final KafkaConsumer<String, String> consumer;
        private final String topic;

        public MessageConsumer() {
            Properties prop = createConsumerConfig();
            this.consumer = new KafkaConsumer(prop);
            this.topic = "custom-partitioned-topic";
            this.consumer.subscribe(Arrays.asList(this.topic));
        }

        private Properties createConsumerConfig() {
            Properties props = new Properties();
            props.put("bootstrap.servers", "localhost:9092");
            props.put("group.id", "custom-partitions");
            props.put("enable.auto.commit", "true");
            props.put("auto.commit.interval.ms", "1000");
            props.put("session.timeout.ms", "30000");
            props.put("auto.offset.reset", "earliest");
            props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
            props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
            return props;
        }

        public void run() {
            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(100);
                for (final ConsumerRecord record : records)
                    System.out.println("Message is " + record.value() + ",Printed from Partition: " + record.partition());
            }
        }

    }
}
```
As you can see when you get a record out of Kafka you can get the id of the partition that the message came out of. 
