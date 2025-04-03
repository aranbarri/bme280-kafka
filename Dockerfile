FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    i2c-tools \
    libi2c-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

CMD ["python", "-u", "main.py"]
