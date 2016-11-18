from flask import Flask

app = Flask(__name__)

# view


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()