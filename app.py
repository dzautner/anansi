from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


#route that multiplies by 7
@app.route('/multiply/<int:num>')
def multiply(num):
    return str(num*7)


#route that says hello to a name
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"