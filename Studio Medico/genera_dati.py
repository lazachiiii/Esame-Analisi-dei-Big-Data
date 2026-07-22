# -*- coding: utf-8 -*-
"""
Genera un dati.sql popolato con un dataset realistico e coerente per lo studio
medico, mantenendo intatti i record originali (P001-P006, M001-M004, F001-F006,
V001-V010, PR001-PR008) e aggiungendo nuovi individui/eventi in coda, con la
stessa struttura e lo stesso stile del file esistente.

Uso:
    python3 genera_dati.py

Sovrascrive il file dati.sql nella cartella corrente.
"""

import random

random.seed(42)  # risultati riproducibili ad ogni esecuzione

# ==============================================================================
# PARAMETRI DEL DATASET
# ==============================================================================
N_PAZIENTI_TOTALI = 200
N_MEDICI_TOTALI = 12
N_FARMACI_TOTALI = 40
N_VISITE_TOTALI = 500
PROBABILITA_PRESCRIZIONE_PER_VISITA = 0.76  # ~380 prescrizioni su 500 visite

# ==============================================================================
# DATI ANAGRAFICI DI SUPPORTO
# ==============================================================================
NOMI_MASCHILI = [
    "Carlo", "Pietro", "Raffaele", "Marco", "Andrea", "Luca", "Giovanni", "Paolo",
    "Francesco", "Alessandro", "Matteo", "Davide", "Simone", "Roberto", "Stefano",
    "Antonio", "Giuseppe", "Fabio", "Riccardo", "Enrico", "Massimo", "Claudio",
    "Sergio", "Vittorio", "Emanuele", "Lorenzo", "Tommaso", "Federico", "Nicola",
    "Salvatore", "Angelo", "Bruno", "Dario", "Emilio", "Franco", "Gianni",
    "Ignazio", "Leonardo", "Mario", "Nicolò", "Ottavio", "Renato", "Silvio",
    "Umberto", "Valerio", "Walter",
]

NOMI_FEMMINILI = [
    "Matilde", "Eva", "Gina", "Giulia", "Chiara", "Francesca", "Sofia", "Elena",
    "Laura", "Silvia", "Valentina", "Alessia", "Martina", "Federica", "Serena",
    "Elisa", "Ilaria", "Cristina", "Barbara", "Roberta", "Simona", "Daniela",
    "Patrizia", "Antonella", "Rosa", "Anna", "Maria", "Paola", "Lucia", "Sara",
    "Beatrice", "Camilla", "Diana", "Emma", "Flavia", "Greta", "Irene", "Jessica",
    "Lara", "Nadia", "Ornella", "Piera", "Rita", "Stefania", "Teresa", "Vera",
]

COGNOMI = [
    "Palermo", "Costa", "Sagese", "Colombo", "Fanucci", "Marchesi", "Rossi",
    "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Gallo", "Conti",
    "De Luca", "Mancini", "Costantini", "Giordano", "Rizzo", "Lombardi",
    "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso",
    "Ferrara", "Galli", "Martini", "Leone", "Longo", "Gentile", "Martinelli",
    "Vitale", "Bruno", "Serra", "Coppola", "Basile", "Silvestri", "Farina",
    "Pellegrini", "D'Angelo", "Bellini", "Fiore", "Bianco", "Marini", "Grasso",
    "Valentini", "Ferri", "Gatti", "Sanna", "Testa", "Monti", "Riva", "Guerra",
    "De Santis", "Amato", "Villa", "Bernardi",
]

VIE = [
    "Via Giuseppe Garibaldi", "Via Galvani", "Via Alcide De Gasperi",
    "Via Calcirelli", "Via Sacchi", "Via delle Coste", "Via Roma", "Via Dante",
    "Via Milano", "Via Torino", "Corso Vittorio Emanuele", "Via Mazzini",
    "Via Cavour", "Viale Europa", "Via Trieste", "Via Napoli", "Via Firenze",
    "Via Verdi", "Via Leopardi", "Via Manzoni", "Via Petrarca", "Via dei Mille",
    "Via San Francesco", "Via del Popolo", "Via Aldo Moro",
]


