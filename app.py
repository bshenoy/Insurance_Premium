from flask import Flask
from insurance.logger import logging
from insurance.exception import InsuranceException
import sys, os

app = Flask(__name__)

try:
    logging.info("yhhhh")
    # raise Exception("we are tseting")
    logging.info("trying")
    
except Exception as e:
    cement = InsuranceException(e, sys)
    logging.info(cement.error_message)


@app.route('/', methods=['POST', 'GET'])
def welcome():
    return "hello"

if __name__=="__main__":
    app.run()

