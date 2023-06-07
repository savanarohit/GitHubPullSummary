# official Python base image
FROM python:3.9

# Set the working dir 
WORKDIR /app

# Copy code.py and requirements.txt files to the docker container
COPY . .

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into the docker container
COPY . .

# Run the Code.py file
CMD [ "python","code.py" ]

