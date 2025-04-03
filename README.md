# BME280 to Kafka

This project reads data from a **BME280 sensor** and sends temperature, humidity, and pressure to **three Kafka topics**. Everything runs via **Docker Compose**, including the Kafka broker and the Python producer.

## 📦 Topics

- `bme280_temperature`
- `bme280_humidity`
- `bme280_pressure`

## 🚀 Quick Start

1. **Clone the repo**

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. **Connect your BME280 sensor**
    Make sure it’s connected to your host (e.g. Raspberry Pi) via I2C.

3. **Run everything**
```bash
docker-compose up --build
```
The Python app will start sending sensor data to Kafka automatically.

🛠️ Notes

    Kafka runs in a container on port 9092.

    The app requires access to I2C (/dev/i2c-1); add privileges to the container if needed.

    Python dependencies are in requirements.txt.
