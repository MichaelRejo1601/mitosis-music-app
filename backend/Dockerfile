# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY ./app /code/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade fastapi yt-dlp spleeter
RUN pip freeze -r > requirements.txt
COPY /code/requirements.txt ./requirements.txt

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
