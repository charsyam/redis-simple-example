from time import perf_counter 
from flask import Flask, jsonify


app = Flask(__name__)


def factorial(value):
    f = 1
    for i in range(2, value+1):
        f = f * i

    return f


@app.route('/api/v1/f/<value>')
def f(value):
    time_start = perf_counter()
    value = factorial(int(value))

    time_stop = perf_counter()
    return jsonify({"elasped": time_stop - time_start, "value": value})


if __name__ == '__main__':
    app.run("0.0.0.0")
