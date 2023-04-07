# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Clone the yolov5 repository from GitHub
RUN git clone https://github.com/ultralytics/yolov5.git

# Install dependencies
WORKDIR /app/yolov5
RUN pip install -qr requirements.txt

# Copy the detect.py file to the working directory
COPY detect.py .

# Set the command to run the detect.py file with the specified arguments
CMD ["python", "detect.py", "--weights", "bestl.pt", "--source", "./video/result1.mp4"]