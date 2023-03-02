"""
// Name        : PickleLoader.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : La seguente classe si occupa di aprire la directory contenente i pickle e caricarli, restituendo
                 il prossimo elemento fino alla fine della directory. Sono parametrizzati anche lo start e l'end.
"""

import pickle
import os
from alive_progress import alive_bar


"""
    Metdo PickleLoader per caricare il pickle
"""
def PickleLoader(folderPath: str, files: list, start: str = None, end: str = None):
    try:
        toLoad = files[files.index(start): files.index(end) + 1]
    except ValueError:
        toLoad = files.copy()
    # Scandisce la lista di file all'interno della cartella.
    with alive_bar(len(toLoad), force_tty=True) as bar:
        for filename in toLoad:
            # Concatena il percorso della cartella con il nome del file.
            file_path = os.path.join(folderPath, filename)
            # Se file_path rappresenta un file (e non una dir).
            if os.path.isfile(file_path):
                # Apriamo il file.
                with open(file_path, "rb") as f:
                    # Carichiamo il pickle.
                    yield pickle.load(f)
                    bar()

