# Use an official Node runtime as a parent image
FROM node:24-alpine

# Set the working directory in the container
WORKDIR /app

# Bundle app source including the public and src directories
COPY . /app/

# Install package.json
RUN npm install

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run npm start when the container launches
CMD ["npm", "run", "dev"]