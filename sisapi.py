
from flask import Flask, jsonify
import requests
import json
import pandas as pd


app = Flask(__name__)

@app.route("/")
def api():
    
    url = "http://www.sismologia.cl/ultimos_sismos.html"
    data = requests.get(url).text

    print(data)


   
    


    return jsonify({"gooood" : "nashe"})
    """ return jsonify(df) """





if __name__ == '__main__':
    app.run(debug=True, port=4000)