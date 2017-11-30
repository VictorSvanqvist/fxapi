from flask import Flask

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
    return 'Hello ' + name + '. Now type your age in the adress bar after /' + name + '/'


@app.route('/hello/<name>/<age>')
def hello_age(name, age):
    return 'Hello ' + name + ' i remember when i was ' + age + ' years olds'

if __name__ == '__main__':
    app.run(port= 5005,debug=True)
