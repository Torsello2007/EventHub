from flask import Flask, jsonify, request, g
from flask_cors import CORS
from database_wrapper import DatabaseWrapper
from auth import require_auth, require_role
import os

app = Flask(__name__)
CORS(app)
db = DatabaseWrapper()

# --- MIDDLEWARE BAN CHECK ---
# (Opzionale: potresti aggiungere un controllo qui per bloccare utenti bannati)

# --- AREA ADMIN: Gestione Utenti ---
@app.route('/api/admin/utenti', methods=['GET'])
@require_auth
@require_role('admin')
def get_all_utenti():
    # In un caso reale interrogheremmo Keycloak, qui prendiamo chi ha fatto azioni nel sistema
    utenti = db.select("SELECT DISTINCT username_utente as username FROM iscrizioni")
    return jsonify(utenti)

@app.route('/api/admin/utenti/<username>/ban', methods=['POST'])
@require_auth
@require_role('admin')
def ban_utente(username):
    db.execute("INSERT INTO utenti_status (username, bannato) VALUES (%s, 1) ON DUPLICATE KEY UPDATE bannato=1", [username])
    return jsonify({"message": f"Utente {username} bannato"})

# --- AREA ADMIN: Moderazione Recensioni ---
@app.route('/api/admin/recensioni', methods=['GET'])
@require_auth
@require_role('admin')
def get_all_recensioni():
    return jsonify(db.select("SELECT * FROM recensioni ORDER BY data_recensione DESC"))

@app.route('/api/admin/recensioni/<int:id>', methods=['DELETE'])
@require_auth
@require_role('admin')
def delete_recensione(id):
    db.execute("DELETE FROM recensioni WHERE id = %s", [id])
    return jsonify({"message": "Recensione rimossa"})

# (Mantenere qui sotto tutte le altre rotte già create in precedenza...)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
