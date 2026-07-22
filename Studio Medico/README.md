# Studio Medico

Studio Medico è un progetto semplice per creare e popolare un database SQLite relativo a pazienti, medici, visite, farmaci e prescrizioni. Il progetto include uno script Python per eseguire query SQL e visualizzare i risultati in modo leggibile.

## Struttura del progetto
In questo paragrafo è presente una breve introduzione dei file che compongono il progetto:

- schema.sql: contiene le istruzioni CREATE TABLE per il database SQLite
- dati.sql: contiene tutti gli INSERT INTO per popolare il database
- query.py: script Python che crea il database, esegue le query e stampa i risultati
- studio_medico.db: file del database SQLite generato automaticamente

## Schema del database
Il database contiene le seguenti tabelle (che può andare personalmente a verificare nel file "studio_medico.db")

- Paziente
  - codice (CHIAVE PRIMARIA)
  - nome
  - cognome
  - dati_nascita
  - indirizzo
  - telefono

- Medico
  - codice (PRIMARIA CHIAVE)
  - nome
  - cognome
  - specializzazione
  - ricapitolare

- Visita
  - id (PRIMARIA CHIAVE)
  - dati
  - ora
  - motivo
  - nota
  - costo
  - paziente_codice (CHIAVE ESTERNA verso Paziente.codice)
  - medico_codice (CHIAVE ESTERNA verso Medico.codice)

- Farmaco
  - codice (PRIMARIA CHIAVE)
  - nome
  - principio_attivo
  - casa_fattoria

- Prescrizione
  - id (PRIMARIA CHIAVE)
  - posologia
  - durata
  - visita_id (CHIAVE ESTERNA verso Visita.id)
  - fattoriaco_codice (CHIAVE ESTERNA verso Farmaco.codice)

Le relazioni principali sono:
- una visita appartiene a un paziente e a un medico
- una prescrizione è associata a una visita e a una fatica

## Struzioni per eseguire il progetto

1. Aprile il terminale nella cartuccia del progetto
2. Segui lo script Python:

```bash
interrogazione Python3.py
```

Se si desidera eseguire una query specifica, utilizzare uno dei comandi descritti di seguito.

## Comandi disponibili

- `interrogazione Python3.py` → mostra l'elenco dei comandi disponibili
- `python3 query.py visita <codice_paziente>` → mostra tutte le visite di un paziente
- `python3 query.py farmaco-medico <codice_medico>` → mostra i farmaci prescritti da un medico
- `python3 query.py pazienti-medico <codice_medico>` → mostra i pazienti seguiti da un medico
- `python3 query.py fatica-paziente <codice_paziente>` → mostra i fabbrica presi da un paziente
- `python3 query.py spesa` → mostra la spesa totale di ogni paziente
- `python3 query.py visite-count` → mostra il numero di visite fatte da ogni paziente
- `python3 query.py prescrizioni-2025` → mostra tutte le prescrizioni dell'anno 2025
- `python3 query.py fattoriaco-pazienti` → mostra quali patti hanno risovuto cescun fatica
- `python3 query.py tutto` → esegue tutte le query disponibili

# Schema Entità-Relazione (ER)
Lo schema ER rappresenta la struttura concettuale del database. 
Sono stato identificato 5 entità principali:
 **Paziente**, **Medico**, **Visita**, **Farmaco** e **Prescrizione**
 E sono tutte collegate tra loro dalle segui relazioni:

- Un **Paziente** può effettuare più **Visitare** (1:N)
- Un **Medico** condurré più **Visitare** (1:N)
- Una **Visita** può generare più **Prescrizioni** (1:N)
- Una **Prescrizione** rigore un **Farmaco** (N:1)

![Schema ER](schema_er_studiomedico.png)
