from flask import Flask
from modules import *

app = Flask(__name__)

# if __name__ == "__main__":
# print("boz")

@app.route("/")
def index():
    return "Boz"