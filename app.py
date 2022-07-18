from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        raise HousingException(e, sys) from e
        logging.info(housing.error_message)
        logging.error("Exception : we are testing custom exception")
    logging.info("Inside the index service")
    return "This is my Test Service"

if __name__ == "__main__":
    logging.info("Starting the service")
    app.run(debug=True)
