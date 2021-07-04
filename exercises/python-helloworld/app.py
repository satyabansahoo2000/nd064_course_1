from flask import Flask
from flask import json
import logging
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    TIMESTAMP = datetime.datetime.now()
    ENDPOINT_NAME = 'main'
    app.logger.info(f'{TIMESTAMP}, {ENDPOINT_NAME} endpoint has reached')
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response = json.dumps({"result":"OK - healthy"}),
        status = 200,
        mimetype = 'application/json'
    )
    TIMESTAMP = datetime.datetime.now()
    ENDPOINT_NAME = 'status'
    app.logger.info(f'{TIMESTAMP}, {ENDPOINT_NAME} endpoint has reached')
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response = json.dumps({"status":"success", "code":0, "data":{"UserCount":140, "UserCountActive":23}}),
        status = 200,
        mimetype = 'application/json'
    )
    TIMESTAMP = datetime.datetime.now()
    ENDPOINT_NAME = 'metrics'
    app.logger.info(f'{TIMESTAMP}, {ENDPOINT_NAME} endpoint has reached')
    return response

if __name__ == "__main__":
    logging.basicConfig(filename = r"E:\nd064_course_1\exercises\python-helloworld\app.log", 
                        level=logging.DEBUG)
    app.run(host='0.0.0.0')
