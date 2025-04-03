import time
import os
import json
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
from bme280pi import Sensor

# Load environment variable
KAFKA_BOOTSTRAP_SERVERS = os.environ["KAFKA_BOOTSTRAP_SERVERS"]

# Kafka topics
TOPIC_TEMP = "bme280-temperature"
TOPIC_HUM = "bme280-humidity"
TOPIC_PRES = "bme280-pressure"

# # Function to wait until Kafka is ready
# def wait_for_kafka(bootstrap_servers, timeout=30):
    # start = time.time()
    # while True:
        # try:
            # print(f"⏳ Waiting for Kafka at {bootstrap_servers}...")
            # KafkaProducer(bootstrap_servers=bootstrap_servers)
            # print("✅ Kafka is up!")
            # break
        # except NoBrokersAvailable:
            # if time.time() - start > timeout:
                # print("❌ Timed out waiting for Kafka.")
                # exit(1)
            # time.sleep(2)

# # Wait for Kafka to be available
# wait_for_kafka(KAFKA_BOOTSTRAP_SERVERS)

time.sleep(30)
# Initialize BME280 sensor
sensor = Sensor(address=0x76)

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Main loop: read and send data every second
while True:
    try:
        data = sensor.get_data()
        timestamp = int(time.time())

        producer.send(TOPIC_TEMP, {"value": data["temperature"], "timestamp": timestamp})
        producer.send(TOPIC_HUM, {"value": data["humidity"], "timestamp": timestamp})
        producer.send(TOPIC_PRES, {"value": data["pressure"], "timestamp": timestamp})

        print(f"[OK] Sent → Temp: {data['temperature']:.2f}°C | Hum: {data['humidity']:.2f}% | Pres: {data['pressure']:.2f} hPa")

    except Exception as e:
        print(f"[ERROR] {e}")

    time.sleep(1)
