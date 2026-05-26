from flask import Flask, jsonify
from flask_cors import CORS
from database_wrapper import DatabaseWrapper

app = Flask(__name__)
CORS(app)

# Inizializziamo il wrapper
db = DatabaseWrapper()

@app.route('/health', methods=['GET'])
def health():
    if db.test_connection():
        return jsonify({"status": "online", "database": "connesso tramite DatabaseWrapper"}), 200
    else:
        return jsonify({"status": "error", "database": "connessione fallita"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
