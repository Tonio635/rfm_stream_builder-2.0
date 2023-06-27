# RFM Stream Builder
Repository per il progetto di tesi: 

* "Sintesi di un approccio di churn prediction basato su Online Learning", A.A. 2021/2022.
* "Sintesi di un approccio di churn prediction basato su Stream Learning", A.A. 2021/2022.
* "Sintesi di un approccio di machine learning per la predizione della fedeltà dei clienti in un sistema di commercio al dettaglio", A.A. 2022/2023.

I datasets utilizzati sono reperibili ai seguenti link:
* https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
* https://archive.ics.uci.edu/ml/datasets/Online+Retail+II#

## Struttura del repository

    
        .
        ├── src                                         # contiene il codice sorgente
        │    ├── classification                         # contiene codice reltivo alla parte di sperimentazione
        │    │    ├── online                            # contiene codice relativo al package degli algoritmi di Online Learning
        │    │    │    ├ AdaptiveRandomForestClassifier.py
        │    │    │    ├ ClassifierEnum.py
        │    │    │    ├ HoeffdingAdaptiveTreeClassifier.py
        │    │    │    ├ HoeffdingTreeClassifier.py
        │    │    │    ├ LogisticRegression.py
        │    │    │    ├ Main.py
        │    │    │    ├ OnlineClassifierInterface.py
        │    │    │    ├ OnlineLearner.py
        │    │    │    └ Perceptron.py
        │    │    ├── offline                          # contiene codice relativo al package degli algoritmi tradizionali di Machine Learning
        │    │    │    ├ Main.py
        │    │    │    ├ OfflineClassifierEnum.py
        │    │    │    ├ OfflineClassifierInterface.py
        │    │    │    ├ OfflineDecisionTree.py
        │    │    │    ├ OfflineLearner.py
        │    │    │    ├ OfflineLogisticRegression.py
        │    │    │    ├ OfflinePerceptron.py
        │    │    │    ├ OfflineRandomForest.py    
        |    |    |    └ OfflineXGBoost.py   
        │    │    └── PickleLoader.py  
        │    └── streamBuilder                        # contiene codice relativo al modulo di ingegnerizzazione dati
        │         ├ CategoryMapping.py
        │         ├ CustomerWindow.py
        │         ├ DataWindow.py
        │         ├ Day.py
        │         ├ DBConnector.py
        │         ├ Example.py
        │         ├ ExampleDictionary.py
        │         ├ ExampleSequence.py
        │         ├ Receipt.py
        │         ├ ReceiptLine.py
        │         ├ Rfm.py
        │         ├ RfmR.py
        │         └ StreamBuilder.py 
        ├── resources                                 # contiene le risorse (datasets, diagrammi e risultati sperimentazioni)
        │    ├ config.json
        │    ├── Datasets
        │    │    ├── brazilian_churn_retail_db
        │    │    │    ├── Datasets Originali
        │    │    │    │    ├ olist_customers_dataset.csv
        │    │    │    │    ├ olist_order_items_dataset.csv
        │    │    │    │    ├ olist_orders_dataset.csv
        │    │    │    │    └ olist_products_dataset.csv
        │    │    │    ├ Delivery_Addresses.csv
        │    │    │    ├ Members.csv
        │    │    │    ├ Products.csv
        │    │    │    ├ Receipt_Lines.csv
        │    │    │    ├ Receipts.csv
        │    │    │    └ Receipts_nuovodb.csv
        │    │    ├── churn_retail_db
        │    │    │    ├── Datasets Originali
        │    │    │    │    └ online_retail_II.xlsx
        │    │    │    ├ Delivery_Addresses.csv
        │    │    │    ├ Members.csv
        │    │    │    ├ Products.csv
        │    │    │    ├ Receipt_Lines.csv
        │    │    │    └ Receipts.csv
        │    ├── Diagrams
        │    │    ├ new classification Class Diagram.png
        │    │    ├ new classification Class Diagram.xml
        │    │    ├ new ER Diagram.png
        │    │    ├ new ER Diagram.xml
        │    │    ├ new Logic Model.png
        │    │    ├ new Logic Model.xml
        │    │    ├ new streamBuilder Class Diagram.png
        │    │    ├ new streamBuilder Class Diagram.xml
        │    │    ├ old classification Class Diagram.png
        │    │    ├ old DB Architecture Diagram.pdf
        │    │    └ old streamBuilder Class Diagram.png
        │    ├── Results
        │    │    ├ Bilanciamento_Classi_brazilian_churn_retail_db_vertwo (Brunetta).xlsx
        │    │    ├ Bilanciamento_Classi_churn_retail_db (Luce).xlsx
        │    │    ├ Sommario sperimentazioni.xlsx
        │    │    ├ Valutazioni Brazilian 120 120 3.xlsx
        │    │    └ Valutazioni UCI 60 60 3.xlsx
        │    └── SQL Scripts 
        │         ├ brazilian_churn_retail_db.sql
        │         ├ brazilian_churn_retail_db_vertwo.sql
        │         ├ brazilian_churn_retail_db_verthree.sql
        │         ├ brazilian_churn_retail_db_verfour.sql
        │         ├ churn_retail_db.sql
        │         ├ churn_retail_db_vertwo.sql
        │         ├ test_db.sql
        │         └ test_tesi.sql
        ├── output                                    # contiene i mini-batch serializzati come output del modulo di ingegnerizzazione dati
        ├── serialized_models                         # contiente i modelli che l'utente decide di salvare a seguito della visualizzazione dei risultati
        ├── requirements.txt                          # file contenente la lista delle dipendenze necessarie
        └── README.md                                 # file contente le informazioni necessarie all'installazione e all'utilizzo

