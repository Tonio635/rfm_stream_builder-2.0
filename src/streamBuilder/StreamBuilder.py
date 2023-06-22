"""
// Name        : StreamBuilder.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe centrale del nostro progetto. Ha il compito di avviare il ciclo di estrazione dei dati dal db,
                 attraverso l'inizializzazione di una connessione usando la classe DBConnector. Viene successivamente
                 aperto il file csv su cui serializziamo gli esempi.
                 Il metodo privato generateStream genererà esempi opportunamente etichettati.
                 Infine la connessione al db e il file verranno chiuse.
"""
import json
import os
import mysql.connector.errors
import pandas as pd
from alive_progress import alive_bar
import datetime as dt
import pickle
from DBConnector import DBConnector
from DataWindow import DataWindow
from pathlib import Path
import argparse
import sys


class StreamBuilder:
    """
        Metodo costruttore:
            - host: Il nome del server o l'indirizzo IP su cui è in esecuzione MySQL. Se si esegue su localhost,
                    è possibile utilizzare localhost o il suo IP 127.0.0.0;
            - username: Il nome utente che si utilizza per lavorare con MySQL.
                        Il nome utente predefinito per il database MySQL è 'root';
            - password: La password viene fornita dall'utente al momento dell'installazione del server MySQL.
            - databaseName: Il nome del database a cui si desidera connettersi ed eseguire le operazioni.
            - churnDim: dimensione del churn, di tipo int;
            - periodDim: dimensione del periodo, di tipo int;
            - periods: numero di periodi, di tipo int;
            - level: livello di gerarchia delle categorie da utilizzare, di tipo int;
            - traditionalRFM: Valore binario per stabilire se considerare o meno queste feature (1 - Sì, 0 - No);
            - aggregates: Valore binario per stabilire se considerare o meno queste feature (1 - Sì, 0 - No);
            - productRFM: Valore binario per stabilire se considerare o meno queste feature (1 - Sì, 0 - No);
            - productAggregates: Valore binario per stabilire se considerare o meno queste feature (1 - Sì, 0 - No);
            - start: data di partenza, di default la prima del db;
            - end: data di fine, di default l'ultima del db;
            - outputFolder: percorso della cartella output dove vengono salvati i pickle;
        Inizializza la DataWindow e richiama il metodo privato generateStream().
    """

    def __init__(self, host: str, username: str, password: str, databaseName: str,
                 churnDim: int, periodDim: int, periods: int, level: int, traditionalRFM: int, aggregates: int,
                 productRFM: int, productAggregates: int, start: dt.date = None,
                 end: dt.date = None):
        current_dir = os.getcwd()
        dir_target = 'rfm_stream_builder'

        while os.path.basename(current_dir) != dir_target:
            current_dir = os.path.dirname(current_dir)
        
        self.__outputFolder = Path(current_dir + "/output")

        if None in [host, username, password, databaseName, churnDim, periodDim, periods, level, traditionalRFM, aggregates, productRFM, productAggregates]:
            raise ValueError("Argomenti non validi, assicurati di aver inserito tutti i parametri necessari!")
        if churnDim > periodDim*periods:
            raise ValueError("Il parametro churnDim non può essere maggiore di periodDim*periods. "
                             "Questo impatta negativamente la funzione splitPeriods di DataWindow!")
        try:
            self.__mydb = DBConnector(host, username, password, databaseName)
        except mysql.connector.errors.ProgrammingError:
            raise ValueError("Connessione al db fallita, controllare che i parametri siano corretti")

        allowed_values = [0, 1]
        if all(value not in allowed_values for value in [traditionalRFM, aggregates, productRFM, productAggregates]):
            raise ValueError("I valori delle features devono essere 0 o 1!")

        self.__window: DataWindow = DataWindow(periodDim, periods, churnDim, traditionalRFM, aggregates, productRFM, productAggregates)
        self.__generateStream(start, end, level)

    """
        Metodo per la generazione ed etichettatura di esempi. Infine serializziamo gli esempi in un pickle.
    """
    def __generateStream(self, start: str, end: str, level: int):
        currentDay = self.__mydb.extractFirstDay() if start is None else dt.date.fromisoformat(start)
        lastDay = self.__mydb.extractLastDay() if end is None else dt.date.fromisoformat(end)
        mapping = self.__mydb.extractProductHierarchy(level)
        categories = mapping.getDistinctCategories()
        with alive_bar((lastDay-currentDay).days, force_tty=True) as bar:
            while currentDay != lastDay:
                examplesOfDay = []
                dataOfDay = self.__mydb.extractReceipts(currentDay, mapping)
                self.__window.deleteFurthestDay()
                self.__window.set(dataOfDay, currentDay)
                self.__window.generateLabels(examplesOfDay)
                self.__window.generateExamplesLabelsForMulReceipts(examplesOfDay, categories)  # and labels on multiple receipts
                self.__window.clean()
                self.__insertLabeledExamples(examplesOfDay, currentDay)
                currentDay += dt.timedelta(days=1)
                bar()
        self.__mydb.closeConnection()

    """        
       Metodo che effettua la serializzazione degli esempi etichettati (examplesOfDay) in data currentDay. 
       Ciascun file (pickle) avrà nome pari al currentDay in cui è stato etichettato.
       I Day vuoti non verranno serializzati.
    """

    def __insertLabeledExamples(self, examplesOfDay: list, currentDay: dt.date):
        try:
            df = pd.DataFrame(examplesOfDay)
            df = df.apply(pd.to_numeric, downcast='float')
            dateColumn = list(df.columns)[len(examplesOfDay[0]) - 2]
            df.sort_values([dateColumn], ascending=True, inplace=True)
            df.drop(columns=[dateColumn], inplace=True)
            # Crea il percorso alla tua sotto cartella e al file
            path = self.__outputFolder / str(currentDay)
            try:
                # Apri il file
                with open(path, 'wb') as f:
                    # Inserisci file nel pickle
                    pickle.dump(df, f)
                # with chiude automaticamente la connessione al file dopo aver inserito i pickle
            except FileNotFoundError:
                os.mkdir(self.__outputFolder)
                with open(path, 'wb') as f:
                    # Inserisci file nel pickle
                    pickle.dump(df, f)
        except IndexError:
            pass


