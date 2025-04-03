# BME280 to Kafka

This project reads data from a **BME280 sensor** and sends temperature, humidity, and pressure to **three Kafka topics**. Everything runs via **Docker Compose**, including the Kafka broker and the Python producer.

## 📦 Topics

Kafka runs on 9092.

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

   ![image](https://github.com/user-attachments/assets/0e89b781-31d8-451b-9ad4-a3ed38d7075a)

   ![image](https://github.com/user-attachments/assets/2bb77206-13f8-4d04-8909-c2257a2ed93a)


4. **Run everything**
```bash
docker-compose up --build
```
The Python app will start sending sensor data to Kafka automatically.

🛠️ Notes

- Kafka runs in a container on port 9092.
- The app requires access to I2C (/dev/i2c-1); add privileges to the container if needed.
- Python dependencies are in requirements.txt [bme280pi, kafka-python]
