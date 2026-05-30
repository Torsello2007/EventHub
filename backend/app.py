from flask import Flask, jsonify, request
from flask_cors import CORS
from database_wrapper import DatabaseWrapper

app = Flask(__name__)
CORS(app)

db = DatabaseWrapper()

# AREA PUBBLICA: Lista eventi (con ricerca e filtri)
@app.route('/api/eventi', methods=['GET'])
def get_eventi():
    categoria = request.args.get('categoria')
    citta = request.args.get('citta')
    
    query = "SELECT * FROM eventi WHERE 1=1"
    params = []
    
    if categoria:
        query += " AND categoria = %s"
        params.append(categoria)
    if citta:
        query += " AND luogo = %s"
        params.append(citta)
        
    query += " ORDER BY data_evento ASC"
    
    eventi = db.select(query, params)
    return jsonify(eventi)

# AREA PUBBLICA: Dettaglio singolo evento
@app.route('/api/eventi/<int:id>', methods=['GET'])
def get_evento(id):
    evento = db.select_one("SELECT * FROM eventi WHERE id = %s", [id])
    if not evento:
        return jsonify({"error": "Evento non trovato"}), 404
    return jsonify(evento)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
