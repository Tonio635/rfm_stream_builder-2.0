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

**Python  3.10**

Packages:

* [Matplotlib 3.6.1](https://matplotlib.org/)
* [Numpy 1.23.4](https://www.numpy.org/)
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


