DROP DATABASE IF EXISTS `test_tesi`;
CREATE DATABASE `test_tesi`;

USE `test_tesi`;

DROP TABLE IF EXISTS `receipts`;

CREATE TABLE `receipts` (
    `K_Receipt` varchar(100) NOT NULL,
    `K_Member` varchar(100) NOT NULL,
    `Quantity` int DEFAULT NULL,
    `Q_Amount` decimal(20,2) DEFAULT NULL,
    `Q_Discount_Amount` int DEFAULT NULL,
    `T_Receipt` timestamp NULL DEFAULT NULL,
    PRIMARY KEY (`K_Receipt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `receipts` WRITE;
INSERT INTO `receipts` VALUES ('1','Giulio',1,20.53,NULL,'2022-01-10 00:00:00'),('2','Giulio',1,52,NULL,'2022-01-14 00:00:00'),('3','Giulio',1,5.99,NULL,'2022-01-16 00:00:00'),('4','Giulio',1,8.70,NULL,'2022-01-16 01:00:00'),('5','Giulio',1,35.67,NULL,'2022-01-27 00:00:00');
UNLOCK TABLES;

DROP TABLE IF EXISTS `product_types`;

CREATE TABLE `product_types` (
    `K_Product_Type` varchar(100) NOT NULL,
    `N_Level` int DEFAULT NULL,
    PRIMARY KEY (`K_Product_Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `product_types` WRITE;
INSERT INTO `product_types` VALUES ('mobili_da_sala', 3), ('segnaletica_e_sicurezza', 3), ('aria_condizionata', 3), ('fumetti', 3), ('console_giochi', 3), ('SALA_E_GIARDINO', 2), ('SICUREZZA', 2), ('ARREDAMENTO', 2), ('SVAGO', 2) ('CASA_E_GIARDINO', 2), ('RADICE', 1);
UNLOCK TABLES;

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
    `K_Product` varchar(100) NOT NULL,
    `K_Product_Type` varchar(100) DEFAULT NULL,
    PRIMARY KEY (`K_Product`),
    KEY `K_Product_Type` (`K_Product_Type`),
    CONSTRAINT `products_ibfk_1` FOREIGN KEY (`K_Product_Type`) REFERENCES `product_types` (`K_Product_Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `products` WRITE;
INSERT INTO `products` VALUES ('P1', 'mobili_da_sala'), ('P2', 'segnaletica_e_sicurezza'), ('P3', 'aria_condizionata'), ('P4', 'console_giochi'), ('P5', 'fumetti'), ('P10', 'SALA_E_GIARDINO'), ('P11', 'SICUREZZA'), ('P12', 'SVAGO'), ('P13', 'CASA_E_GIARDINO'), ('P14', 'ARREDAMENTO'), ('P100', 'RADICE');
UNLOCK TABLES;

DROP TABLE IF EXISTS `receipt_lines`;

CREATE TABLE `receipt_lines` (
    `K_Receipt_Line` int NOT NULL AUTO_INCREMENT,
    `K_Receipt` varchar(100) NOT NULL,
    `K_Product` varchar(100) NOT NULL,
    `Quantity` int DEFAULT NULL,
    `Q_Amount` decimal(20,2) DEFAULT NULL,
    `Q_Discount_Amount` int DEFAULT NULL,
    PRIMARY KEY (`K_Receipt_Line`),
    KEY `K_Receipt` (`K_Receipt`),
    KEY `K_Product` (`K_Product`),
    CONSTRAINT `receipt_lines_ibfk_1` FOREIGN KEY (`K_Receipt`) REFERENCES `receipts` (`K_Receipt`),
    CONSTRAINT `receipt_lines_ibfk_2` FOREIGN KEY (`K_Product`) REFERENCES `products` (`K_Product`)
) ENGINE=InnoDB AUTO_INCREMENT=112651 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `receipt_lines` WRITE;
INSERT INTO `receipt_lines` VALUES (1,'1','P1',1,10.00,NULL), (2,'1','P3',1,5.53,NULL), (3,'1','P2',1,5.00,NULL), (4,'2','P4',1,52.00,NULL), (5,'3','P1',1,2.99,NULL), (6,'3','P5',1,3,NULL), (7,'4','P2',1,4.70,NULL), (8,'4','P4',1,4.00,NULL), (9,'5','P3',1,35.67,NULL);
UNLOCK TABLES;

DROP TABLE IF EXISTS `product_hierarchies`;

CREATE TABLE `product_hierarchies` (
    `K_Product_Hierarchy` varchar(100) NOT NULL,
    `K_Product_Parent` varchar(100) NOT NULL,
    `K_Product_Child` varchar(100) NOT NULL,
    PRIMARY KEY (`K_Product_Hierarchy`),
    KEY `K_Product_Parent` (`K_Product_Parent`),
    KEY `K_Product_Child` (`K_Product_Child`),
    CONSTRAINT `product_hierarchies_ibfk_1` FOREIGN KEY (`K_Product_Parent`) REFERENCES `products` (`K_Product`),
    CONSTRAINT `product_hierarchies_ibfk_2` FOREIGN KEY (`K_Product_Child`) REFERENCES `products` (`K_Product`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `product_hierarchies` WRITE;
INSERT INTO `product_hierarchies` VALUES ('1', 'P100', 'P10'), ('2', 'P100', 'P11'), ('3', 'P10', 'P1'), ('4', 'P14', 'P1'), ('5', 'P100', 'P12'), ('6', 'P100', 'P13'), ('7', 'P100', 'P14'), ('8', 'P11', 'P2'), ('9', 'P13', 'P3'), ('10', 'P13', 'P4'), ('11', 'P12', 'P4'), ('12', 'P12', 'P5');
UNLOCK TABLES;