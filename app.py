from flask import Flask, render_template, jsonify
import sqlite3
from config import *
import queries

app = Flask(__name__)


def serialize_row(row: sqlite3.Row):
    return {key: row[key] for key in row.keys()}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<animal_id>/')
def get_animal_by_id(animal_id):
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(queries.GET_ANIMAL_BY_ID_QUERY, (animal_id, ))
    row = cursor.fetchone()

    cursor.close()

    return jsonify(serialize_row(row))


@app.route('/<animal_id>/full/')
def get_animal_by_id_full(animal_id):
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(queries.GET_ANIMAL_BY_ID_FULL_QUERY, (animal_id, ))
    row = cursor.fetchone()

    cursor.close()

    return jsonify(serialize_row(row))


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        connection.close()
