from flask import Flask

app = Flask(__name__)

@app.route("/search")
def search_spaces():
    return "<p>Hello, World!</p>"