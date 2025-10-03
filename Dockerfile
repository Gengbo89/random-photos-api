FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

# Copy the source code into the container
COPY src ./src

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "src/main.py"]
