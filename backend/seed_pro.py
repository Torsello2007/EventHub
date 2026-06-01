from database_wrapper import DatabaseWrapper
db = DatabaseWrapper()

# Puliamo i vecchi dati
db.execute("DELETE FROM eventi")

# Inseriamo 3 eventi di categorie diverse
eventi = [
    ('Milano Summer Festival', 'Il più grande concerto rock dell\'estate con band internazionali.', '2026-07-15 20:30:00', 'Ippodromo San Siro', 500, 'Musica', 45.00),
    ('Masterclass Angular 18', 'Impara a costruire app moderne con le ultime feature del framework.', '2026-09-10 09:00:00', 'Online / Zoom', 50, 'Workshop', 15.00),
    ('Presentazione: Il Futuro dell\'AI', 'Incontro con l\'autore del bestseller sulle intelligenze artificiali.', '2026-06-20 18:00:00', 'Libreria Centrale', 30, 'Libri', 0.00)
]

for e in eventi:
    db.execute("INSERT INTO eventi (titolo, descrizione, data_evento, luogo, posti_disponibili, categoria, prezzo, locandina_url) VALUES (%s,%s,%s,%s,%s,%s,%s,'')", e)

print("Database aggiornato con 3 eventi!")
