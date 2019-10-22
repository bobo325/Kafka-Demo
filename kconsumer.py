from kafka import KafkaConsumer
consumer = KafkaConsumer("bobo", group_id="bobo",
                         bootstrap_servers=["10.43.142.197:9092"])
while True:
    for msg in consumer:
        print(str(msg))
