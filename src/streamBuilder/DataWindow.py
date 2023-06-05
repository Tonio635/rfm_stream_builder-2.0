"""
// Name        : DataWindow.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : Classe che modella la finestra del cliente.
"""

import datetime as dt
from itertools import islice
from itertools import chain
import numpy as np
import operator
from decimal import Decimal

from ExampleSequence import ExampleSequence
from CustomerWindow import CustomerWindow
from Day import Day
from Example import Example
from ExampleDictionary import ExampleDictionary
from Receipt import Receipt
from Rfm import Rfm
from ReceiptLine import ReceiptLine


class DataWindow:
    """
        Metodo costruttore. Inizializza gli attributi privati della classe con i valori passati in input.
            - churnDim: dimensione del churn, di tipo int;
            - periodDim: dimensione del periodo, di tipo int;
            - periods: numero di periodi, di tipo int;
            - windowDim: dimensione della data windows, il max(periodDim * periods, churnDim)
            - currentDay: giorno attuale;
            - examples: dizionario che conterrà gli esempi in attesa di essere etichettati;
            - window: dizionario <k, v> dove k = K_Member e v = customerWindow di quel cliente;
    """

    def __init__(self, periodDim: int, periods: int, churnDim: int, traditionalRFM: int, aggregates: int,
                 productRFM: int, productAggregates: int):
        self.__churnDim = churnDim
        self.__periodDim: int = periodDim
        self.__periods: int = periods
        self.__traditionalRFM: int = traditionalRFM
        self.__aggregates: int = aggregates
        self.__productRFM: int = productRFM
        self.__productAggregates: int = productAggregates
        self.__windowDim: int = max(periodDim * periods, churnDim)
        self.__currentDay: dt.date = None
        self.__examples: ExampleDictionary = ExampleDictionary()
        self.__window: dict = {}

    """
        Metodo set che prende in input una lista di tuple, ovvero il risultato di una query sul db, e la data del giorno
        e setta i relativi Day, liste di receipts, nelle customer windows. 
    """
    def set(self, data: list[tuple], dateToSet: dt.date):
        self.__currentDay = dateToSet
        # Lista che contiene le liste di ricevute di ciascun cliente
        receipts = []
        try:
            # Salviamo il 'K_Member' della lista data in prima posizione, in modo da usarlo come confronto iniziale
            oldMember = data[0][1]

            # Scandisce la lista di tuple
            for row in data:
                receiptLines = []
                for line in row[6]:
                    receiptLines.append(ReceiptLine(line[0], line[1], line[2], line[3]))
                # Confronta l'attuale 'K_Member' con oldMember. Se non siamo ancora sulle sue ricevute
                if row[1] != oldMember:
                    # Costruisce il Day passando come oggetto la lista di receipts
                    day = Day(receipts)
                    try:
                        # Prova ad accedere alla CustomerWindow e settare il Day
                        self.__window[oldMember].setDay(day, lastPurchase)
                    except KeyError:
                        # Altrimenti inizializza la CustomerWindow e setta il Day
                        cw = CustomerWindow(oldMember, self.__windowDim)
                        cw.setDay(day, lastPurchase)
                        self.__window[oldMember] = cw
                    # Svuotiamo la lista di receipts e la inizializziamo con la Receipt del nuovo cliente
                    receipts = [
                        Receipt(row[0], row[1], row[2], row[3], row[4], row[5], receiptLines)
                    ]
                    # Salviamo il suo ultimo acquisto
                    lastPurchase = row[5]
                    # Settiamo il nuovo K_Member come old
                    oldMember = row[1]
                # Se siamo ancora tra le receipts di oldMember, aggiungiamo la receipt alla lista
                else:
                    receipts.append(Receipt(row[0], row[1], row[2], row[3], row[4], row[5], receiptLines))
                    lastPurchase = row[5]

            # L'ultimo cliente non sarà mai precedente di nessuno, viene aggiunto a prescindere
            day = Day(receipts)
            try:
                self.__window[row[1]].setDay(day, lastPurchase)
            except KeyError:
                cw = CustomerWindow(row[1], self.__windowDim)
                cw.setDay(day, lastPurchase)
                self.__window[row[1]] = cw
        except IndexError:
            pass

    """
        Metodo per pulire la DataWindow rimuovendo le CustomerWindow aventi tutti i Day vuoti. Questo significa che non
        sono stati effettuati acquisti dal cliente negli ultimi windowDim giorni.
    """
    def clean(self):
        self.__window = {key: value for (key, value) in self.__window.items() if not value.isEmpty()}

    """
        Metodo per cancellare dalla DataWindow il giorno più lontano. 
    """
    def deleteFurthestDay(self):
        for val in self.__window.values():
            val.deleteFurthestDay()

    """
        Metodo per la generazione degli esempi. Ha in input una lista dove collezionare gli esempi etichettati.
        La generazione degli esempi avviene nel seguente modo:
            - generazione dell'esempio anche per i giorni in cui non ci sono ricevute ma ci sono esempi nel 
              ExampleDictionary in attesa di etichettatura.
            - generazione di un esempio per ogni ricevuta del currentDay.
        Per ogni esempio calcolo RFM su tutti i 'periods' periodi. 
    """
    def generateExamplesLabelsForMulReceipts(self, toFill: list, categories: list[str]):
        # Generazione esempi per tutti quei clienti che hanno comprato
        # nel periodo che va da ]currentDay-churnDim, currentDay]
        try:
            # Lista di CustomerWindow dei clienti che in currentDay hanno effettuato acquisti e/o sono nel dizionario
            windows = [cw for cw in self.__window.values()
                       if (self.__currentDay - cw.getLastReceipt().date()).days < self.__churnDim]
            for cw in windows:
                recencys = {key: -1 for key in categories}
                rfm = Rfm(0, 0, 0)
                periods = self.__splitPeriods(cw)
                ex = Example(self.__currentDay)

                recencyPeriod = [periods[-2][-1]] + periods[-1][:-1] if len(periods) > 1 else [None] + periods[-1][:-1]

                for day in recencyPeriod:
                    categoriesBought = day.getCategoriesBought() if day is not None else set()
                    for key in recencys.keys():
                        if key in categoriesBought:
                            recencys[key] = 0
                        elif recencys[key] != -1:
                            recencys[key] += 1

                for period in periods:
                    
                    rfm = self.__calculateRFM(period)
                    productRfm = self.__calculateProductRFM(period, categories)
                    ex.addRfm(rfm)
                    ex.addProductRfm(productRfm)
                # Inserisce l'esempio in ExampleDictionary. Esso è formato dai k (con k=periods) RFM calcolati.
                self.__examples.insertExample(cw.getKMember(), ex)
                # Verifica se il cliente attuale ha acquistato nel currentDay
                if cw.getLastReceipt().date() == self.__currentDay:
                    # Accesso all'ultimo elemento della DataWindow attraverso l'operatore 'itemgetter' della libreria
                    # operator per controllare qualora vi siano più ricevute relative al currentDay
                    day = operator.itemgetter(-1)(cw.getListOfDays())
                    receipts = day.getReceiptsOfDay()
                    # Se nel Day ci sono più ricevute
                    if len(receipts) > 1:
                        # Instanziazione dell'ExampleSequence che conterrà gli esempi da etichettare immediatamente
                        seq = ExampleSequence()
                        # Ciclo sulle ricevute del giorno partendo dall'ultima. Questo ci permetterà di scandire una sola
                        # volta il periodo per il calcolo RFM. Per le ricevute precedenti all'ultima, il calcolo viene
                        # effettuato per sottrazione.
                        receipts.reverse()
                        oldMonetary = receipts[0].getQAmount()
                        oldProductMonetary = receipts[0].getInfoCategories(categories)
                        oldReceiptCategories = set(category for line in receipts[0].getLines() for category in line.getCategories())

                        remainingReceipts = receipts[1:].copy()

                        for receipt in receipts[1:]:
                            rfm = Rfm(rfm.getRecency(), rfm.getFrequency() - 1, rfm.getMonetary() - oldMonetary)
                            productsRfm = []
                            for i in range(len(categories)):
                                recency = -1
                                for ricevuta in remainingReceipts:
                                    if ricevuta.getInfoCategories(categories)[categories[i]] != 0:
                                        recency = 0
                                        break
                                
                                if recencys[categories[i]] != -1 and recency == -1:
                                    recency = recencys[categories[i]] + 1
                                
                                frequency = productRfm[i].getFrequency() - 1 if categories[i] in oldReceiptCategories else productRfm[i].getFrequency()
                                monetary = productRfm[i].getMonetary() - Decimal(oldProductMonetary[categories[i]])
                                productsRfm.append(Rfm(recency, frequency, monetary))
                            
                            remainingReceipts.pop(0)
                            newExample = ex.copy()
                            newExample.replaceLastRfm(rfm)
                            newExample.replaceLastProductRfm(productsRfm)
                            newExample.setLabelTimestamp(receipt.getTReceipt())
                            seq.appendExample(newExample.copy())
                            oldMonetary = receipt.getQAmount()
                            oldProductMonetary = receipt.getInfoCategories(categories)
                            oldReceiptCategories = set(category for line in receipt.getLines() for category in line.getCategories())

                        # Etichettatura a False degli esempi costruiti per questa casistica
                        seq.record(False, toFill, self.__traditionalRFM, self.__aggregates, self.__productRFM, self.__productAggregates)
        except TypeError as err:
            print(err)

    """
        Metodo per suddividere una CustomerWindow in 'periods' sotto-periodi di dimensione 'periodDim'.
    """
    def __splitPeriods(self, cw: CustomerWindow):
        days = cw.getListOfDays()
        iter_days = iter(days)
        length_to_split = [self.__periodDim] * self.__periods
        return [list(islice(iter_days, elem)) for elem in length_to_split]

    """
        Metodo per calcolare l'RFM di un cliente, dato in input il periodo.
        Ritorna al chiamante un oggetto di tipo Rfm.
    """
    def __calculateRFM(self, period: list[Day]):
        recency = -1
        frequency = 0
        monetary = 0
        if period != [None] * self.__periodDim:
            receipts = np.asarray(
                list(chain.from_iterable([day.getReceiptsOfDay() for day in period if day is not None]))
            )
            lastPos = self.__periodDim - next((pos for pos, el in enumerate(period.__reversed__()) if el is not None),
                                              self.__periodDim) - 1
            recency = self.__periodDim - lastPos - 1
            frequency = np.count_nonzero(receipts)
            monetary = np.sum([receipt.getQAmount() for receipt in receipts])
        return Rfm(recency, frequency, monetary)

    """
        Metodo per calcolare l'RFM delle categorie dei prodotti, dato in input il periodo.
        Ritorna al chiamante un oggetto di tipo lista di Rfm.
    """
    def __calculateProductRFM(self, period: list[Day], categories: list[str]):
        recency = -1
        frequency = 0
        monetary = 0
        productsRFM = []
        for key in categories:
            if period != [None] * self.__periodDim:
                days = []
                receipts = []
                for day in period:
                    if day is not None:
                        days.append(day.getReceiptsOfDay())
                        for receipt in day.getReceiptsOfDay():
                            receipts.append(receipt)
                    else:
                        days.append(None)
                
                found = False
                lastPos = self.__periodDim
                for pos, value in enumerate(days.__reversed__()):
                    if value is not None:
                        for receipt in value:
                            if receipt.getInfoCategories(categories)[key] != 0:
                                lastPos = self.__periodDim - pos - 1
                                found = True
                                break
                        if found:
                            break
                
                recency = self.__periodDim - lastPos - 1
                frequency = np.count_nonzero([receipt.getInfoCategories(categories)[key] for receipt in receipts if receipt is not None])
                monetary = np.sum([receipt.getInfoCategories(categories)[key] for receipt in receipts if receipt is not None])
            productsRFM.append(Rfm(recency, frequency, monetary))
        
        return productsRFM

    """
        Metodo per generare le etichette.
    """
    def generateLabels(self, toFill: list):
        timestamp = dt.datetime(self.__currentDay.year, self.__currentDay.month, self.__currentDay.day, 23, 59, 59)
        try:
            customers = [cw.getKMember() for cw in self.__window.values() if
                         cw.getLastReceipt().date() == self.__currentDay]
            for customer in customers:
                try:
                    self.__examples.recordLabeledExample(customer, False, timestamp, toFill, self.__traditionalRFM, self.__aggregates, self.__productRFM, self.__productAggregates)
                    self.__examples.delete(customer)
                except KeyError:
                    pass
        except TypeError:
            pass

        try:
            customers = [cw.getKMember() for cw in self.__window.values() if
                         (self.__currentDay - cw.getLastReceipt().date()).days == self.__churnDim]
            for member in customers:
                try:
                    self.__examples.recordLabeledExample(member, True, timestamp, toFill, self.__traditionalRFM, self.__aggregates, self.__productRFM, self.__productAggregates)
                    self.__examples.delete(member)
                except KeyError:
                    pass
        except TypeError:
            pass
