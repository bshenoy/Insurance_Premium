from flask import Flask
from insurance.logger import logging
from insurance.exception import InsuranceException
import sys, os

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def welcome():
    return "hello"

if __name__=="__main__":
    app.run()

