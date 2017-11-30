import requests
from flask import Flask, jsonify
from fxlib import fxdata


app = Flask(__name__)


# this is a decorator
@app.route('/')
# this is a function
def hello_world():
    return 'Hello World! type /hello/ in the adress bar'


@app.route('/hello/')
# this is a function
def hello():
    return 'Type your name after the /hello/ to proceed!'



@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello ' + name.title() + '. Now type your age in the adress bar after /' + name + '/'


@app.route('/hello/<name>/<age>')
def hello_age(name, age):
    return 'Hello ' + name.title() + ' i remember when i was ' + age + ' years olds'

@app.route('/bank/<currency>')
def bank_currency(currency):
    return jsonify(fxdata())











if __name__ == '__main__':
    app.run(port= 5005,debug=True)
