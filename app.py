from flask import Flask, request
import psycopg2
from server import connection

app = Flask(__name__)

@app.route("/count", methods=['GET'])
def filter():
    sphere = request.args.get('sphere')
    cursor = connection.cursor()

    cursor.execute (
                """SELECT COUNT(company_id) FROM companies
                WHERE sphere = %s""", (sphere,)
            )
    data = cursor.fetchall()
    cursor.close()

    return str(data)

if __name__ == '__main__':
    app.run(debug=True)
