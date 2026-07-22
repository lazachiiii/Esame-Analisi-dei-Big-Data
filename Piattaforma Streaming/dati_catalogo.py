from typing import Any
CATALOGO = [
    # ---------------------- FILM ----------------------
    {
        "titolo": "Alien",
        "tipo": "film",
        "anno": 1979,
        "genere": ["Fantascienza", "Horror"],
        "regista": "Ridley Scott",
        "trama": "L'equipaggio di una nave spaziale commerciale intercetta un misterioso segnale su un pianeta sconosciuto e si ritrova braccato da una creatura extraterrestre letale che si infiltra a bordo.",
        "valutazione": 8.5,
        "durata_minuti": 117,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Inception",
        "tipo": "film",
        "anno": 2010,
        "genere": ["Fantascienza", "Thriller"],
        "regista": "Christopher Nolan",
        "trama": "Un ladro specializzato nell'estrazione di segreti dai sogni altrui riceve l'incarico opposto: impiantare un'idea nella mente di un bersaglio, un'operazione considerata quasi impossibile.",
        "valutazione": 8.8,
        "durata_minuti": 148,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Carol",
        "tipo": "film",
        "anno": 2015,
        "genere": ["Drammatico", "Romantico"],
        "regista": "Todd Haynes",
        "trama": "Nella New York dei primi anni '50, una giovane commessa e una donna elegante e sposata sviluppano un legame sentimentale proibito, in un'epoca ostile a quel tipo di amore.",
        "valutazione": 7.2,
        "durata_minuti": 118,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "The Substance",
        "tipo": "film",
        "anno": 2024,
        "genere": ["Horror", "Fantascienza"],
        "regista": "Coralie Fargeat",
        "trama": "Un'ex star televisiva ormai scartata dall'industria dello spettacolo sperimenta una sostanza sperimentale che genera una versione più giovane di se stessa, con conseguenze corporee sempre più grottesche.",
        "valutazione": 7.3,
        "durata_minuti": 141,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Interstellar",
        "tipo": "film",
        "anno": 2014,
        "genere": ["Fantascienza", "Drammatico"],
        "regista": "Christopher Nolan",
        "trama": "Un gruppo di astronauti attraversa un varco spazio-temporale alla ricerca di un nuovo pianeta abitabile, mentre la Terra sta diventando inospitale per l'umanità.",
        "valutazione": 8.7,
        "durata_minuti": 169,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Obsession",
        "tipo": "film",
        "anno": 2026,
        "genere": ["Horror", "Thriller"],
        "regista": "Curry Barker",
        "trama": "Un timido commesso di un negozio di dischi spezza un oggetto magico per conquistare il cuore della sua migliore amica, scoprendo troppo tardi che ogni desiderio esaudito ha un prezzo oscuro.",
        "valutazione": 6.8,
        "durata_minuti": 108,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Tarzan",
        "tipo": "film",
        "anno": 1999,
        "genere": ["Animazione", "Avventura"],
        "regista": "Kevin Lima, Chris Buck",
        "trama": "Un neonato naufrago viene cresciuto da una famiglia di gorilla nella giungla africana, crescendo diviso tra la sua identità umana e il mondo animale che lo ha accolto come figlio.",
        "valutazione": 7.3,
        "durata_minuti": 88,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Il Signore degli Anelli: La Compagnia dell'Anello",
        "tipo": "film",
        "anno": 2001,
        "genere": ["Fantasy", "Avventura"],
        "regista": "Peter Jackson",
        "trama": "Uno hobbit riluttante eredita un anello dal potere devastante e deve intraprendere un lungo viaggio per distruggerlo, insieme a una compagnia di alleati provenienti da popoli diversi.",
        "valutazione": 8.9,
        "durata_minuti": 178,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "The Thing",
        "tipo": "film",
        "anno": 1982,
        "genere": ["Horror", "Fantascienza"],
        "regista": "John Carpenter",
        "trama": "In una base scientifica isolata in Antartide, un gruppo di ricercatori scopre un organismo alieno capace di imitare perfettamente qualsiasi essere vivente, scatenando paranoia e sospetto reciproco.",
        "valutazione": 8.2,
        "durata_minuti": 109,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Perfect Blue",
        "tipo": "film",
        "anno": 1997,
        "genere": ["Animazione", "Thriller"],
        "regista": "Satoshi Kon",
        "trama": "Un'ex idol pop giapponese abbandona la musica per diventare attrice, ma inizia a perdere il confine tra realtà e finzione mentre uno stalker ossessivo minaccia la sua nuova identità pubblica.",
        "valutazione": 8.0,
        "durata_minuti": 81,
        "piattaforma": "Piattaforma Streaming"
    },

    # ---------------------- SERIE TV ----------------------
    {
        "titolo": "Il Trono di Spade",
        "tipo": "serie",
        "anno": 2011,
        "genere": ["Fantasy", "Drammatico"],
        "regista": "David Benioff, D.B. Weiss",
        "trama": "Diverse casate nobiliari si contendono il controllo di un regno diviso, mentre a nord un'antica minaccia sovrannaturale torna a manifestarsi dopo secoli di quiete.",
        "valutazione": 9.2,
        "numero_stagioni": 8,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Black Mirror",
        "tipo": "serie",
        "anno": 2011,
        "genere": ["Fantascienza", "Thriller"],
        "regista": "Charlie Brooker",
        "trama": "Un'antologia di episodi indipendenti che esplora i lati oscuri e inquietanti della tecnologia moderna e le sue conseguenze impreviste sulla società e sui rapporti umani.",
        "valutazione": 8.7,
        "numero_stagioni": 7,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Grey's Anatomy",
        "tipo": "serie",
        "anno": 2005,
        "genere": ["Drammatico", "Medico"],
        "regista": "Shonda Rhimes",
        "trama": "Le vite personali e professionali di un gruppo di chirurghi di un ospedale di Seattle si intrecciano tra interventi complessi, dilemmi etici e relazioni sentimentali travagliate.",
        "valutazione": 7.6,
        "numero_stagioni": 21,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Widow's Bay",
        "tipo": "serie",
        "anno": 2026,
        "genere": ["Horror", "Commedia"],
        "regista": "Katie Dippold",
        "trama": "Il sindaco scettico di un'isola del New England cerca di rilanciare il turismo locale, ma deve fare i conti con gli abitanti superstiziosi e con una maledizione secolare che sembra tutt'altro che leggenda.",
        "valutazione": 8.6,
        "numero_stagioni": 1,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Breaking Bad",
        "tipo": "serie",
        "anno": 2008,
        "genere": ["Drammatico", "Crime"],
        "regista": "Vince Gilligan",
        "trama": "Un professore di chimica malato di cancro inizia a produrre metanfetamina per garantire un futuro economico alla propria famiglia, trasformandosi gradualmente in un boss criminale.",
        "valutazione": 9.5,
        "numero_stagioni": 5,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "L'amica geniale",
        "tipo": "serie",
        "anno": 2018,
        "genere": ["Drammatico"],
        "regista": "Saverio Costanzo",
        "trama": "L'amicizia complessa e duratura tra due donne cresciute in un quartiere popolare di Napoli, seguita dall'infanzia all'età adulta sullo sfondo di un'Italia in trasformazione.",
        "valutazione": 8.4,
        "numero_stagioni": 4,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "L'Attacco dei Giganti",
        "tipo": "serie",
        "anno": 2013,
        "genere": ["Animazione", "Azione"],
        "regista": "Tetsuro Araki",
        "trama": "L'umanità sopravvive rinchiusa dietro enormi mura per proteggersi da giganti antropofagi, finché un giovane non giura vendetta dopo che la sua città natale viene distrutta.",
        "valutazione": 9.0,
        "numero_stagioni": 4,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Dickinson",
        "tipo": "serie",
        "anno": 2019,
        "genere": ["Commedia", "Drammatico"],
        "regista": "Alena Smith",
        "trama": "Una rilettura anticonvenzionale e anacronistica della vita della poetessa Emily Dickinson nell'America del diciannovesimo secolo, tra desiderio artistico e ribellione alle convenzioni sociali.",
        "valutazione": 7.5,
        "numero_stagioni": 3,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Serial Experiments Lain",
        "tipo": "serie",
        "anno": 1998,
        "genere": ["Animazione", "Fantascienza"],
        "regista": "Ryutaro Nakamura",
        "trama": "Una ragazza introversa viene risucchiata in una rete di comunicazione globale dopo aver ricevuto un'email da una compagna di scuola morta, perdendo progressivamente il confine tra identità reale e virtuale.",
        "valutazione": 8.0,
        "numero_stagioni": 1,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Twin Peaks",
        "tipo": "serie",
        "anno": 1990,
        "genere": ["Mistero", "Drammatico"],
        "regista": "David Lynch, Mark Frost",
        "trama": "Un agente dell'FBI indaga sull'omicidio di una giovane reginetta di bellezza in una piccola cittadina di montagna, scoprendo segreti inquietanti nascosti dietro la sua facciata idilliaca.",
        "valutazione": 8.8,
        "numero_stagioni": 3,
        "piattaforma": "Piattaforma Streaming"
    },

    # ---------------------- DOCUMENTARI ----------------------
    {
        "titolo": "Cunk on Earth",
        "tipo": "documentario",
        "anno": 2022,
        "genere": ["Commedia", "Storico"],
        "regista": "Charlie Brooker",
        "trama": "Una conduttrice fittizia e volutamente impreparata ripercorre la storia della civiltà umana intervistando veri esperti accademici, generando un contrasto comico tra ignoranza e sapere.",
        "valutazione": 7.9,
        "numero_stagioni": 1,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Free Solo",
        "tipo": "documentario",
        "anno": 2018,
        "genere": ["Sport", "Avventura"],
        "regista": "Elizabeth Chai Vasarhelyi, Jimmy Chin",
        "trama": "Lo scalatore Alex Honnold si prepara ad affrontare la parete di El Capitan, nello Yosemite, senza corde né protezioni, in un'impresa che non ammette il minimo errore.",
        "valutazione": 8.1,
        "durata_minuti": 100,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "My Octopus Teacher",
        "tipo": "documentario",
        "anno": 2020,
        "genere": ["Natura"],
        "regista": "Pippa Ehrlich, James Reed",
        "trama": "Un documentarista sudafricano sviluppa nell'arco di un anno un legame straordinario con un polpo selvatico osservato quotidianamente in una foresta di kelp sottomarina.",
        "valutazione": 8.1,
        "durata_minuti": 85,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Won't You Be My Neighbor?",
        "tipo": "documentario",
        "anno": 2018,
        "genere": ["Biografico"],
        "regista": "Morgan Neville",
        "trama": "La vita e la filosofia gentile di Fred Rogers, storico conduttore di un programma televisivo educativo per bambini, e l'impatto duraturo del suo approccio empatico sulla società americana.",
        "valutazione": 8.4,
        "durata_minuti": 94,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "The Social Dilemma",
        "tipo": "documentario",
        "anno": 2020,
        "genere": ["Tecnologia"],
        "regista": "Jeff Orlowski",
        "trama": "Ex dipendenti delle più grandi aziende tecnologiche riflettono sui meccanismi nascosti degli algoritmi dei social media e sui rischi che questi comportano per la salute mentale collettiva.",
        "valutazione": 7.6,
        "durata_minuti": 94,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "13th",
        "tipo": "documentario",
        "anno": 2016,
        "genere": ["Storico", "Sociale"],
        "regista": "Ava DuVernay",
        "trama": "Un'analisi delle radici storiche e razziali del sistema carcerario statunitense, a partire dal tredicesimo emendamento della Costituzione americana fino alle politiche contemporanee.",
        "valutazione": 8.2,
        "durata_minuti": 100,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Cowspiracy",
        "tipo": "documentario",
        "anno": 2014,
        "genere": ["Ambientale"],
        "regista": "Kip Andersen, Keegan Kuhn",
        "trama": "Un'indagine sull'impatto ambientale dell'industria zootecnica su scala globale e sul motivo per cui questo tema resterebbe spesso ai margini del dibattito pubblico sul clima.",
        "valutazione": 7.7,
        "durata_minuti": 90,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Icarus",
        "tipo": "documentario",
        "anno": 2017,
        "genere": ["Sport", "Investigativo"],
        "regista": "Bryan Fogel",
        "trama": "Un'indagine amatoriale sul doping nel ciclismo si trasforma inaspettatamente nella scoperta di un sistema di doping di stato orchestrato dalla Russia ai massimi livelli sportivi.",
        "valutazione": 8.2,
        "durata_minuti": 121,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Planet Earth II",
        "tipo": "documentario",
        "anno": 2016,
        "genere": ["Natura"],
        "regista": "BBC Natural History Unit",
        "trama": "Una serie naturalistica che esplora la vita selvatica negli habitat più estremi del pianeta, dalle isole remote alle giungle, alle città, con riprese di altissima qualità tecnica.",
        "valutazione": 9.5,
        "numero_stagioni": 1,
        "piattaforma": "Piattaforma Streaming"
    },
    {
        "titolo": "Chef's Table",
        "tipo": "documentario",
        "anno": 2015,
        "genere": ["Cibo"],
        "regista": "David Gelb",
        "trama": "Una docu-serie che ritrae la vita e la filosofia culinaria di alcuni tra gli chef più influenti e innovativi al mondo, tra storie personali e ossessione per la perfezione in cucina.",
        "valutazione": 8.2,
        "numero_stagioni": 7,
        "piattaforma": "Piattaforma Streaming"
    },
]