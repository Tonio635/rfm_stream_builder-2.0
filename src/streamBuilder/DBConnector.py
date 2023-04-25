"""
// Name        : DBConnector.py
// Author      : Andrea Brunetta, Francesco Luce
// Version     : 3.0
// Description : La classe DBConnector modella la connessione al DB.
                 Modulo MySQL Connector Python. Questa classe sviluppa e integra 
                 il nostro progetto Python con un server di database MySQL.
                 MySQL Connector Python è scritto in Python ed è autosufficiente per eseguire query di database 
                 tramite Python. È un driver ufficiale supportato da Oracle per funzionare con MySQL e Python. 
"""

import mysql.connector
from CategoryMapping import CategoryMapping

class DBConnector:
    __mydb = mysql.connector.MySQLConnection()

    """
        Metodo costruttore:
            - host: Il nome del server o l'indirizzo IP su cui è in esecuzione MySQL. Se si esegue su localhost, 
                    è possibile utilizzare localhost o il suo IP 127.0.0.0;
            - username: Il nome utente che si utilizza per lavorare con MySQL. 
                        Il nome utente predefinito per il database MySQL è 'root';
            - password: La password viene fornita dall'utente al momento dell'installazione del server MySQL. 
                        Se si usa root, non c'è bisogno della password;
            - database: Il nome del database a cui si desidera connettersi ed eseguire le operazioni.
        Il costruttore setta gli attributi della classe con i parametri ricevuti in input.
    """
    def __init__(self, host="localhost", username="root", password="", database="test_db"):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__database = database
        self.__mydb = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )

    """
        Metodo per chiudere le connessioni aperte al termine del lavoro.
    """
    def closeConnection(self):
        self.__mydb.close()

    def __scaleHierarchy(self, child, hierarchy, diff):
        parents = []

        if diff == 0:
            return [child]

        for row in hierarchy:
            if child == row[1]:
                parents.append(row[0])

        result = []
        for parent in parents:
            result += self.__scaleHierarchy(parent, hierarchy, diff-1)

        return result

    def __descendHierarchy(self, parent, hierarchy, diff):
        children = []

        if diff == 0:
            return [parent]

        for row in hierarchy:
            if parent == row[0]:
                children.append(row[1])

        result = []
        for child in children:
            result += self.__descendHierarchy(child, hierarchy, diff-1)

        return result

    def extractProductHierarchy(self, level):
        mapping = {}
        cursor = self.__mydb.cursor()
        cursor.execute("SELECT Products.K_Product, Products.K_Product_Type, N_Level FROM Products, Product_Types WHERE Products.K_Product_Type=Product_Types.K_Product_Type")
        products = cursor.fetchall()

        cursor.execute("SELECT K_Product_Parent, K_Product_Child FROM Product_Hierarchies")
        hierarchy = cursor.fetchall()

        for row in products:
            mapping[row[0]] = []
            if row[2] == level:
                mapping[row[0]].append(row[1])
            elif row[2] > level:
                parents = self.__scaleHierarchy(row[0], hierarchy, row[2] - level)                
                mapping[row[0]] = list(set([products[[x[0] for x in products].index(val)][1] for val in parents]))
            else:
                children = self.__descendHierarchy(row[0], hierarchy, level - row[2])
                mapping[row[0]] = list(set([products[[x[0] for x in products].index(val)][1] for val in children]))
            

        return CategoryMapping(mapping)

    """
        Metodo che effettua la query estraendo le ricevute del giorno.
        I metodi execute() eseguono la query SQL e restituiscono il risultato.
        cursor() di un oggetto MySQLConnection per creare un oggetto cursore per eseguire varie operazioni SQL.
    """
    def extractReceipts(self, gg, mapping):
        cursor = self.__mydb.cursor()
        cursor.execute("SELECT * FROM Receipts WHERE DATE(T_Receipt) = %s ORDER BY K_Member, T_Receipt ASC",
                       [gg.isoformat()])
        rows = cursor.fetchall()
        
        for i in range(len(rows)):
            cursor.execute("SELECT Products.K_Product, Quantity, Q_Amount, Q_Discount_Amount FROM Receipt_Lines, Products WHERE %s = K_Receipt AND Receipt_Lines.K_Product = Products.K_Product", [rows[i][0]])
            lines = cursor.fetchall()
            for j in range(len(lines)):
                lines[j] = list(lines[j])
                lines[j][0] = mapping.getProductCategories(lines[j][0])
                lines[j] = tuple(lines[j])
            rows[i] = rows[i] + (lines,)
        
        return rows

    """
        Metodo che effettua la query per estrarre la prima data del DB.
        MIN perchè è la data meno recente di tutto il DB.
    """
    def extractFirstDay(self):
        cursor = self.__mydb.cursor()
        cursor.execute("SELECT DATE(MIN(T_Receipt)) FROM Receipts")
        rows = cursor.fetchall()
        return rows[0][0]

    """
        Metodo che effettua la query per estrarre l'ultima data del DB.
        MAX perchè è la data più recente di tutto il DB.
    """
    def extractLastDay(self):
        cursor = self.__mydb.cursor()
        cursor.execute("SELECT DATE(MAX(T_Receipt)) FROM Receipts")
        rows = cursor.fetchall()
        return rows[0][0]