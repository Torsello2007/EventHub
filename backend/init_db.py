from database_wrapper import DatabaseWrapper
db = DatabaseWrapper()

print("Creazione tabelle in corso...")

# 1. Tabella Eventi
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

# 2. Tabella Iscrizioni
db.execute("""
CREATE TABLE IF NOT EXISTS iscrizioni (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT,
    username_utente VARCHAR(255),
    data_iscrizione TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_evento) REFERENCES eventi(id) ON DELETE CASCADE
)
""")

# 3. Tabella Recensioni
db.execute("""
CREATE TABLE IF NOT EXISTS recensioni (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT,
    username_utente VARCHAR(255),
    rating INT,
    commento TEXT,
    data_recensione TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_evento) REFERENCES eventi(id) ON DELETE CASCADE
)
""")

# 4. Inserimento evento di prova
db.execute("INSERT INTO eventi (titolo, descrizione, data_evento, luogo, posti_disponibili, categoria, prezzo, locandina_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
           ('Grande Concerto Rock', 'Un evento incredibile live a Milano.', '2026-07-20 21:00:00', 'Milano', 100, 'Musica', 25.00, ''))

print("Database configurato correttamente con evento di prova!")