def genera_telefono():
    prefisso = random.choice(["0321", "0322", "0323", "0327", "0331", "0341",
                               "0342", "0358", "0398", "0312"])
    numero = "".join(str(random.randint(0, 9)) for _ in range(7))
    return f"{prefisso} {numero[:1]}{numero[1:]}"


def genera_indirizzo():
    via = random.choice(VIE)
    civico = random.randint(1, 180)
    return f"{via}, {civico}"


def genera_data_nascita():
    anno = random.randint(1940, 2007)
    mese = random.randint(1, 12)
    giorno = random.randint(1, 28)
    return f"{anno:04d}-{mese:02d}-{giorno:02d}"


def genera_data_visita():
    anno = random.choice([2023, 2024, 2025])
    mese = random.randint(1, 12)
    giorno = random.randint(1, 28)
    return f"{anno:04d}-{mese:02d}-{giorno:02d}"


def genera_ora():
    ora = random.randint(9, 17)
    minuto = random.choice(["00", "15", "30", "45"])
    return f"{ora:02d}:{minuto}"


# ==============================================================================
# PAZIENTI (P001-P006 esistenti + nuovi fino a 200)
# ==============================================================================
def genera_pazienti():
    pazienti = [
        ("P001", "Carlo", "Palermo", "2003-09-24", "Via Giuseppe Garibaldi, 9", "0327 5017538"),
        ("P002", "Matilde", "Costa", "2001-01-13", "Via Galvani, 39", "0398 1963448"),
        ("P003", "Pietro", "Sagese", "1968-10-18", "Via Alcide De Gasperi, 67", "0342 8057122"),
        ("P004", "Raffaele", "Colombo", "1956-03-04", "Via Calcirelli, 37", "0322 0192612"),
        ("P005", "Eva", "Fanucci", "1992-05-15", "Via Sacchi, 124", "0398 2526615"),
        ("P006", "Gina", "Marchesi", "1944-10-21", "Via delle Coste, 82", "0312 5772958"),
    ]

    usati = set()
    for i in range(7, N_PAZIENTI_TOTALI + 1):
        codice = f"P{i:03d}"
        while True:
            if random.random() < 0.5:
                nome = random.choice(NOMI_MASCHILI)
            else:
                nome = random.choice(NOMI_FEMMINILI)
            cognome = random.choice(COGNOMI)
            if (nome, cognome) not in usati:
                usati.add((nome, cognome))
                break
        pazienti.append((
            codice, nome, cognome, genera_data_nascita(),
            genera_indirizzo(), genera_telefono()
        ))
    return pazienti


# ==============================================================================
# MEDICI (M001-M004 esistenti + nuovi fino a 12)
# ==============================================================================
def genera_medici():
    medici = [
        ("M001", "Dalia", "Rizzo", "Neurologia", "0323 3544451"),
        ("M002", "Ludovica", "Manfredi", "Cardiologia", "0341 9523395"),
        ("M003", "Umberto", "Borghi", "Endocrinologia", "0358 0533869"),
        ("M004", "Massimiliano", "Rinaldis", "Ortopedia", "0398 6363959"),
    ]

    nuove_specializzazioni = [
        "Neurologia", "Cardiologia", "Endocrinologia", "Ortopedia",
        "Dermatologia", "Pediatria", "Ginecologia", "Oncologia",
    ]
    nomi_nuovi_medici = [
        ("Alessia", "Ferretti"), ("Davide", "Sartori"), ("Chiara", "Bellucci"),
        ("Simone", "Greco"), ("Federica", "Ricci"), ("Nicola", "Marino"),
        ("Silvia", "Barone"), ("Andrea", "Fabbri"),
    ]

    for i, (spec, (nome, cognome)) in enumerate(zip(nuove_specializzazioni, nomi_nuovi_medici), start=5):
        codice = f"M{i:03d}"
        medici.append((codice, nome, cognome, spec, genera_telefono()))
    return medici


