from flask import Flask, request
import psycopg2
from server import connection

app = Flask(__name__)

@app.route("/", methods=['POST'])
def filter():
    filter = request.form['filter']
    cursor = connection.cursor()

    cursor.execute (
                f"""SELECT COUNT(company_id) FROM сompanies
                WHERE sphere = '{filter}'"""
            )
    data = cursor.fetchall()
    connection.close()

    return str(data)

if __name__ == '__main__':
    app.run(debug=True)