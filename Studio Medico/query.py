import os
import sqlite3
import sys

DB_NAME = 'studio_medico.db'
SCHEMA_FILE = 'schema.sql'
DATA_FILE = 'dati.sql'

CREATE_STUDIO_SCHEMA = None
INSERT_STUDIO_DATA = None


def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def execute_script(connection, script):
    cursor = connection.cursor()
    cursor.executescript(script)
    connection.commit()


def query_visite_paziente(connection, paziente_codice):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT v.id, v.data, v.ora, v.motivo, v.note, v.costo, m.nome || ' ' || m.cognome AS medico
        FROM Visita v
        JOIN Medico m ON v.medico_codice = m.codice
        WHERE v.paziente_codice = ?
        ORDER BY v.data, v.ora
        ''',
        (paziente_codice,)
    )
    return cursor.fetchall()


def query_farmaci_per_medico(connection, medico_codice):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT DISTINCT f.codice, f.nome, f.princ_attivo, f.casa_farm
        FROM Prescrizione p
        JOIN Visita v ON p.visita_id = v.id
        JOIN Farmaco f ON p.farmaco_codice = f.codice
        WHERE v.medico_codice = ?
        ORDER BY f.nome
        ''',
        (medico_codice,)
    )
    return cursor.fetchall()


def print_visite(visite, paziente_descrizione):
    print(f"Visite per il paziente {paziente_descrizione}:\n")
    if not visite:
        print("Nessuna visita trovata.\n")
        return

    for visita in visite:
        id_, data, ora, motivo, note, costo, medico = visita
        print(f"- {id_}: {data} {ora} | Motivo: {motivo} | Note: {note} | Costo: {costo:.2f} | Medico: {medico}")
    print()


def print_farmaci(farmaci, medico_descrizione):
    print(f"Farmaci prescritti dal medico {medico_descrizione}:\n")
    if not farmaci:
        print("Nessun farmaco trovato.\n")
        return

    for codice, nome, princ_attivo, casa_farm in farmaci:
        print(f"- {codice}: {nome} | Principio attivo: {princ_attivo} | Casa farmaceutica: {casa_farm}")
    print()


def query_pazienti_per_medico(connection, medico_codice):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT DISTINCT p.codice, p.nome, p.cognome
        FROM Visita v
        JOIN Paziente p ON v.paziente_codice = p.codice
        WHERE v.medico_codice = ?
        ORDER BY p.cognome, p.nome
        ''',
        (medico_codice,)
    )
    return cursor.fetchall()


def query_farmaci_per_paziente(connection, paziente_codice):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT DISTINCT f.codice, f.nome, f.princ_attivo, f.casa_farm
        FROM Prescrizione pr
        JOIN Visita v ON pr.visita_id = v.id
        JOIN Farmaco f ON pr.farmaco_codice = f.codice
        WHERE v.paziente_codice = ?
        ORDER BY f.nome
        ''',
        (paziente_codice,)
    )
    return cursor.fetchall()


def print_pazienti_per_medico(pazienti, medico_descrizione):
    print(f"Pazienti distinti seguiti dal medico {medico_descrizione}:\n")
    if not pazienti:
        print("Nessun paziente trovato.\n")
        return

    for codice, nome, cognome in pazienti:
        print(f"- {codice}: {nome} {cognome}")
    print()


def print_farmaci_per_paziente(farmaci, paziente_descrizione):
    print(f"Farmaci prescritti al paziente {paziente_descrizione}:\n")
    if not farmaci:
        print("Nessun farmaco trovato.\n")
        return

    for codice, nome, princ_attivo, casa_farm in farmaci:
        print(f"- {codice}: {nome} | Principio attivo: {princ_attivo} | Casa farmaceutica: {casa_farm}")
    print()


def initialize_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    schema_sql = load_file(SCHEMA_FILE)
    dati_sql = load_file(DATA_FILE)

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('PRAGMA foreign_keys = ON;')
        execute_script(conn, schema_sql)
        execute_script(conn, dati_sql)


COMANDI = {
    'visite': "visite <codice_paziente>",
    'farmaci-medico': "farmaci-medico <codice_medico>",
    'pazienti-medico': "pazienti-medico <codice_medico>",
    'farmaci-paziente': "farmaci-paziente <codice_paziente>",
}


def print_help():
    print("Comandi disponibili:")
    for uso in COMANDI.values():
        print(f"  python3 query.py {uso}")


def main():
    initialize_database()

    with sqlite3.connect(DB_NAME) as conn:
        args = sys.argv[1:]

        if not args or args[0] not in COMANDI:
            comando = args[0] if args else None
            if comando is None:
                print("Errore: nessun comando specificato.\n")
            else:
                print(f"Errore: comando sconosciuto '{comando}'.\n")
            print_help()
            return

        command = args[0]

        if len(args) != 2:
            print(f"Errore: parametro mancante o in eccesso per '{command}'.")
            print(f"Uso: python3 query.py {COMANDI[command]}\n")
            print_help()
            return

        codice = args[1]

        if command == 'visite':
            visite = query_visite_paziente(conn, codice)
            print_visite(visite, codice)

        elif command == 'farmaci-medico':
            farmaci = query_farmaci_per_medico(conn, codice)
            print_farmaci(farmaci, codice)

        elif command == 'pazienti-medico':
            pazienti = query_pazienti_per_medico(conn, codice)
            print_pazienti_per_medico(pazienti, codice)

        elif command == 'farmaci-paziente':
            farmaci = query_farmaci_per_paziente(conn, codice)
            print_farmaci_per_paziente(farmaci, codice)


if __name__ == '__main__':
    main()

