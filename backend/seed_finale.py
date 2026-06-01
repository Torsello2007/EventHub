from database_wrapper import DatabaseWrapper
db = DatabaseWrapper()
db.execute("DELETE FROM recensioni")
db.execute("DELETE FROM iscrizioni")
db.execute("DELETE FROM eventi")
eventi = [
    ('Festival Jazz Milano', 'Una serata indimenticabile sotto le stelle con i migliori artisti jazz.', '2026-07-15 21:00:00', 'Castello Sforzesco', 200, 'Musica', 35.00),
    ('Workshop Fotografia', 'Impara le tecniche di base e avanzate con fotografi professionisti.', '2026-08-10 10:00:00', 'Studio Luce', 25, 'Workshop', 50.00),
    ('Fiera del Libro', 'Presentazioni con autori famosi e sconti su tutte le ultime uscite.', '2026-06-25 15:00:00', 'Palazzo Reale', 500, 'Libri', 0.00)
]
for e in eventi:
    db.execute("INSERT INTO eventi (titolo, descrizione, data_evento, luogo, posti_disponibili, categoria, prezzo, locandina_url) VALUES (%s,%s,%s,%s,%s,%s,%s,'')", e)
print("Database popolato con 3 eventi reali!")
