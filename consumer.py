from kafka import KafkaConsumer
consumer = KafkaConsumer('rep-topic2', bootstrap_servers='test:9092')
for msg in consumer:
    print("topic =", msg.topic, "  partition = ", msg.partition, "  value=", msg.value)
    #print(msg)
