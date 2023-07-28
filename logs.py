from flask import Flask
from Delivery.logger import logging

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("We are testing our logging file")

    return "Welcome to Machine Learning Project"


if __name__ == "__main__":
    app.run(debug=True)  # 5000
