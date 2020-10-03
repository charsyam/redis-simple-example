from time import perf_counter 
from flask import Flask, jsonify
import redis


rconn = redis.StrictRedis("127.0.0.1", 6379)

app = Flask(__name__)


def factorial(value):
    f = 1
    for i in range(2, value+1):
        f = f * i

    return f


def cache_key(value):
    return f'f:{value}'


@app.route('/api/v1/f/<value>')
def f(value):
    key = cache_key(value) 
    time_start = perf_counter()
    cached_value = rconn.get(key)
    if not cached_value:
        value = factorial(int(value))
        rconn.set(key, value)
    else:
        value = int(cached_value.decode("utf-8"))

    time_stop = perf_counter()
    return jsonify({"elasped": time_stop - time_start, "value": value})


if __name__ == '__main__':
    app.run("0.0.0.0")
