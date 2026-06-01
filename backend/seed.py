from database_wrapper import DatabaseWrapper
db = DatabaseWrapper()
db.execute("INSERT INTO eventi (titolo, descrizione, data_evento, luogo, posti_disponibili, categoria, prezzo, locandina_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
           ('Grande Concerto Rock', 'Un evento incredibile live a Milano.', '2026-07-20 21:00:00', 'Milano', 100, 'Musica', 25.00, ''))
print("Evento di prova inserito correttamente!")
