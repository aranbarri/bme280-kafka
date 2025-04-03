

# BME280 Kafka Data Pipeline

This project streams environmental data from a **BME280 sensor** (temperature, humidity, pressure) to **three separate Kafka topics**. The system is containerized using **Docker Compose**, which includes both the Kafka broker and the Python producer app.

## 🧩 Features

- Reads data from a BME280 sensor.
- Sends temperature, humidity, and pressure to individual Kafka topics.
- Kafka broker in KRaft mode included via Docker Compose.
- Python app auto-starts with Compose.

## 📦 Kafka Topics

- `bme280_temperature`
- `bme280_humidity`
- `bme280_pressure`

Each topic receives one specific type of data from the BME280 sensor.

## 📁 Project Structure

. ├── docker-compose.yml ├── producer/ │ ├── app.py │ ├── requirements.txt │ └── ... └── README.md


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
2. Connect the BME280 Sensor

Ensure your BME280 sensor is connected to the host machine (e.g., a Raspberry Pi) and accessible via I2C.
3. Update Configuration (if needed)

Edit the app.py or environment variables if your sensor is on a different I2C address or you want to change Kafka topics.
4. Build and Run with Docker Compose

docker-compose up --build

This will:

    Start the Kafka KRaft broker.

    Start the Python producer that continuously reads from the sensor and pushes data to Kafka.

5. Verify the Kafka Topics

You can use Kafka tools (e.g., kafka-console-consumer) or a UI like Kafka UI to inspect topic messages.


🛠️ Dependencies

The Python app uses:

smbus2 for I2C communication
bme280pi
kafka-python

Dependencies are listed in requirements.txt.
📌 Notes

    This setup assumes the sensor is physically accessible to the host running Docker (e.g., /dev/i2c-1).

    Make sure to give the container appropriate permissions or use --privileged if required.

📜 License

MIT License. See LICENSE file for more information.


---
