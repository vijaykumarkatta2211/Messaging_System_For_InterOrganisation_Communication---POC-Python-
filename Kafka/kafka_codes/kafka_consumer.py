from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "testtopic",
        bootstrap_servers='127.0.0.1:9092',
        api_version=(0, 11, 5),
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("testtopic = {}".format(json.loads(msg.value)))
