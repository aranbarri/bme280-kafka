# 📡 BME280 Sensor + InfluxDB + Docker (Adafruit version)

This project reads temperature, humidity, and pressure from a BME280 sensor connected via I2C to a Raspberry Pi and sends the data to an InfluxDB instance. The app runs in a Docker container and uses Adafruit's CircuitPython BME280 driver.

---

##  Requirements

- Raspberry Pi with I2C enabled
- BME280 sensor connected to I2C
- Docker & Docker Compose installed
- Python 3.11 base image

---

## 🚀 Running with `docker compose`

Build the Docker Stack:

```bash
docker compose build -t
