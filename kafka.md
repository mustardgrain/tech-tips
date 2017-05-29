## Reset Kafka Streams State

```bash
bin/kafka-streams-application-reset.sh \
  --bootstrap-servers localhost:9092
  --application-id my-application \
  --input-topics foo \
  --intermediate-topics bar \
```

## View Stream Output with non-String Keys/Values

```
bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic foo \
  --from-beginning \
  --property print.key=true \
  --property print.value=true \
  --formatter kafka.tools.DefaultMessageFormatter \
  --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
  --property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer
```

For whatever reason, using `--key-deserializer` and/or `--value-deserializer` options doesn't have the same result.