# ==============================================================================
# FARMACI (F001-F006 esistenti + nuovi fino a 40)
# ==============================================================================
def genera_farmaci():
    farmaci = [
        ("F001", "Imigran", "Sumatriptan", "GSK"),
        ("F002", "Cardioaspirina", "Acido Acetilsalicilico", "Bayer"),
        ("F003", "Coumadin", "Warfarin", "Bristol-Myers"),
        ("F004", "Metformina", "Metformina", "Merck"),
        ("F005", "Eutirox", "Levotiroxina", "Merck"),
        ("F006", "Voltaren", "Diclofenac", "Novartis"),
    ]

    nuovi_farmaci = [
        ("Tachipirina", "Paracetamolo", "Angelini"),
        ("Augmentin", "Amoxicillina/Acido Clavulanico", "GSK"),
        ("Zoloft", "Sertralina", "Pfizer"),
        ("Xanax", "Alprazolam", "Pfizer"),
        ("Lasix", "Furosemide", "Sanofi"),
        ("Zantac", "Ranitidina", "GSK"),
        ("Nurofen", "Ibuprofene", "Reckitt"),
        ("Norvasc", "Amlodipina", "Pfizer"),
        ("Lipitor", "Atorvastatina", "Pfizer"),
        ("Prozac", "Fluoxetina", "Eli Lilly"),
        ("Ventolin", "Salbutamolo", "GSK"),
        ("Omeprazolo Teva", "Omeprazolo", "Teva"),
        ("Bentelan", "Betametasone", "Defiante"),
        ("Deltacortene", "Prednisone", "Bruno Farmaceutici"),
        ("Zyrtec", "Cetirizina", "UCB"),
        ("Enterogermina", "Bacillus Clausii", "Sanofi"),
        ("Moment", "Ibuprofene", "Angelini"),
        ("Diflucan", "Fluconazolo", "Pfizer"),
        ("Aulin", "Nimesulide", "Roche"),
        ("Losartan Teva", "Losartan", "Teva"),
        ("Depakin", "Acido Valproico", "Sanofi"),
        ("Rivotril", "Clonazepam", "Roche"),
        ("Motilium", "Domperidone", "Johnson & Johnson"),
        ("Buscopan", "Butilscopolamina", "Sanofi"),
        ("Clarityn", "Loratadina", "Bayer"),
        ("Insulina Lantus", "Insulina Glargine", "Sanofi"),
        ("Micardis", "Telmisartan", "Boehringer Ingelheim"),
        ("Symbicort", "Budesonide/Formoterolo", "AstraZeneca"),
        ("Diamicron", "Gliclazide", "Servier"),
        ("Priligy", "Dapoxetina", "Menarini"),
        ("Levotiroxina EG", "Levotiroxina", "EG Stada"),
        ("Cortisone Acetato", "Cortisone", "Bruno Farmaceutici"),
        ("Antra", "Omeprazolo", "AstraZeneca"),
        ("Muscoril", "Tiocolchicoside", "Sanofi"),
    ]

    for i, (nome, principio, casa) in enumerate(nuovi_farmaci, start=7):
        codice = f"F{i:03d}"
        farmaci.append((codice, nome, principio, casa))
    return farmaci


# ==============================================================================
# VISITE (V001-V010 esistenti + nuove fino a 500)
# ==============================================================================
MOTIVI_PER_SPECIALIZZAZIONE = {
    "Neurologia": [("Mal di testa ricorrente", "Possibile emicrania"),
                   ("Cefalea cronica", "Emicrania con aura"),
                   ("Controllo neurologico", "Nessuna anomalia rilevata"),
                   ("Vertigini", "Da approfondire con esami strumentali")],
    "Cardiologia": [("Controllo cardiaco", "Pressione alta"),
                    ("Controllo cardiaco", "Aritmia lieve"),
                    ("Controllo cardiaco", "Colesterolo alto"),
                    ("Dolore toracico", "Da monitorare")],
    "Endocrinologia": [("Controllo glicemia", "Diabete di tipo 2"),
                       ("Controllo tiroide", "Ipotiroidismo"),
                       ("Controllo glicemia", "Valori nella norma"),
                       ("Squilibrio ormonale", "Da approfondire")],
    "Ortopedia": [("Dolore articolare", "Artrosi al ginocchio"),
                  ("Dolore alla schiena", "Ernia lombare"),
                  ("Trauma sportivo", "Distorsione alla caviglia"),
                  ("Controllo post-frattura", "Guarigione regolare")],
    "Dermatologia": [("Controllo nei", "Nessuna lesione sospetta"),
                     ("Dermatite", "Da contatto"),
                     ("Acne", "Trattamento in corso")],
    "Pediatria": [("Controllo di routine", "Crescita regolare"),
                  ("Febbre", "Sindrome influenzale"),
                  ("Vaccinazione", "Nessuna reazione avversa")],
    "Ginecologia": [("Controllo ginecologico", "Di routine"),
                    ("Visita di controllo", "Nessuna anomalia")],
    "Oncologia": [("Controllo oncologico", "Follow-up post trattamento"),
                  ("Visita di controllo", "Esami nella norma")],
}

