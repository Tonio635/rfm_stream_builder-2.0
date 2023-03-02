"""
// Name        : Main.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe Main.
"""

import os
import matplotlib.pyplot as plt
import scikitplot as skplt
import argparse

from sklearn.metrics import accuracy_score, classification_report
from src.classification.offline.OfflineLearner import OfflineLearner
from src.classification.PickleLoader import PickleLoader
from src.classification.offline.OfflineClassifierEnum import OfflineClassifierEnum


class Main:
    # Costante dove salviamo il percorso della cartella dove viene serializzato lo stream
    STREAMFOLDERPATH = 'output'
    MODELSFOLDERPATH = 'serialized_models/offline'

    """
        Metodo costruttore. Richiama il metodo main di Main.
    """
    def __init__(self, start: str, end: str, serialized: str):
        self.__main(start, end, serialized)

    """
        Metodo printReport per la stampa di matrice di confusione e diversi score.
    """
    def __printReport(self, results: list, title: str):
        acc = accuracy_score(results[0], results[1])
        report = classification_report(results[0], results[1])
        print(f'Accuracy: {acc}')
        print(f'Missclassification: {1 - acc}')
        print(report)
        skplt.metrics.plot_confusion_matrix(results[0], results[1])
        plt.title(title)
        plt.show()

    """ 
        Metodo main. Si occupa di avviare l'instanzazione del learner, loader e avvia fase di train e test. Infine 
        richiama un metodo per la stampa dei risultati
    """
    def __main(self, start: str, end: str, serialized: str):
        # Carichiamo un modello precedentemente serializzato
        if serialized:
            file_path = os.path.join(self.MODELSFOLDERPATH, serialized)
            learner = OfflineLearner(fromPickle=file_path)
        else:
            print("Classificatori disponibili: \n")
            for elem in [elem for elem in OfflineClassifierEnum]:
                print(f'{elem.value} - {elem.name}')
            print("\n")

            i = int(input("Inserire numero classificatore"))
            if i not in [elem.value for elem in OfflineClassifierEnum]:
                raise ValueError("Effettuare scelta correttamente")

            # Istanziamo il learner richiamando il costruttore di OnlineLearner e passando come parametro l'enumerativo
            # corrsipondente alla scelta
            learner = OfflineLearner(OfflineClassifierEnum(i))

        # in files carichiamo la lista di file in STREAMFOLDERPATH
        files = os.listdir(self.STREAMFOLDERPATH)
        if None not in [start, end]:
            try:
                # Splittiamo il troncone di file delimitato tra start ed end presi, eventualmente, in input
                files = files[files.index(start): files.index(end) + 1]
            except ValueError:
                print("Uno dei file di inizio o di fine non è presente all'interno della cartella, ")

        # Stabiliamo percentuale Train Set
        train_percentage = int((len(files) * 70) / 100)

        # loader per il train che va da start a 70% (esempio) dove start può essere passato in input
        train_loader = PickleLoader(self.STREAMFOLDERPATH, files, start=files[0], end=files[train_percentage])
        # loader per il test che va da 70% a end dove end può essere passato in input
        test_loader = PickleLoader(self.STREAMFOLDERPATH, files, start=files[train_percentage + 1], end=files[-1])

        # TRAIN
        print("Training:")
        learner.train(train_loader)

        # TEST
        print("Testing:")
        results = learner.test(test_loader)

        # STAMPA DEI RISULTATI
        self.__printReport(results, "")

        # SERIALIZZAZIONE MODELLO
        if input("Vuoi serializzare il modello? (y/n)") == 'y':
            learner.toPickle('serialized_models', input("Inserire nome file:"))


parser = argparse.ArgumentParser()
parser.add_argument('--start',
                    help='Data di partenza in formato: AAAA-MM-DD, OPZIONALE: di default la prima della cartella.',
                    default=None)
parser.add_argument('--end',
                    help='Data di fine in formato: AAAA-MM-DD, OPZIONALE: di default l\'ultima della cartella.',
                    default=None)
parser.add_argument('--serialized',
                    help='Nome del file da caricare che contiene il modello precedentemente addestrato e serializzato',
                    default=None)
args = parser.parse_args()
try:
    Main(args.start, args.end, args.serialized)
except ValueError as err:
    print('\033[91m' + str(err))
