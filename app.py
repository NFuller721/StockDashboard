from flask import Flask, redirect, url_for, render_template, request, jsonify
from alpha_vantage.timeseries import TimeSeries
from SP500 import SP500

## Initialize alpha vantage api
ts = TimeSeries(key='73RE9B6EKHVY8OTJ', output_format='pandas')

## Symbols dictionary for symbols page
symbols = {'Symbols': SP500}

## Flask Initialization
App = Flask(__name__)

## Symbols page
@App.route('/Symbols/')
def Symbols():
    return jsonify(symbols['Symbols'])

## Main page
@App.route("/", methods=["POST", "GET"])
def index():
    ## Is there a post request
    if request.method == "POST":

        ## Get symbol
        Symbol = request.form['symbol']

        ## Get stock data
        data, _ = ts.get_intraday(symbol=Symbol, interval='1min', outputsize='full')
        Value = data['4. close'].tolist()[0]

        ## Return endpoint
        return render_template("index.html",Symbol=Symbol, Value=Value)
    else:
        ## Return endpoint
        return render_template("index.html",Symbol=None, Value=None)



## Flask Run
if __name__ == '__main__':
    App.run()
