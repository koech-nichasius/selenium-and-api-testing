FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    cargo \
    wget \
    gnupg \
    unzip \
  libnss3 \
  libasound2 \
  libatk1.0-0 \
  libcups2 \
  libxss1 \
  libappindicator3-1 \
  libatk-bridge2.0-0 \
  libgtk-3-0 \
  libgbm1\
&& rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /Selenium

COPY . /Selenium


CMD ["pytest","tests"]