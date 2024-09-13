# Using official Python runtime as a parent image, version 1 of dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
CMD ["python", "chisom.py"]