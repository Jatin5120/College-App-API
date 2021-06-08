from flask import Flask, jsonify
import json

app = Flask(__name__)


def getData(fileName):
    file = open(f"api/{fileName}.json", "r", encoding="utf8")
    jsonContent = file.read()
    return jsonify(json.loads(jsonContent))


@app.route('/')
@app.route('/home')
def home_method():
    return getData('home')


@app.route('/about')
def about_method():
    return getData('about')


@app.route('/achievements')
def achievements_method():
    return getData('achievements')


@app.route('/placements')
def placements_method():
    return getData('placements')


@app.route('/alumni')
def alumni_method():
    return getData('alumni')


@app.route('/help')
def help_method():
    return getData('help')


if __name__ == '__main__':
    app.run()
