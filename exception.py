from flask import Flask
from Delivery.logger import logging
from Delivery.exception import CustomException
import os
import sys

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    try:
        raise Exception("we are testing our Exception file")  # Error
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)

        logging.info("We are testing our logging file")

        return "Welcome to Machine Learning Project"


if __name__ == "__main__":
    app.run(debug=True)  # 5000
