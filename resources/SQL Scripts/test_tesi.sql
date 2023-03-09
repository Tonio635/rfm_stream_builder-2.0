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