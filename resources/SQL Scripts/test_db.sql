DROP DATABASE IF EXISTS `test`;
CREATE DATABASE `test`;
DROP TABLE IF EXISTS `receipts`;

CREATE TABLE `receipts` (
  `K_Receipt` varchar(100) NOT NULL,
  `K_Member` varchar(100) NOT NULL,
  `Quantity` int DEFAULT NULL,
  `Q_Amount` decimal(20,2) DEFAULT NULL,
  `Q_Discount_Amount` int DEFAULT NULL,
  `T_Receipt` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`K_Receipt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `receipts` WRITE;
INSERT INTO `receipts` VALUES ('1','Andrea',15,72.00,NULL,'2022-01-01 00:00:00'),('10','Marco',15,87.00,NULL,'2022-01-06 03:00:00'),('11','Marco',6,93.00,NULL,'2022-01-06 04:00:00'),('12','Marco',1,66.00,NULL,'2022-01-06 09:00:00'),('13','Marco',9,58.00,NULL,'2022-01-06 14:00:00'),('14','Andrea',8,97.00,NULL,'2022-01-07 01:00:00'),('15','Francesco',6,85.00,NULL,'2022-01-07 02:00:00'),('16','Andrea',5,68.00,NULL,'2022-01-07 04:00:00'),('17','Marco',6,92.00,NULL,'2022-01-07 07:00:00'),('18','Francesco',14,91.00,NULL,'2022-01-08 09:00:00'),('19','Andrea',7,96.00,NULL,'2022-01-09 12:00:00'),('2','Francesco',7,59.00,NULL,'2022-01-01 07:00:00'),('20','Francesco',3,68.00,NULL,'2022-01-09 16:00:00'),('21','Francesco',12,72.00,NULL,'2022-01-09 21:00:00'),('22','Andrea',6,73.00,NULL,'2022-01-10 08:00:00'),('23','Marco',15,65.00,NULL,'2022-01-10 09:00:00'),('24','Andrea',2,99.00,NULL,'2022-01-10 10:00:00'),('25','Andrea',1,88.00,NULL,'2022-01-10 11:00:00'),('26','Francesco',4,93.00,NULL,'2022-01-11 11:30:00'),('27','Andrea',15,72.00,NULL,'2022-01-11 13:00:00'),('28','Francesco',5,65.00,NULL,'2022-01-12 04:00:00'),('29','Marco',4,99.00,NULL,'2022-01-12 06:00:00'),('3','Francesco',7,62.00,NULL,'2022-01-01 23:00:00'),('30','Marco',15,66.00,NULL,'2022-01-12 11:00:00'),('31','Marco',4,78.00,NULL,'2022-01-12 17:00:00'),('32','Marco',12,67.00,NULL,'2022-01-12 19:00:00'),('33','Francesco',1,99.00,NULL,'2022-01-12 22:00:00'),('34','Francesco',12,52.00,NULL,'2022-01-13 00:00:00'),('35','Andrea',14,88.00,NULL,'2022-01-13 01:00:00'),('36','Andrea',3,86.00,NULL,'2022-01-13 02:00:00'),('37','Marco',4,74.00,NULL,'2022-01-14 03:00:00'),('38','Andrea',15,71.00,NULL,'2022-01-14 04:00:00'),('39','Andrea',5,77.00,NULL,'2022-01-14 05:00:00'),('4','Andrea',10,97.00,NULL,'2022-01-02 00:00:00'),('40','Andrea',10,72.00,NULL,'2022-01-15 07:00:00'),('41','Francesco',8,78.00,NULL,'2022-01-15 08:00:00'),('42','Francesco',10,71.00,NULL,'2022-01-15 09:00:00'),('43','Fabrizio',2,56.00,2,'2022-01-17 02:00:00'),('5','Marco',10,80.00,NULL,'2022-01-02 09:00:00'),('6','Andrea',5,77.00,NULL,'2022-01-02 23:00:00'),('7','Marco',14,85.00,NULL,'2022-01-03 00:00:00'),('8','Fabrizio',2,56.00,2,'2022-01-08 02:00:00'),('9','Marco',3,80.00,NULL,'2022-01-06 02:00:00');
UNLOCK TABLES;