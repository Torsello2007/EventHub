from database_wrapper import DatabaseWrapper
db = DatabaseWrapper()

# Crea Tabella Eventi
db.execute("""
CREATE TABLE IF NOT EXISTS eventi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titolo VARCHAR(255) NOT NULL,
    descrizione TEXT,
    data_evento DATETIME,
    luogo VARCHAR(255),
    posti_disponibili INT,
    categoria VARCHAR(100),
    prezzo DECIMAL(10, 2),
    locandina_url TEXT
)
""")

# Inserisci un evento se la tabella è vuota
check = db.select("SELECT id FROM eventi")
if not check:
    db.execute("INSERT INTO eventi (titolo, descrizione, data_evento, luogo, posti_disponibili, categoria, prezzo, locandina_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
               ('Grande Concerto Rock', 'Un evento incredibile live a Milano.', '2026-07-20 21:00:00', 'Milano', 100, 'Musica', 25.00, ''))
    print("Tabelle create e Evento inserito!")
else:
    print("Le tabelle esistono già e hanno dati.")
