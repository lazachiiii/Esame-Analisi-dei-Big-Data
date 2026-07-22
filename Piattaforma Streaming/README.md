# Piattaforma Streaming — Catalogo Film, Serie TV e Documentari (Elasticsearch)

Terza traccia del progetto d'esame a scelta libera nell'ambito dei database NoSQL. 
Modella un catalogo di contenuti in stile piattaforma streaming come indice di documenti in Elasticsearch, sfruttando la ricerca full-text, i filtri strutturati e le aggregazioni statistiche,
tre capacità che lo distinguono nettamente da un database relazionale.

## Il dominio

Il catalogo raccoglie trenta titoli reali (dieci film, dieci serie TV e dieci
documentari), ciascuno rappresentato come un documento JSON con campi come titolo,
tipo di contenuto, anno, uno o più generi, regista, trama, valutazione e, a seconda
del tipo, durata in minuti oppure numero di stagioni. Le trame sono sinossi
originali scritte a scopo didattico, non copiate da fonti esterne.

Un aspetto importante di questo modello è che, a differenza di una tabella
relazionale, documenti diversi nello stesso indice possono avere campi
diversi tra loro: i film e i documentari singoli hanno una durata in minuti, mentre
le serie TV e i documentari seriali hanno invece un numero di stagioni, senza che
questo richieda tabelle separate o colonne sempre vuote.

## Avviare Elasticsearch
Il progetto usa Elasticsearch 8.15.0, avviato localmente tramite Docker. Con
Docker Desktop attivo, basta lanciare:

bashdocker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  docker.elastic.co/elasticsearch/elasticsearch:8.15.0

Questo comando scarica l'immagine ufficiale (solo la prima volta) e avvia un nodo
singolo, con la sicurezza disattivata per semplicità, trattandosi di un ambiente
locale a scopo didattico. Si può verificare che il servizio sia attivo con:

bashcurl http://localhost:9200

che deve restituire un JSON con il nome del cluster e la versione installata.

Installare le dipendenze Python

bashpython3 -m pip install "elasticsearch==8.15.0"

È importante che la versione del client Python corrisponda a quella del server:
versioni troppo distanti (per esempio client 9.x contro server 8.x) possono
restituire errori generici e poco chiari in fase di connessione.

## Query disponibili

Lo script catalogo_es.py (che ricrea e popola l'indice a ogni esecuzione) espone
tre comandi da riga di comando, ciascuno pensato per mostrare una capacità diversa
di Elasticsearch.

cerca-trama <termine> — ricerca full-text sul campo trama (di tipo text,
quindi tokenizzato), con risultati ordinati per rilevanza (_score).

   bashpython3 catalogo_es.py cerca-trama sogni

Limite noto: l'analyzer standard non fa stemming in italiano, quindi "sogno"
(singolare) non trova "Inception" pur avendo "sogni" nella trama — servirebbe un
analyzer italiano dedicato per unificare le forme flesse della stessa parola.

filtro-genere <genere> <voto_minimo> — filtro strutturato che combina un
match esatto su genere (term, campo keyword) con una soglia minima di
valutazione (range), risultati ordinati per voto decrescente.

   bashpython3 catalogo_es.py filtro-genere Horror 8.0

media-voti-genere — aggregazione statistica (terms + avg) che calcola
numero di titoli e valutazione media per ciascun genere presente nel catalogo.

   bashpython3 catalogo_es.py media-voti-genere
