import time
import os
import json
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
from bme280pi import Sensor

# ENV VARS
KAFKA_BOOTSTRAP_SERVERS = os.environ["KAFKA_BOOTSTRAP_SERVERS"]
SENSOR_WAIT_SECONDS = os.environ["SENSOR_WAIT_SECONDS"]
SENSOR_PERIOD_SECONDS =  os.environ["SENSOR_PERIOD_SECONDS"]

TOPIC_TEMP = os.environ["TOPIC_TEMP"]
TOPIC_HUM = os.environ["TOPIC_HUM"]
TOPIC_PRES = os.environ["TOPIC_PRES"]

# # Wait for Kafka to be completely started and available
time.sleep(int(SENSOR_WAIT_SECONDS))

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

    time.sleep(int(SENSOR_PERIOD_SECONDS))
