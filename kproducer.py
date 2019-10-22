import datetime

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=["10.43.142.197:9092"])
while True:
    for _ in range(20):
        now = str(datetime.datetime.now()).encode("utf-8")
        producer.send("bobo", now)