COSTI_PER_SPECIALIZZAZIONE = {
    "Neurologia": 60.00, "Cardiologia": 50.00, "Endocrinologia": 45.00,
    "Ortopedia": 55.00, "Dermatologia": 50.00, "Pediatria": 40.00,
    "Ginecologia": 55.00, "Oncologia": 70.00,
}


def genera_visite(pazienti, medici):
    visite = [
        ("V001", "2025-01-10", "09:00", "Controllo cardiaco", "Pressione alta", 50.00, "P001", "M002"),
        ("V002", "2025-01-15", "10:30", "Mal di testa ricorrente", "Possibile emicrania", 60.00, "P002", "M001"),
        ("V003", "2025-02-05", "11:00", "Controllo cardiaco", "Aritmia lieve", 50.00, "P003", "M002"),
        ("V004", "2025-02-18", "14:00", "Cefalea cronica", "Emicrania con aura", 60.00, "P003", "M001"),
        ("V005", "2025-03-06", "09:30", "Dolore articolare", "Artrosi al ginocchio", 55.00, "P004", "M004"),
        ("V006", "2025-03-18", "11:30", "Controllo glicemia", "Diabete di tipo 2", 45.00, "P004", "M003"),
        ("V007", "2025-04-19", "10:00", "Controllo tiroide", "Ipotiroidismo", 45.00, "P005", "M003"),
        ("V008", "2025-05-10", "15:00", "Dolore alla schiena", "Ernia lombare", 55.00, "P006", "M004"),
        ("V009", "2025-05-22", "09:00", "Controllo cardiaco", "Colesterolo alto", 50.00, "P001", "M002"),
        ("V010", "2025-06-03", "11:00", "Controllo glicemia", "Valori nella norma", 45.00, "P005", "M003"),
    ]

    codici_pazienti = [p[0] for p in pazienti]
    medici_per_codice = {m[0]: m[3] for m in medici}  # codice -> specializzazione
    codici_medici = list(medici_per_codice.keys())

    for i in range(11, N_VISITE_TOTALI + 1):
        id_visita = f"V{i:03d}"
        paziente_codice = random.choice(codici_pazienti)
        medico_codice = random.choice(codici_medici)
        specializzazione = medici_per_codice[medico_codice]

        opzioni = MOTIVI_PER_SPECIALIZZAZIONE.get(specializzazione,
                                                     [("Visita di controllo", "Nessuna anomalia")])
        motivo, nota = random.choice(opzioni)
        costo = COSTI_PER_SPECIALIZZAZIONE.get(specializzazione, 50.00)

        visite.append((
            id_visita, genera_data_visita(), genera_ora(), motivo, nota,
            costo, paziente_codice, medico_codice
        ))
    return visite


# ==============================================================================
# PRESCRIZIONI (PR001-PR008 esistenti + nuove)
# ==============================================================================
POSOLOGIE = [
    ("1 compressa al giorno", "30 giorni"),
    ("1 compressa al bisogno", "15 giorni"),
    ("1 compressa al giorno", "60 giorni"),
    ("1 compressa al bisogno", "20 giorni"),
    ("1 gel applicazione locale 2x giorno", "20 giorni"),
    ("1 compressa 2x giorno", "90 giorni"),
    ("1 compressa al giorno", "180 giorni"),
    ("1 bustina al giorno", "10 giorni"),
    ("2 compresse al giorno", "14 giorni"),
    ("1 fiala intramuscolo", "7 giorni"),
    ("1 compressa alla sera", "45 giorni"),
    ("1 spray nasale al bisogno", "30 giorni"),
]


