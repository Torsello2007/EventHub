from flask import Flask, jsonify, request, send_from_directory, g
from flask_cors import CORS
from database_wrapper import DatabaseWrapper
from auth import require_auth, require_role
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
db = DatabaseWrapper()
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/api/eventi', methods=['GET'])
def get_eventi():
    return jsonify(db.select("SELECT * FROM eventi ORDER BY data_evento ASC"))

@app.route('/api/eventi/<int:id_evento>/iscriviti', methods=['POST'])
@require_auth
def iscriviti_evento(id_evento):
    username = g.user.get('preferred_username')
    evento = db.select_one("SELECT posti_disponibili FROM eventi WHERE id = %s", [id_evento])
    count = db.select_one("SELECT COUNT(*) as tot FROM iscrizioni WHERE id_evento = %s", [id_evento])
    if count['tot'] >= evento['posti_disponibili']: return jsonify({"error": "Posti esauriti"}), 400
    db.execute("INSERT INTO iscrizioni (id_evento, username_utente) VALUES (%s, %s)", [id_evento, username])
    return jsonify({"message": "Iscritto!"}), 201

# --- NUOVA ROTTA PER MUCA (S2) ---
@app.route('/api/utente/biglietti', methods=['GET'])
@require_auth
def get_biglietti():
    username = g.user.get('preferred_username')
    query = """
        SELECT e.*, i.data_iscrizione 
        FROM eventi e 
        JOIN iscrizioni i ON e.id = i.id_evento 
        WHERE i.username_utente = %s
    """
    biglietti = db.select(query, [username])
    return jsonify(biglietti)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
