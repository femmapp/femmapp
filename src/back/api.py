from flask import Flask, request
from ast import literal_eval
from Search import *
from pin_manager import * 

app = Flask(__name__)

@app.route("/search", methods=['GET'])
def search():
    args = request.args
    values = args.to_dict()
    return query(literal_eval(values["query"]),literal_eval(values['categories']),int(values['dist']))
    #http://127.0.0.1:5000/search?query=(41.43050169245379,2.18336528460343)&dist=500&categories={0}

@app.route("/add_pin", methods=['POST'])
def add_pin():
    values = request.json
    print(values)
    create_new_pin(values["name"],values["author"],values["categories"],values["lat"],values["long"],values["description"])
    return "Pin created successfully!"

@app.route("/review_pin", methods=['PUT'])
def review():
    values = request.json
    review_pin(int(values["id"]),values["categories"],values["is_positive"])
    return "Pin updated successfully!"
