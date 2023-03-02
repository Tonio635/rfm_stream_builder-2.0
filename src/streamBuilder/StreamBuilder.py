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
            - start: data di partenza, di default la prima del db;
            - end: data di fine, di default l'ultima del db;
            - outputFolder: percorso della cartella output dove vengono salvati i pickle.
        Inizializza la DataWindow e richiama il metodo privato generateStream().
    """
    def __init__(self, host: str, username: str, password: str, databaseName: str,
                 churnDim: int, periodDim: int, periods: int, start: dt.date = None,
                 end: dt.date = None):
        self.__outputFolder = Path("./../../output")
        if None in [host, username, password, databaseName, churnDim, periodDim, periods]:
            raise ValueError("Argomenti non validi, assicurati di aver inserito tutti i parametri necessari!")
        if churnDim > periodDim*periods:
            raise ValueError("Il parametro churnDim non può essere maggiore di periodDim*periods. "
                             "Questo impatta negativamente la funzione splitPeriods di DataWindow!")
        try:
            self.__mydb = DBConnector(host, username, password, databaseName)
        except mysql.connector.errors.ProgrammingError:
            raise ValueError("Connessione al db fallita, controllare che i parametri siano corretti")

        self.__window: DataWindow = DataWindow(periodDim, periods, churnDim)
        self.__generateStream(start, end)

    """
        Metodo per la generazione ed etichettatura di esempi. Infine serializziamo gli esempi in un pickle.
    """
    def __generateStream(self, start: str, end: str):
        currentDay = self.__mydb.extractFirstDay() if start is None else dt.date.fromisoformat(start)
        lastDay = self.__mydb.extractLastDay() if end is None else dt.date.fromisoformat(end)
        with alive_bar((lastDay-currentDay).days, force_tty=True) as bar:
            while currentDay != lastDay:
                examplesOfDay = []
                dataOfDay = self.__mydb.extractReceipts(currentDay)
                self.__window.deleteFurthestDay()
                self.__window.set(dataOfDay, currentDay)
                self.__window.generateLabels(examplesOfDay)
                self.__window.generateExamplesLabelsForMulReceipts(examplesOfDay)  # and labels on multiple receipts
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
parser.add_argument('--database', help='Il nome del database a cui si desidera connettersi ed eseguire le operazioni.'
                    , type=str)
parser.add_argument('--churnDim', help='Dimensione del churn, di tipo int.', type=int)
parser.add_argument('--periodDim', help='Dimensione del periodo, di tipo int.', type=int)
parser.add_argument('--periods', help='Numero di periodi, di tipo int.', type=int)
parser.add_argument('--start', help='Data di partenza in formato: AAAA-MM-DD, OPZIONALE: di default la prima del db.',
                    default=None)
parser.add_argument('--end', help='Data di fine in formato: AAAA-MM-DD, OPZIONALE: di default l\'ultima del db.',
                    default=None)
args = parser.parse_args()
try:
    StreamBuilder(args.host, args.user, args.password, args.database, args.churnDim, args.periodDim, args.periods,
                  args.start, args.end)
except ValueError as err:
    print('\033[91m' + str(err))
