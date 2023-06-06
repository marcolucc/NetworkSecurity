# My Flask App

This is a simple Flask app that pings a given host.

## Installation

1. Clone the repository
2. Install the required packages with `pip install -r requirements.txt`
3. Run the app with `python app.py`

## Usage

1. Open your web browser and go to `http://localhost:5000`
2. Enter the ip and click "Ping"
3. The results will be displayed on the page
4. Your job is to hack into the app and gain access to a shell

## Docker

You can also run this app in a Docker container. To do so, follow these steps:

1. Build the Docker image with `docker build -t my-flask-app .`
2. Run the container with `docker run -p 5000:5000 my-flask-app`
3. Open your web browser and go to `http://localhost:5000`

## Hints

1. Look up the ping command documentation
2. Look up RCE

