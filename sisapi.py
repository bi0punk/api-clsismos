
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

app = Flask(__name__)

@app.route("/")
def api():
    
    url = 'http://www.sismologia.cl/ultimos_sismos.html'
    requests.get(url)
    page = requests.get(url)


    sopita = BeautifulSoup(page.text, 'lxml')

    table_data = sopita.find('table')

    """ print(table_data) """

    headers = []
    for i in table_data.find_all('th'):
        title = i.text
        headers.append(title)

    df = pd.DataFrame(columns = headers)

    for j in table_data.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        length = len(df)
        df.loc[length] = row

    df_lista = df.to_numpy().tolist() #lista por filas
    df_lista2 = df.to_numpy().transpose().tolist() #listas por columnas 
    print(df_lista)
    print()


#Convertimos df a formato json para poder operar

    resultdataframe = df.to_json(orient="split")
    pars = json.loads(resultdataframe)
    json.dumps(pars, indent=4)  


    return jsonify (df_lista)
   
if __name__ == '__main__':
    app.run(debug=True)



    #?


    """return jsonify({"gooood" : "nashe"})"""
    """ return jsonify(df) """
    """ return jsonify (resultdataframe) """
    """ print(resultdataframe) """
