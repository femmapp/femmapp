from flask import Flask, request
from ast import literal_eval
from Search import *

app = Flask(__name__)

@app.route("/search", methods=['GET'])
def search():
    args = request.args
    values = args.to_dict()
    return query(literal_eval(values["query"]),literal_eval(values['categories']),int(values['dist']))


#Dues qüestions: Afegim newline al final dels tsv? A Search no caldria un if __name__ == '__main__'?