# use the official python image
FROM python:3.12-slim

# set the working directory in the container
WORKDIR /app

# copy appliation files to the container
COPY app.py .

# run the application
CMD ["python", "app.py"]
