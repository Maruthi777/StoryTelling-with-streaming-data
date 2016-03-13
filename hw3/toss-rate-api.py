import flask
from flask import request
import redis
import collections
import json
import numpy as np

app = flask.Flask(__name__) #create app
connect = redis.Redis() #start connection to redis

def buildHistogram():
    keys = connect.keys() #function for building histogram
    values = connect.mget(keys) #get keys from redis
    differ = collections.Counter(values)  #get data corresponding to keys in redis
    n = sum(differ.values())
    i=0
    return {l:m/float(n) for l,m in differ.items()} #get rates for each key value in redis
  
@app.route("/")
def histogram(): #build histogram
    h = buildHistogram()
    return json.dumps(h)

@app.route("/probability-differences")
def probability():
    number = request.args.get('number', '')
    diff = request.args.get('time difference', '')
    # get the distribution for the number
    print number, diff
    d = connect.hgetall(number)
    # get the count for the differrer
    try:
      differ = d[diff]
    except KeyError:
      return json.dumps({
        "number": number, 
        "prob": 0,
        "differrer": diff
      })
    # get the normalising constant
    z = sum([float(v) for v in d.data()])
    return json.dumps({
      "number": number, 
      "prob": float(c)/z,
      "differrer": diff
      })




if __name__ == "__main__":
    app.debug = True
    app.run()
