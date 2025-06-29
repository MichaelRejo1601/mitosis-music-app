# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /

# Cacheable copy, so if dependencies dont change, rebuild isnt long
COPY requirements.txt /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the current directory contents into the container
COPY . /

ENV WATCHFILES_FORCE_POLLING=true

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
