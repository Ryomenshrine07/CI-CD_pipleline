"""Simple Flask application."""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Return service status."""
    return 'SERVICERUNNING'


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
