from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'base page'

@app.route('/take')
def hello():
    return 'data taken'

if __name__ == '__main__':
    app.run()
