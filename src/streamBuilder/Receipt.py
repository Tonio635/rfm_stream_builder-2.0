"""
// Name        : Receipt.py
// Author      : Andrea Brunetta, Francesco Luce, Antonio Giuseppe Doronzo
// Version     : 4.0
// Description : La classe Receipt modella la singola entry della tabella Receipt del DB.
                 Essa contiene tutti i campi della tabella Receipt come attributi e relativi metodi get e set.
"""

class Receipt:

    categories: dict[int, str] = {}

    """
        Metodo costruttore. Inizializza gli attributi privati della classe con i valori passati in input.
            - K_Receipt: id della receipt, di tipo str;
            - K_Member: id del cliente, di tipo str;
            - Quantity: quantità del prodotto acquistato, di tipo int;
            - Q_Amount: prezzo totale, di tipo float;
            - Q_Discount_Amount: sconto totale, di tipo int, al momento non trattato;
            - T_Receipt: Data e orario dell'acquisto;
            - lines: Receipt lines che formano la ricevuta.
    """
    def __init__(self, K_Receipt, K_Member, Quantity, Q_Amount, Q_Discount_Amount, T_Receipt, lines):
        self.__K_Receipt = K_Receipt
        self.__K_Member = K_Member
        self.__Quantity = Quantity
        self.__Q_Amount = Q_Amount
        self.__Q_Discount_Amount = Q_Discount_Amount
        self.__T_Receipt = T_Receipt
        self.__lines = lines

    """
        Metodo getter attributo K_Receipt.
        Return di un tipo str.
    """
    def getKReceipt(self):
        return self.__K_Receipt

    """
        Metodo getter attributo K_Member.
        Return di un tipo str.
    """
    def getKMember(self):
        return self.__K_Member

    """
        Metodo getter attributo Quantity.
        Return di un tipo int.
    """
    def getQuantity(self):
        return self.__Quantity

    """
        Metodo getter attributo Q_Amount.
        Return di un tipo float.
    """
    def getQAmount(self):
        return self.__Q_Amount

    """
        Metodo getter attributo Q_Discount_Amount.
        Return di un tipo int.
    """
    def getQDiscountAmount(self):
        return self.__Q_Discount_Amount

    """
        Metodo getter attributo T_Receipt.
        Return di un tipo datetime.
    """
    def getTReceipt(self):
        return self.__T_Receipt
    
    """
        Metodo finalizzato ad ottenere le top k categorie della ricevuta in base ad un type specifico.
        type = 1: top categorie in base a Quantity
        type = 2: top categorie in base a Q_Amount
        type = 3: top categorie in base a Q_Discount_Amount
        Return di una lista di interi.
    """
    def getTopFrequentCategories(self, k, type):
        # creazione di un dizionario per mantenere la somma delle quantità/qamount/qdiscountamount per ogni categoria
        categories_count = {}

        if type == 1:           # top categorie in base alla quantity
            for line in self.__lines:
                category_id = line.getCategoryID()
                quantity = line.getQuantity()
                if category_id in categories_count:
                    categories_count[category_id] += quantity
                else:
                    categories_count[category_id] = quantity
        elif type == 2:         # top categorie in base alla q_amount
            for line in self.__lines:
                category_id = line.getCategoryID()
                q_amount = line.getQAmount()
                if category_id in categories_count:
                    categories_count[category_id] += q_amount
                else:
                    categories_count[category_id] = q_amount
        elif type == 3:         # top categorie in base alla q_discount_amount
            for line in self.__lines:
                category_id = line.getCategoryID()
                q_discount_amount = line.getQDiscountAmount()
                if category_id in categories_count:
                    categories_count[category_id] += q_discount_amount
                else:
                    categories_count[category_id] = q_discount_amount
        else:
            return None
        
        # ordinamento del dizionario in ordine decrescente in base alla somma
        sorted_categories = sorted(
            categories_count.items(), key=lambda x: x[1], reverse=True)

        # restituzione dei primi k elementi del dizionario come lista di interi
        top_k_categories = [category[0] for category in sorted_categories[:k]]

        i = len(top_k_categories)

        # se non ci sono sufficienti categorie, si riempiono gli spazi rimasti con "-1"
        while i < k:
           top_k_categories.append(-1)
           i += 1

        return top_k_categories

    """
        Metodo finalizzato ad ottenere il numero distinto di categorie presenti nella ricevuta.
        Return di un tipo int.
    """
    def getNumDistinctCategories(self):
        distinctCategories = set([receiptLine.getCategoryID() for receiptLine in self.__lines])
        return len(distinctCategories)