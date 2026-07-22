import os
from neo4j import GraphDatabase

# 1. CONFIGURAZIONE DELLE CREDENZIALI E DEI PARAMETRI
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "esameesame2"
NOME_DB = "neo4j"


TARGET_UTENTE = "USR024"
TARGET_PRODOTTO = "PROD055"


# 2. DEFINIZIONE DELLE QUERY
QUERY_1_PRODOTTI = """
MATCH (c:Cliente {id: $id_utente})-[:ACQUISTATO]->(p_acquistato:Prodotto)
WITH c, collect(elementId(p_acquistato)) AS prodotti_acquistati

MATCH (c)-[:ACQUISTATO|AGGIUNTO_AL_CARRELLO|VISUALIZZATO]->(p_interazione:Prodotto)
WITH c, prodotti_acquistati, collect(elementId(p_interazione)) AS prodotti_interazione

MATCH (p_comune:Prodotto)<-[:ACQUISTATO|AGGIUNTO_AL_CARRELLO|VISUALIZZATO]-(simile:Cliente)
WHERE simile <> c AND elementId(p_comune) IN prodotti_interazione

WITH c, prodotti_acquistati, simile, count(p_comune) AS score_similarita
ORDER BY score_similarita DESC
LIMIT 10

MATCH (simile)-[:ACQUISTATO|AGGIUNTO_AL_CARRELLO|VISUALIZZATO]->(raccomandato:Prodotto)
WHERE NOT elementId(raccomandato) IN prodotti_acquistati

WITH raccomandato, sum(score_similarita) AS raccomandazione_score
ORDER BY raccomandazione_score DESC
LIMIT 5

RETURN raccomandato.nome AS prodotti_consigliati
"""

QUERY_2_CATEGORIE = """
// 1. QUERY 2 Definisci il prodotto di partenza dal quale generare le raccomandazioni
MATCH (p_inizio:Prodotto {codice: $codice_prodotto})

// 2. Trova i clienti che hanno interagito con questo prodotto (dando pesi diversi alle azioni)
MATCH (c:Cliente)-[interazione]->(p_inizio)
WITH p_inizio, c, 
     CASE type(interazione)
       WHEN 'ACQUISTATO' THEN 3
       WHEN 'AGGIUNTO_AL_CARRELLO' THEN 2
       WHEN 'VISUALIZZATO' THEN 1
       ELSE 0 
     END AS peso_interazione

// 3. Scopri cos'altro ha catturato l'interesse di questi clienti (escludendo il prodotto di partenza)
MATCH (c)-[altra_interazione]->(p_consigliato:Prodotto)-[:APPARTIENE_A]->(cat:Categoria)
WHERE p_consigliato <> p_inizio
WITH cat, p_consigliato, peso_interazione,
     CASE type(altra_interazione)
       WHEN 'ACQUISTATO' THEN 3
       WHEN 'AGGIUNTO_AL_CARRELLO' THEN 2
       WHEN 'VISUALIZZATO' THEN 1
       ELSE 0 
     END AS peso_raccomandazione

// 4. Calcola il punteggio di rilevanza complessivo per ogni Categoria
WITH cat, sum(peso_interazione * peso_raccomandazione) AS rilevanza
ORDER BY rilevanza DESC

// 5. Restituisce il verdetto finale
RETURN cat.nome AS categoria_connessa, rilevanza
"""


def esegui_analisi():
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

    try:
        with driver.session(database=NOME_DB) as session:
            # ---------------------------------------------------------
            # SFIDA 1: PRODOTTI RACCOMANDATI
            # ---------------------------------------------------------
            print("=" * 60)
            print(f"QUERY 1: PRODOTTI RACCOMANDATI PER L'UTENTE {TARGET_UTENTE}")
            print("=" * 60)

            risultato_1 = session.run(QUERY_1_PRODOTTI, id_utente=TARGET_UTENTE)
            record_1 = list(risultato_1)

            if not record_1:
                print(
                    f"Nessun prodotto consigliato trovato (controlla se l'utente {TARGET_UTENTE} ha interazioni o acquisti)."
                )
            else:
                for i, record in enumerate(record_1, 1):
                    print(f"{i}. {record['prodotti_consigliati']}")

            # ---------------------------------------------------------
            # SFIDA 2: CATEGORIE RILEVANTI
            # ---------------------------------------------------------
            print("\n" + "=" * 60)
            print(f"QUERY 2: CATEGORIE CONNESSE AL PRODOTTO {TARGET_PRODOTTO}")
            print("=" * 60)

            risultato_2 = session.run(
                QUERY_2_CATEGORIE, codice_prodotto=TARGET_PRODOTTO
            )
            record_2 = list(risultato_2)

            if not record_2:
                print(
                    f"Nessuna categoria consigliata trovata (controlla le interazioni sul prodotto {TARGET_PRODOTTO})."
                )
            else:
                print(f"{'CATEGORIA':<25} | {'PUNTEGGIO RILEVANZA':<20}")
                print("-" * 50)
                for record in record_2:
                    # Ho aggiornato la chiave del dizionario usando 'categoria_connessa'
                    print(
                        f"{record['categoria_connessa']:<25} | {record['rilevanza']:<20}"
                    )

    except Exception as e:
        print(f"\n[ERRORE DI CONNESSIONE O QUERY]: {e}")
    finally:
        driver.close()


if __name__ == "__main__":
    esegui_analisi()
