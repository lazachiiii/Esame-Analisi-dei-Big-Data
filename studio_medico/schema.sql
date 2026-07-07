PRAGMA foreign_keys = ON;


CREATE TABLE IF NOT EXISTS Paziente (
    codice TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    data_nascita TEXT,
    indirizzo TEXT,
    telefono TEXT
);

CREATE TABLE IF NOT EXISTS Medico (
    codice TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    specializzazione TEXT,
    recapito TEXT
);

CREATE TABLE IF NOT EXISTS Visita (
    id TEXT PRIMARY KEY,
    data TEXT NOT NULL,
    ora TEXT NOT NULL,
    motivo TEXT,
    note TEXT,
    costo REAL,
    paziente_codice TEXT NOT NULL,
    medico_codice TEXT NOT NULL,
    FOREIGN KEY (paziente_codice) REFERENCES Paziente(codice),
    FOREIGN KEY (medico_codice) REFERENCES Medico(codice)
);

CREATE TABLE IF NOT EXISTS Farmaco (
    codice TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    princ_attivo TEXT,
    casa_farm TEXT
);

CREATE TABLE IF NOT EXISTS Prescrizione (
    id TEXT PRIMARY KEY,
    posologia TEXT,
    durata TEXT,
    visita_id TEXT NOT NULL,
    farmaco_codice TEXT NOT NULL,
    FOREIGN KEY (visita_id) REFERENCES Visita(id),
    FOREIGN KEY (farmaco_codice) REFERENCES Farmaco(codice)
);
