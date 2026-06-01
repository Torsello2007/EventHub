from flask import Flask, jsonify
from flask_cors import CORS
from database_wrapper import DatabaseWrapper

app = Flask(__name__)
CORS(app)
db = DatabaseWrapper()

@app.route('/eventi', methods=['GET'])
def get_eventi():
    data = db.select("SELECT * FROM eventi ORDER BY data_evento ASC")
    return jsonify(data if data else [])

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
