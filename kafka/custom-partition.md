Kafka supports custom partitions, and if you want/need to use them, this is a quick guide on writing custom partitions for Apache Kafka in Java.

This guide will assume you already have Kafka and zookeeper up and running, for more on that see this guide (https://kafka.apache.org/quickstart). For this guide we'll also be setting up our project using Maven, to start a project with Maven see this guide (https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html).

First off we'll start a topic with a partition from command line.

```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic custom-partitioned-topic
```

Once we have that running we can start coding. 
This is a super simple Kafka Producer that will just send out a message to our topic values 0, 1, and 2.

```
package com.mustardgrain;

import java.util.*;
import org.apache.kafka.clients.producer.*;

public class CustomProducer {

    public static void main(String[] args) throws Exception{

        String topicName = "custom-partitioned-topic";

        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer","org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("partitioner.class", "com.mustardgrain.CustomPartitioner");

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
package com.mustardgrain;

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