## Installazione

    pip install -r /path/to/requirements.txt

**Python  3.11**

Packages:

* [Matplotlib 3.7.1](https://matplotlib.org/)
* [Numpy 1.25.0](https://www.numpy.org/)
* [Scikit-learn 1.1.3](https://scikit-learn.org/stable/)
* [Pandas 1.5.1](https://pandas.pydata.org/)
* [Mysql-connector 8.0.31](https://pypi.org/project/mysql-connector-python/)
* [Seaborn 0.12.1](https://seaborn.pydata.org/)
* [River 0.14.0](https://riverml.xyz/0.14.0/)





## Generazione stream di esempi

La serializzazione degli esempi etichettati avviene all'interno della cartella output e sono denominati con la data del giorno in cui sono stati etichettati.

**Prima di eseguire il programma, tuttavia, è opportuno svuotare la cartella output dai risultati di eventuali precedenti esecuzioni.**

Per eseguire il software è necessario utilizzare il terminale posizionandosi nella cartella 'src/streamBuilder' del progetto e digitare:

``python StreamBuilder.py`` seguito dai parametri di input:

    -h, --help: Mostra la lista dei comandi 
    --host: Il nome del server o l'indirizzo IP su cui è in esecuzione MySQL. Se si esegue su localhost è possibile utilizzare localhost o IP 127.0.0.0.
    --user: Il nome utente che si utilizza per lavorare con MySQL. Il nome utente predefinito per il database MySQL è root.
    --password: La password viene fornita dall'utente al momento dell'installazione del server MySQL.
    --database: Il nome del database a cui si desidera connettersi ed eseguire le operazioni.
    --churnDim: Dimensione del churn, di tipo int.
    --periodDim: Dimensione del periodo, di tipo int.
    --periods: Numero di periodi, di tipo int.
    -–level: Livello della gerarchia delle categorie di prodotti da tenere in considerazione nella generazione degli esempi, di tipo int.
    -–traditionalRFM, -–aggregates, –-productRFM, --productAggregates: Valori binari per stabilire se considerare o meno queste feature (1 o 0).
    --start: Data di partenza in formato: AAAA-MM-DD, OPZIONALE: di default la prima del db.
    --end: Data di fine in formato: AAAA-MM-DD, OPZIONALE: di default l'ultima del db.

Esempio di input:

    python StreamBuilder.py --password "la_tua_password" --database "nome_db" --churnDim 60 --periodDim 60 --periods 3 --level 2 --traditionalRFM 1 --aggregates 1 --productRFM 1 --productAggregates 1 --start 2022-01-01 --end 2022-02-07

È possibile impostare i parametri di input anche tramite il file di configurazione config.json presente nella cartella resources. Nella cartella resources è possibile trovare il diagramma delle classi e degli script SQL per creare dei database. Di questi ultimi:
* Quattro versioni del database brazilian: La prima versione, denominata con brazilian_churn_retail_db, è quella originale e senza riduzioni, mentre la seconda versione è la quella ridotta. La terza e la quarta versione sono le uniche compatibili completamente con la nuova versione del progetto e contengono rispettivamente 3 e 4 livelli di gerarchia dei prodotti;
* Due versioni del database UCI: La prima versione, chiamata churn_retail_db, è quella originale, la seconda è quella che include le categorie di prodotti con 3 livelli di gerarchia. Solo la seconda è pienamente compatibile con questa nuova versione;
* Due versioni di test: Una è chiamata test_tesi e riprende l'esempio illustrato nel capitolo 4. L'altra versione, chiamata test_db, è un altro database di test non compatibile con le novità introdotte.

I database usati per le sperimentazioni sono **brazilian_churn_retail_db_verfour** e **churn_retail_db_vertwo**.
## Addestramento e Classificazione

Dopo aver serializzato gli esempi nella cartella output, i file verranno caricati dal programma di addestramento e classificazione.

Per eseguire il software è necessario utilizzare il terminale posizionandosi nella cartella 'rfm_stream_builder' del progetto e digitare:

* per algoritmi di apprendimento online:

      python -m src.classification.online.Main
* oppure per algoritmi di apprendimento offline:
      
      python -m src.classification.offline.Main

seguito dai parametri di input:

     --start: Data di partenza in formato: AAAA-MM-DD, OPZIONALE: di default la prima della cartella.
     --end: Data di fine in formato: AAAA-MM-DD, OPZIONALE: di default l'ultima della cartella.
     --serialized: Parametro per caricare un modello precedentemente serializzato.
     --training_dim: Valore intero da 1 a 99 per selezionare, in percentuale, la dimensione del training set. Per selezionare un anno esatto di training set inserire 0. Il valore di default è 70.

**Se vengono inseriti i parametri opzionali di start ed end è opportuno inserirli entrambi affinchè l'algoritmo funzioni correttamente.**

Si dovrà successivamente scegliere nella lista presente, il numero dell'algoritmo da testare.

Al termine del processo si potrà scegliere se serializzare il modello appena addestrato. Inoltre è possibile salvare
il nome del modello con uno inserito da input.

Il nostro programma presenta anche la funzione di caricamento del modello serializzato: basta specificare l'argomento:

    --serialized "nome_file"

## Categorie Brazilian
Per il dataset Brazilian esistono 4 livelli nella gerarchia:
* **Livello 1**: La radice. Racchiude tutte quante le categorie e, selezionandolo, ogni prodotto sarà considerato di un'unica categoria;
* **Livello 2**: 15 categorie che si occupano di raggruppare le categorie di livello 3, al fine di ridurle;
* **Livello 3**: 74 categorie originarie del dataset che raggruppano tutti quanti i prodotti;
* **Livello 4**: I prodotti stessi. Selezionando questo livello non si prenderanno più in considerazione le categorie ma direttamente i singoli prodotti. Risulteranno quindi 33041 RFM dei prodotti e aggregati dei prodotti.

Di seguito sono mostrate le cateogire di livello 2 con tutte le categorie di livello 3 che esse racchiudono:

* **musica_e_arte**: *instrumentos_musicais, artes, audio, musica, cds_dvds_musicais;*
* **svago**: *artes, cool_stuff, brinquedos, fashion_calcados, consoles_games, livros_interesse_geral, fashion_underwear_e_moda_praia, livros_tecnicos, market_place, audio, musica, livros_importados, dvds_blu_ray,artes_e_artesanato, pc_gamer, cine_foto, flores, cds_dvds_musicais;*
* **bambini**: *bebes, brinquedos, fraldas_higiene;*
* **casa_e_giardino**: *utilidades_domesticas, moveis_decoracao, eletrodomesticos, cama_mesa_banho, ferramentas_jardim, climatizacao, eletrodomesticos_2, la_cuisine, construcao_ferramentas_jardim, casa_conforto,portateis_casa_forno_e_cafe, moveis_quarto, casa_conforto_2, portateis_cozinha_e_preparadores_de_alimentos, moveis_colchao_e_estofado;*
* **costruzione**: *construcao_ferramentas_seguranca, casa_construcao, construcao_ferramentas_construcao, construcao_ferramentas_ferramentas, construcao_ferramentas_iluminacao;*
* **computer_ed_elettronica**: *eletrodomesticos, informatica_acessorios, eletronicos, pcs, climatizacao, consoles_games, telefonia_fixa, eletrodomesticos_2, tablets_impressao_imagem, pc_gamer;*
* **prodotti_di_bellezza**: *perfumaria, beleza_saude;*
* **abbigliamento**: *malas_acessorios, fashion_calcados, fashion_bolsas_e_acessorios, fashion_underwear_e_moda_praia,fashion_roupa_masculina, fashion_roupa_feminina, fashion_esporte, fashion_roupa_infanto_juvenil;*
* **arredamento**: *moveis_decoracao, cama_mesa_banho, moveis_escritorio, moveis_sala, moveis_cozinha_area_de_servico_jantar_e_jardim, la_cuisine, portateis_casa_forno_e_cafe, moveis_quarto, portateis_cozinha_e_preparadores_de_alimentos, moveis_colchao_e_estofado;*
* **automotive**: *automotivo;*
* **lavoro**: *moveis_escritorio, papelaria, agro_industria_e_comercio, construcao_ferramentas_ferramentas, industria_comercio_e_negocios, livros_tecnicos, market_place, livros_importados, dvds_blu_ray;*
* **animali**: *pet_shop;*
* **sicurezza**: *sinalizacao_e_seguranca, seguros_e_servicos;*
* **alimenti**: *portateis_cozinha_e_preparadores_de_alimento, alimentos, alimentos_bebidas, bebidas;*
* **eventi_speciali**: *perfumaria, brinquedos, relogios_presentes, consoles_games, artigos_de_festas, audio, musica, artigos_de_natal, flores, cds_dvds_musicais.*

Si può notare che le categorie di livello 3 sono in portoghese. Questo perché era presente già inizialmente una categorizzazione preliminare dei prodotti, che in questo lavoro è stata riprogettata e riorganizzata. 
È anche da notare che ogni prodotto può essere presente in più categorie e che quindi non esiste nessun vincolo che lega un prodotto ad una ed una sola categoria. La stessa cosa vale per le varie categorie verso categorie di un livello superiore. 
## Categorie UCI
Per il dataset UCI esistono 3 livelli nella gerarchia:

* **Livello 1**: La radice. Racchiude tutte quante le categorie e, selezionandolo, ogni prodotto sarà considerato di un'unica categoria;
* **Livello 2**: 16 categorie che raggruppano tutti quanti i prodotti;
* **Livello 3**: I prodotti stessi. Selezionando questo livello non si prenderanno più in considerazione le categorie ma direttamente i singoli prodotti. Risulteranno quindi 4620 RFM dei prodotti e aggregati dei prodotti.

Le categorie di livello 2 solo le seguenti: *HOUSE_AND_GARDEN, ENTERTAINMENT, STATIONERY, PET, UTILITIES, SET, VINTAGE, CLOTHING, KITCHEN, KIDS, ELECTRONIC, PHOTO_AND_VIDEOS, ART_AND_MUSIC, SPECIAL_EVENTS, HYGIENE_AND_BEAUTY_PRODUCTS, FOOD_AND_DRINK.*

In questo caso, inizialmente, non era presente una categorizzazione, quindi è stato necessario crearla da zero studiando tutti i prodotti del dataset. 
Anche in questo caso ogni prodotto può essere presente in più categorie e senza nessun vincolo che lo leghi ad una ed una sola categoria.