# Demo of Azure Face API with Python

This is a demo of the Face API using Python. It shows how to do simple face detection and framing.

## Requirements

* Face API key: https://azure.microsoft.com/en-us/services/cognitive-services/face/
* Pillow and Requests libraries for Python

## Running

* Install the dependencies: `pip install -r requirements.txt`
* Create an API key, set it as environment variable FACE_API_KEY
* Run it: `Python demo.py [image url]`. If no image url given, uses example one from https://www.how-old.net/
