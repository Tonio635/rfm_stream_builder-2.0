# RFM Stream Builder
Repository per il progetto di tesi: 

* "Sintesi di un approccio di churn prediction basato su Online Learning", A.A. 2021/2022.
* "Sintesi di un approccio di churn prediction basato su Stream Learning", A.A. 2021/2022.

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
        │    │    │    └ OfflineRandomForest.py       
        │    │    └── PickleLoader.py  
        │    └── streamBuilder                        # contiene codice relativo al modulo di ingegnerizzazione dati
        │         ├ CustomerWindow.py
        │         ├ DataWindow.py
        │         ├ Day.py
        │         ├ DBConnector.py
        │         ├ Example.py
        │         ├ ExampleDictionary.py
        │         ├ ExampleSequence.py
        │         ├ Receipt.py
        │         ├ Rfm.py
        │         └ StreamBuilder.py 
        ├── resources                                 # contiene le risorse (datasets, diagrammi e risultati sperimentazioni)
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
        │    │    ├ classification Class Diagram.png
        │    │    ├ DB Architecture Diagram.pdf
        │    │    └ streamBuilder Class Diagram.png
        │    ├── Results
        │    │    ├ Bilanciamento_Classi_brazilian_churn_retail_db_vertwo (Brunetta).xlsx       
        │    │    ├ Bilanciamento_Classi_churn_retail_db (Luce).xlsx
        │    │    └ Sommario sperimentazioni.xlsx
        │    └── SQL Scripts 
        │         ├ brazilian_churn_retail_db.sql
        │         ├ brazilian_churn_retail_db_vertwo.sql
        │         ├ churn_retail_db.sql
        │         └ test_db.sql
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

Per eseguire il software è necessario utilizzare il terminale posizionandosi nella cartella 'src/streamBuilder' del progetto e 
digitare:

``python StreamBuilder.py`` seguito dai parametri di input:

    -h, --help &emsp; mostra la lista dei comandi 
    --host HOST &emsp; Il nome del server o l'indirizzo IP su cui è in esecuzione MySQL. Se si esegue su localhost è possibile utilizzare localhost o IP 127.0.0.0.
    --user USER &emsp; Il nome utente che si utilizza per lavorare con MySQL. Il nome utente predefinito per il database MySQL è root.
    --password PASSWORD &emsp; La password viene fornita dall'utente al momento dell'installazione del server MySQL.
    --database DATABASE &emsp; Il nome del database a cui si desidera connettersi ed eseguire le operazioni.
    --churnDim CHURNDIM &emsp; Dimensione del churn, di tipo int.
    --periodDim PERIODDIM &emsp; Dimensione del periodo, di tipo int.
    --periods PERIODS &emsp; Numero di periodi, di tipo int.
    --start START &emsp; Data di partenza in formato: AAAA-MM-DD, OPZIONALE: di default la prima del db.
    --end END &emsp; Data di fine in formato: AAAA-MM-DD, OPZIONALE: di default l'ultima del db.

Esempio di input:

    python StreamBuilder.py --password "la_tua_password" --database "nome_db" --churnDim 115 --periodDim 60 --periods 3 --start 2022-01-01 --end 2022-02-07

Nella cartella resources è possibile trovare il diagramma delle classi e lo scripts sql per creare un db di test.

## Addestramento e Classificazione

Dopo aver serializzato gli esempi nella cartella output, i file verranno caricati dal programma di addestramento e classificazione.

Per eseguire il software è necessario utilizzare il terminale posizionandosi nella cartella 'rfm_stream_builder' del progetto e digitare:

* per algoritmi di apprendimento online:

      python -m src.classification.online.Main
* oppure per algoritmi di apprendimento offline:
      
      python -m src.classification.offline.Main

seguito dai parametri di input:

     --start START &emsp; Data di partenza in formato: AAAA-MM-DD, OPZIONALE: di default la prima della cartella.
     --end END &emsp; Data di fine in formato: AAAA-MM-DD, OPZIONALE: di default l'ultima della cartella.
     --serialized NAME &emsp; Parametro per caricare un modello precedentemente serializzato.

**Se vengono inseriti i parametri opzionali di start ed end è opportuno inserirli entrambi affinchè l'algoritmo funzioni correttamente.**

Si dovrà successivamente scegliere nella lista presente, il numero dell'algoritmo da testare.

Al termine del processo si potrà scegliere se serializzare il modello appena addestrato. Inoltre è possibile salvare
il nome del modello con uno inserito da input.

Il nostro programma presenta anche la funzione di caricamento del modello serializzato: basta specificare l'argomento:

    --serialized``"nome_file"