"""
    Sfruttiamo la libreria argparse per creare degli argument utilizzabili da Command Line
"""

parser = argparse.ArgumentParser()
parser.add_argument('--host', help='Il nome del server o l\'indirizzo IP su cui è in esecuzione MySQL. Se si esegue'
                    ' su localhost è possibile utilizzare localhost o IP 127.0.0.0.', default='localhost', type=str)
parser.add_argument('--user', help='Il nome utente che si utilizza per lavorare con MySQL. Il nome utente predefinito '
                    'per il database MySQL è root.', default='root', type=str)
parser.add_argument('--password', help='La password viene fornita dall\'utente al momento dell\'installazione del '
                    'server MySQL.', type=str)
parser.add_argument('--database', help='Il nome del database a cui si desidera connettersi ed eseguire le operazioni.', type=str)
parser.add_argument('--churnDim', help='Dimensione del churn, di tipo int.', type=int)
parser.add_argument('--periodDim', help='Dimensione del periodo, di tipo int.', type=int)
parser.add_argument('--periods', help='Numero di periodi, di tipo int.', type=int)
parser.add_argument('--level', help='livello di gerarchia delle categorie da utilizzare, di tipo int;', type=int)
parser.add_argument('--traditionalRFM', help='Valore binario per stabilire se considerare o meno queste feature (1 - Sì, 0 - No).', type=int)
parser.add_argument('--aggregates', help='Valore binario per stabilire se considerare o meno queste feature (1 - Sì, 0 - No).', type=int)
parser.add_argument('--productRFM', help='Valore binario per stabilire se considerare o meno queste feature (1 - Sì, 0 - No).', type=int)
parser.add_argument('--productAggregates', help='Valore binario per stabilire se considerare o meno queste feature (1 - Sì, 0 - No)..', type=int)
parser.add_argument('--start', help='Data di partenza in formato: AAAA-MM-DD, OPZIONALE: di default la prima del db.',
                    default=None)
parser.add_argument('--end', help='Data di fine in formato: AAAA-MM-DD, OPZIONALE: di default l\'ultima del db.',
                    default=None)
args = parser.parse_args()
try:
    if len(sys.argv) > 1:
        StreamBuilder(args.host, args.user, args.password, args.database, args.churnDim, args.periodDim, args.periods,
                      args.level, args.traditionalRFM, args.aggregates, args.productRFM, args.productAggregates, args.start, args.end)
    else:
        current_dir = os.getcwd()
        dir_target = 'rfm_stream_builder'

        while os.path.basename(current_dir) != dir_target:
            current_dir = os.path.dirname(current_dir)

        with open(current_dir + '/resources/config.json', 'r') as file:
            config = json.load(file)

        StreamBuilder(config["host"]["value"], config["user"]["value"], config["password"]["value"], config["database"]["value"],
                      config["churnDim"]["value"], config["periodDim"]["value"], config["periods"]["value"], config["level"]["value"],
                      config["traditionalRFM"]["value"], config["aggregates"]["value"], config["productRFM"]["value"],
                      config["productAggregates"]["value"], config["start"]["value"], config["end"]["value"])
except ValueError as err:
    print('\033[91m' + str(err))
