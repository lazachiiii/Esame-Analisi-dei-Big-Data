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


def get_all_pazienti(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT codice, nome, cognome
        FROM Paziente
        ORDER BY cognome, nome
        '''
    )
    return cursor.fetchall()


def get_all_medici(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT codice, nome, cognome
        FROM Medico
        ORDER BY cognome, nome
        '''
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


def query_numero_visite_per_paziente(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT p.codice, p.nome, p.cognome, COUNT(v.id) AS numero_visite
        FROM Paziente p
        LEFT JOIN Visita v ON p.codice = v.paziente_codice
        GROUP BY p.codice, p.nome, p.cognome
        ORDER BY p.cognome, p.nome
        '''
    )
    return cursor.fetchall()


def query_spesa_totale_per_paziente(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT p.codice, p.nome, p.cognome, COALESCE(SUM(v.costo), 0) AS spesa_totale
        FROM Paziente p
        LEFT JOIN Visita v ON p.codice = v.paziente_codice
        GROUP BY p.codice, p.nome, p.cognome
        ORDER BY p.cognome, p.nome
        '''
    )
    return cursor.fetchall()


def query_prescrizioni_anno(connection, anno):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT pr.id, v.data, v.ora, p.codice AS paziente_codice, p.nome || ' ' || p.cognome AS paziente,
               m.codice AS medico_codice, m.nome || ' ' || m.cognome AS medico,
               f.codice AS farmaco_codice, f.nome AS farmaco, pr.posologia, pr.durata
        FROM Prescrizione pr
        JOIN Visita v ON pr.visita_id = v.id
        JOIN Paziente p ON v.paziente_codice = p.codice
        JOIN Medico m ON v.medico_codice = m.codice
        JOIN Farmaco f ON pr.farmaco_codice = f.codice
        WHERE substr(v.data, 1, 4) = ?
        ORDER BY v.data, v.ora, pr.id
        ''',
        (anno,)
    )
    return cursor.fetchall()


def query_pazienti_per_farmaco(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT DISTINCT f.codice, f.nome, p.codice, p.nome, p.cognome
        FROM Farmaco f
        JOIN Prescrizione pr ON f.codice = pr.farmaco_codice
        JOIN Visita v ON pr.visita_id = v.id
        JOIN Paziente p ON v.paziente_codice = p.codice
        ORDER BY f.nome, p.cognome, p.nome
        '''
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


def print_numero_visite_per_paziente(statistiche):
    print("Numero di visite per paziente:\n")
    if not statistiche:
        print("Nessun paziente trovato.\n")
        return

    for codice, nome, cognome, numero_visite in statistiche:
        print(f"- {codice}: {nome} {cognome} | Visite: {numero_visite}")
    print()


def print_spesa_totale_per_paziente(statistiche):
    print("Spesa totale per paziente:\n")
    if not statistiche:
        print("Nessun paziente trovato.\n")
        return

    for codice, nome, cognome, spesa_totale in statistiche:
        print(f"- {codice}: {nome} {cognome} | Spesa totale: {spesa_totale:.2f}")
    print()


def print_prescrizioni_anno(prescrizioni, anno):
    print(f"Prescrizioni effettuate nell'anno {anno}:\n")
    if not prescrizioni:
        print("Nessuna prescrizione trovata.\n")
        return

    for pr_id, data, ora, paziente_codice, paziente, medico_codice, medico, farmaco_codice, farmaco, posologia, durata in prescrizioni:
        print(f"- {pr_id}: {data} {ora} | Paziente: {paziente_codice} ({paziente}) | Medico: {medico_codice} ({medico}) | Farmaco: {farmaco_codice} ({farmaco}) | Posologia: {posologia} | Durata: {durata}")
    print()


def print_pazienti_per_farmaco(pazienti_per_farmaco):
    print("Pazienti che hanno ricevuto ciascun farmaco:\n")
    if not pazienti_per_farmaco:
        print("Nessun farmaco trovato.\n")
        return

    current_farmaco = None
    for farmaco_codice, farmaco_nome, paziente_codice, paziente_nome, paziente_cognome in pazienti_per_farmaco:
        if current_farmaco != farmaco_nome:
            if current_farmaco is not None:
                print()
            print(f"{farmaco_codice}: {farmaco_nome}")
            current_farmaco = farmaco_nome
        print(f"  - {paziente_codice}: {paziente_nome} {paziente_cognome}")
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


def print_help():
    print("Comandi disponibili:")
    print("  visite <codice_paziente>")
    print("  farmaci-medico <codice_medico>")
    print("  pazienti-medico <codice_medico>")
    print("  farmaci-paziente <codice_paziente>")
    print("  spesa")
    print("  visite-count")
    print("  prescrizioni-2025")
    print("  farmaco-pazienti")
    print("  tutto")


def run_all_reports(conn):
    pazienti = get_all_pazienti(conn)
    medici = get_all_medici(conn)

    print("=== Visite per paziente ===")
    for codice, nome, cognome in pazienti:
        visite = query_visite_paziente(conn, codice)
        print_visite(visite, f"{codice} ({nome} {cognome})")

    print("=== Farmaci prescritti per medico ===")
    for codice, nome, cognome in medici:
        farmaci = query_farmaci_per_medico(conn, codice)
        print_farmaci(farmaci, f"{codice} ({nome} {cognome})")

    print("=== Pazienti distinti per medico ===")
    for codice, nome, cognome in medici:
        pazienti_per_medico = query_pazienti_per_medico(conn, codice)
        print_pazienti_per_medico(pazienti_per_medico, f"{codice} ({nome} {cognome})")

    print("=== Farmaci presi da ciascun paziente ===")
    for codice, nome, cognome in pazienti:
        farmaci_paziente = query_farmaci_per_paziente(conn, codice)
        print_farmaci_per_paziente(farmaci_paziente, f"{codice} ({nome} {cognome})")

    print("=== Numero di visite per paziente ===")
    visite_per_paziente = query_numero_visite_per_paziente(conn)
    print_numero_visite_per_paziente(visite_per_paziente)

    print("=== Spesa totale per paziente ===")
    spesa_per_paziente = query_spesa_totale_per_paziente(conn)
    print_spesa_totale_per_paziente(spesa_per_paziente)

    print("=== Prescrizioni effettuate nel 2025 ===")
    prescrizioni_2025 = query_prescrizioni_anno(conn, '2025')
    print_prescrizioni_anno(prescrizioni_2025, '2025')

    print("=== Pazienti che hanno ricevuto ciascun farmaco ===")
    pazienti_per_farmaco = query_pazienti_per_farmaco(conn)
    print_pazienti_per_farmaco(pazienti_per_farmaco)


def main():
    initialize_database()

    with sqlite3.connect(DB_NAME) as conn:
        args = sys.argv[1:]
        if not args:
            print_help()
            return

        command = args[0]

        if command == 'visite':
            if len(args) != 2:
                print("Uso: python3 query.py visite <codice_paziente>")
                return
            visite = query_visite_paziente(conn, args[1])
            print_visite(visite, args[1])

        elif command == 'farmaci-medico':
            if len(args) != 2:
                print("Uso: python3 query.py farmaci-medico <codice_medico>")
                return
            farmaci = query_farmaci_per_medico(conn, args[1])
            print_farmaci(farmaci, args[1])

        elif command == 'pazienti-medico':
            if len(args) != 2:
                print("Uso: python3 query.py pazienti-medico <codice_medico>")
                return
            pazienti = query_pazienti_per_medico(conn, args[1])
            print_pazienti_per_medico(pazienti, args[1])

        elif command == 'farmaci-paziente':
            if len(args) != 2:
                print("Uso: python3 query.py farmaci-paziente <codice_paziente>")
                return
            farmaci = query_farmaci_per_paziente(conn, args[1])
            print_farmaci_per_paziente(farmaci, args[1])

        elif command == 'spesa':
            spesa_per_paziente = query_spesa_totale_per_paziente(conn)
            print_spesa_totale_per_paziente(spesa_per_paziente)

        elif command == 'visite-count':
            visite_per_paziente = query_numero_visite_per_paziente(conn)
            print_numero_visite_per_paziente(visite_per_paziente)

        elif command == 'prescrizioni-2025':
            prescrizioni_2025 = query_prescrizioni_anno(conn, '2025')
            print_prescrizioni_anno(prescrizioni_2025, '2025')

        elif command == 'farmaco-pazienti':
            pazienti_per_farmaco = query_pazienti_per_farmaco(conn)
            print_pazienti_per_farmaco(pazienti_per_farmaco)

        elif command == 'tutto':
            run_all_reports(conn)

        else:
            print(f"Comando sconosciuto: {command}")
            print_help()


if __name__ == '__main__':
    main()

