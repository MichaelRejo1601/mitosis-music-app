# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /

# Copy the current directory contents into the container at /code
COPY . /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
