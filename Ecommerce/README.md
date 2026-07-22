# Struttura del grafo

**Nodi**
- `Cliente`
- `Prodotto`
- `Categoria`

**Relazioni**
- `VISUALIZZA` — un cliente ha visualizzato un prodotto
- `AGGIUNGE_AL_CARRELLO` — un cliente ha aggiunto un prodotto al carrello
- `ACQUISTA` — un cliente ha acquistato un prodotto
- `RECENSISCE` (proprietà `punteggio`) — un cliente ha recensito un prodotto
- `APPARTIENE_A` — un prodotto appartiene a una categoria
- `SIMILE` / `COMPATIBILE` — relazioni prodotto-prodotto
- `ACQUISTATO_INSIEME` — due prodotti acquistati nello stesso ordine

## File
La cartella contiene due file principali. `esame_1.py` è lo script Python che si
collega al database Neo4j attraverso il driver ufficiale `neo4j` ed esegue le due
query di analisi descritte più sotto. `ecommerce.dump` è invece il dump del
database Neo4j, generato con il comando `neo4j-admin database dump`: contiene
tutti i nodi e le relazioni del grafo e va importato in una nuova istanza Neo4j
per ricreare i dati prima di poter eseguire lo script.

## Come eseguire il progetto

### 1. Importare il database
1. Rinomina il file, se necessario, in `ecommerce.dump`
2. Apri **Neo4j Desktop** → crea una nuova istanza
3. Nella sezione **"Load from .dump, .backup or .tar"** del form di creazione, seleziona `ecommerce.dump`
4. Avvia l'istanza creata

### 2. Configurare le credenziali
Lo script legge URI, utente, password e nome del database da variabili d'ambiente,
con valori di default per un rapido test in locale:

```bash
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="<la tua password>"
export NEO4J_DATABASE="neo4j"
```

### 3. Installare le dipendenze ed eseguire
```bash
pip install neo4j
python esame_1.py
```

## Query implementate

**Query 1 — Prodotti consigliati ai clienti**
Per ogni cliente, individua i prodotti non ancora acquistati e calcola un indice
di raccomandazione sommando tre segnali: visualizzazione (+1), presenza nel
carrello (+2), recensione positiva (punteggio ≥ 4) da parte di un altro cliente
che condivide almeno un acquisto (+3).

**Query 2 — Categorie connesse per prodotto**
Per ogni prodotto, analizza i prodotti correlati (via `SIMILE` o `COMPATIBILE`)
e conta a quali categorie appartengono, restituendo una "forza di connessione"
per categoria.

> Nota: un prodotto privo di relazioni `SIMILE`/`COMPATIBILE` con altri prodotti
> non compare nei risultati di questa query, anche se appartiene lui stesso a
> una categoria — è un limite noto della query così com'è scritta.