def genera_prescrizioni(visite, farmaci):
    prescrizioni = [
        ("PR001", "1 compressa al giorno", "30 giorni", "V001", "F002"),
        ("PR002", "1 compressa al bisogno", "15 giorni", "V002", "F001"),
        ("PR003", "1 compressa al giorno", "60 giorni", "V003", "F003"),
        ("PR004", "1 compressa al bisogno", "20 giorni", "V004", "F001"),
        ("PR005", "1 gel applicazione locale 2x giorno", "20 giorni", "V005", "F006"),
        ("PR006", "1 compressa 2x giorno", "90 giorni", "V006", "F004"),
        ("PR007", "1 compressa al giorno", "180 giorni", "V007", "F005"),
        ("PR008", "1 compressa al giorno", "30 giorni", "V009", "F002"),
    ]

    codici_farmaci = [f[0] for f in farmaci]
    # V001-V010 già hanno le loro prescrizioni originali (tranne V008, V010: nessuna, come nel dataset di partenza)
    visite_gia_prescritte = {"V001", "V002", "V003", "V004", "V005", "V006", "V007", "V009"}

    contatore = 9
    for visita in visite:
        id_visita = visita[0]
        if id_visita in visite_gia_prescritte:
            continue
        if random.random() < PROBABILITA_PRESCRIZIONE_PER_VISITA:
            posologia, durata = random.choice(POSOLOGIE)
            farmaco_codice = random.choice(codici_farmaci)
            id_prescrizione = f"PR{contatore:03d}"
            prescrizioni.append((id_prescrizione, posologia, durata, id_visita, farmaco_codice))
            contatore += 1

    return prescrizioni


# ==============================================================================
# SCRITTURA DEL FILE dati.sql
# ==============================================================================
def sql_string(valore):
    if valore is None:
        return "NULL"
    return "'" + str(valore).replace("'", "''") + "'"


def formatta_insert(tabella, colonne, righe):
    intestazione = f"INSERT INTO {tabella} ({', '.join(colonne)}) VALUES\n"
    righe_formattate = []
    for riga in righe:
        valori = []
        for valore in riga:
            if isinstance(valore, float):
                valori.append(f"{valore:.2f}")
            else:
                valori.append(sql_string(valore))
        righe_formattate.append("(" + ", ".join(valori) + ")")
    return intestazione + ",\n".join(righe_formattate) + ";\n"


def main():
    pazienti = genera_pazienti()
    medici = genera_medici()
    farmaci = genera_farmaci()
    visite = genera_visite(pazienti, medici)
    prescrizioni = genera_prescrizioni(visite, farmaci)

    blocchi = [
        "PRAGMA foreign_keys = ON;\n",
        formatta_insert("Paziente",
                         ["codice", "nome", "cognome", "data_nascita", "indirizzo", "telefono"],
                         pazienti),
        formatta_insert("Medico",
                         ["codice", "nome", "cognome", "specializzazione", "recapito"],
                         medici),
        formatta_insert("Farmaco",
                         ["codice", "nome", "princ_attivo", "casa_farm"],
                         farmaci),
        formatta_insert("Visita",
                         ["id", "data", "ora", "motivo", "note", "costo", "paziente_codice", "medico_codice"],
                         visite),
        formatta_insert("Prescrizione",
                         ["id", "posologia", "durata", "visita_id", "farmaco_codice"],
                         prescrizioni),
    ]

    with open("dati.sql", "w", encoding="utf-8") as f:
        f.write("\n".join(blocchi))

    print(f"dati.sql generato con successo:")
    print(f"  - {len(pazienti)} pazienti")
    print(f"  - {len(medici)} medici")
    print(f"  - {len(farmaci)} farmaci")
    print(f"  - {len(visite)} visite")
    print(f"  - {len(prescrizioni)} prescrizioni")


if __name__ == "__main__":
    main()