## Raspberry Pi - BME280 to Kafka ##

This project reads data from a **BME280 sensor** and sends Temperature, Humidity and Pressure data to a **Kafka** broker. 

Everything runs via **Docker Compose**, including the Kafka broker and the Python producer.

No Zookeeper required. 

Just clone, build and check the kafka topics!

![image](https://github.com/user-attachments/assets/6673e73c-f573-46cb-92ba-cb101d6dbfd6)


## 📦 Topics

Default values. Can be modified in the .env file

- `bme280_temperature`
- `bme280_humidity`
- `bme280_pressure`

## 🚀 Quick Start

1. **Clone the repo**

```bash
git clone https://github.com/aranbarri/bme280-kafka
cd bme280-kafka
```

2. **Connect your BME280 sensor**
   
    Make sure it’s connected to your host (e.g. Raspberry Pi) via I2C.


3. **Run everything**
```bash
docker-compose up --build
```
The Python app will start sending sensor data to Kafka automatically.
You can read from the topics via console-consumer this way:
```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bme280_humidity
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bme280_temperature
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bme280_pressure

````

🛠️ Notes

- Kafka runs in a container on port 9092.
- The app requires access to I2C (/dev/i2c-1); add privileges to the container if needed.
- Python dependencies are in requirements.txt [bme280pi, kafka-python]
- https://pypi.org/project/bme280pi/

-----------------
## Environment Configuration
This project uses environment variables to configure sensor data streaming to Apache Kafka. Below is a description of each variable defined in the .env file:

````.env
Variable	                Description
KAFKA_BOOTSTRAP_SERVERS	      Kafka bootstrap server address.
SENSOR_WAIT_SECONDS	      Wait time until the broker is Up.

TOPIC_TEMP	              Kafka topic name for temperature readings.
TOPIC_HUM	              Kafka topic name for humidity readings.
TOPIC_PRES	              Kafka topic name for pressure readings.
````
Default values:

````
KAFKA_BOOTSTRAP_SERVERS=kafka:9092
SENSOR_WAIT_SECONDS=30
MOCK=FALSE
TOPIC_TEMP=bme280-temperature
TOPIC_HUM=bme280-humidity
TOPIC_PRES=bme280-pressure
````

Make sure Kafka is accessible from the address specified in KAFKA_BOOTSTRAP_SERVERS.

When using MOCK=TRUE, ensure the application supports mock data generation.

-----------------


**Connection Diagram**

   ![image](https://github.com/user-attachments/assets/0e89b781-31d8-451b-9ad4-a3ed38d7075a)

![image](https://github.com/user-attachments/assets/8170dfd1-4143-4864-8c0b-b361f06049c8)

![image](https://github.com/user-attachments/assets/8ebd018b-7754-4dfa-8326-0c8bece102bd)
