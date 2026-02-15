# 1. Use a lightweight Python base image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your requirements file and install dependencies
# (Even if it's just flake8 for now)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your application code
COPY . .

# 5. Set the entrypoint to your script
# This allows the container to act like a command-line tool
RUN flake8 .