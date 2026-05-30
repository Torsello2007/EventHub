from flask import Flask, jsonify, request, send_from_directory, g, Response
from flask_cors import CORS
from database_wrapper import DatabaseWrapper
from auth import require_auth, require_role
import os, io, csv
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
db = DatabaseWrapper()
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/api/eventi', methods=['GET'])
def get_eventi():
    return jsonify(db.select("SELECT * FROM eventi ORDER BY data_evento ASC"))

@app.route('/api/eventi/<int:id>', methods=['GET'])
def get_evento(id):
    evento = db.select_one("SELECT * FROM eventi WHERE id = %s", [id])
    return jsonify(evento)

# --- DASHBOARD ORGANIZZATORE: Statistiche ---
@app.route('/api/organizzatore/statistiche', methods=['GET'])
@require_auth
@require_role('organizer')
def get_stats():
    query = """
        SELECT e.titolo, COUNT(i.id) as iscritti, (COUNT(i.id) * e.prezzo) as incasso_stimato
        FROM eventi e
        LEFT JOIN iscrizioni i ON e.id = i.id_evento
        GROUP BY e.id
    """
    stats = db.select(query)
    return jsonify(stats)

# --- AREA ORGANIZZATORE: Esportazione CSV ---
@app.route('/api/organizzatore/eventi/<int:id_evento>/csv', methods=['GET'])
@require_auth
@require_role('organizer')
def export_csv(id_evento):
    iscritti = db.select("SELECT username_utente, data_iscrizione FROM iscrizioni WHERE id_evento = %s", [id_evento])
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Username', 'Data Iscrizione'])
    for i in iscritti:
        writer.writerow([i['username_utente'], i['data_iscrizione']])
    
    output.seek(0)
    return Response(output, mimetype="text/csv", headers={"Content-disposition": f"attachment; filename=iscritti_evento_{id_evento}.csv"})

# (Mantieni le altre rotte già create per iscrizione, create_evento, ecc.)
@app.route('/api/eventi/<int:id_evento>/iscriviti', methods=['POST'])
@require_auth
def iscriviti_evento(id_evento):
    username = g.user.get('preferred_username')
    db.execute("INSERT INTO iscrizioni (id_evento, username_utente) VALUES (%s, %s)", [id_evento, username])
    return jsonify({"message": "Iscritto!"}), 201

@app.route('/api/organizzatore/eventi', methods=['POST'])
@require_auth
@require_role('organizer')
def create_evento():
    f = request.form
    file = request.files.get('immagine')
    filename = secure_filename(file.filename) if file else ""
    if file: file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    query = "INSERT INTO eventi (titolo, descrizione, data_evento, luogo, posti_disponibili, categoria, prezzo, locandina_url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    db.execute(query, [f['titolo'], f['descrizione'], f['data_evento'], f['luogo'], f['posti_disponibili'], f['categoria'], f['prezzo'], filename])
    return jsonify({"message": "Evento creato"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
