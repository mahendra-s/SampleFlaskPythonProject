from flask import Flask
from app.module1 import module1


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(module1)
    app.run(debug=True)