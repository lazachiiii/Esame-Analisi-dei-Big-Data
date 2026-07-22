import os
import sys
from elasticsearch import Elasticsearch, helpers

from dati_catalogo import CATALOGO

ES_URL = os.getenv("ES_URL", "http://localhost:9200")
NOME_INDICE = "catalogo_streaming"

def get_client():
    return Elasticsearch(ES_URL)

def crea_indice(client):
    """Elimina l'indice se esiste già e lo ricrea con un mapping esplicito."""
    if client.indices.exists(index=NOME_INDICE):
        client.indices.delete(index=NOME_INDICE)

    mapping = {
        "mappings": {
            "properties": {
                "titolo": {"type": "text"},
                "tipo": {"type": "keyword"},
                "anno": {"type": "integer"},
                "genere": {"type": "keyword"},
                "regista": {"type": "text"},
                "trama": {"type": "text"},
                "valutazione": {"type": "float"},
                "durata_minuti": {"type": "integer"},
                "numero_stagioni": {"type": "integer"},
                "piattaforma": {"type": "keyword"},
            }
        }
    }
    client.indices.create(index=NOME_INDICE, body=mapping)


def carica_dati(client):
    """Carica tutti i documenti del catalogo tramite l'API bulk."""
    azioni = [
        {"_index": NOME_INDICE, "_source": documento}
        for documento in CATALOGO
    ]
    helpers.bulk(client, azioni)
    # Rende subito ricercabili i documenti appena inseriti (utile in demo)
    client.indices.refresh(index=NOME_INDICE)


def inizializza():
    client = get_client()
    crea_indice(client)
    carica_dati(client)
    print(f"Indice '{NOME_INDICE}' creato e popolato con {len(CATALOGO)} titoli.\n")

def cerca_trama(client, termine):
    query = {
        "query": {
            "match": {
                "trama": termine
            }
        }
    }
    risposta = client.search(index=NOME_INDICE, body=query)
    risultati = risposta["hits"]["hits"]

    print(f"Titoli con '{termine}' nella trama:\n")
    if not risultati:
        print("Nessun risultato trovato.\n")
        return

    for hit in risultati:
        doc = hit["_source"]
        print(f"- {doc['titolo']} ({doc['anno']}) | Score: {hit['_score']:.2f} | {doc['trama'][:80]}...")
    print()

def filtro_genere(client, genere, voto_minimo):
    query = {
        "query": {
            "bool": {
                "filter": [
                    {"term": {"genere": genere}},
                    {"range": {"valutazione": {"gte": float(voto_minimo)}}}
                ]
            }
        },
        "sort": [{"valutazione": {"order": "desc"}}]
    }
    risposta = client.search(index=NOME_INDICE, body=query)
    risultati = risposta["hits"]["hits"]

    print(f"Titoli di genere '{genere}' con valutazione >= {voto_minimo}:\n")
    if not risultati:
        print("Nessun risultato trovato.\n")
        return

    for hit in risultati:
        doc = hit["_source"]
        print(f"- {doc['titolo']} ({doc['anno']}) | Tipo: {doc['tipo']} | Voto: {doc['valutazione']}")
    print()

def media_voti_genere(client):
    query = {
        "size": 0,
        "aggs": {
            "per_genere": {
                "terms": {"field": "genere", "size": 20},
                "aggs": {
                    "media_voto": {"avg": {"field": "valutazione"}}
                }
            }
        }
    }
    risposta = client.search(index=NOME_INDICE, body=query)
    buckets = risposta["aggregations"]["per_genere"]["buckets"]

    print("Media valutazione e numero titoli per genere:\n")
    print(f"{'GENERE':<15} | {'N. TITOLI':<10} | {'MEDIA VOTO'}")
    print("-" * 45)
    for bucket in buckets:
        genere = bucket["key"]
        conteggio = bucket["doc_count"]
        media = bucket["media_voto"]["value"]
        print(f"{genere:<15} | {conteggio:<10} | {media:.2f}")
    print()

COMANDI = {
    "cerca-trama": "cerca-trama <termine>",
    "filtro-genere": "filtro-genere <genere> <voto_minimo>",
    "media-voti-genere": "media-voti-genere",
}


def print_help():
    print("Comandi disponibili:")
    for uso in COMANDI.values():
        print(f"  python3 catalogo_es.py {uso}")


def main():
    inizializza()

    args = sys.argv[1:]
    client = get_client()

    if not args or args[0] not in COMANDI:
        comando = args[0] if args else None
        if comando is None:
            print("Errore: nessun comando specificato.\n")
        else:
            print(f"Errore: comando sconosciuto '{comando}'.\n")
        print_help()
        return

    command = args[0]

    if command == "cerca-trama":
        if len(args) != 2:
            print(f"Uso: python3 catalogo_es.py {COMANDI[command]}\n")
            return
        cerca_trama(client, args[1])

    elif command == "filtro-genere":
        if len(args) != 3:
            print(f"Uso: python3 catalogo_es.py {COMANDI[command]}\n")
            return
        filtro_genere(client, args[1], args[2])

    elif command == "media-voti-genere":
        media_voti_genere(client)


if __name__ == "__main__":
    main()