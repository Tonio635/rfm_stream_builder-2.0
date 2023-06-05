DROP DATABASE IF EXISTS `test_vertwo`;
CREATE DATABASE `test_vertwo`;

USE `test_vertwo`;

DROP TABLE IF EXISTS `product_types`;

CREATE TABLE `product_types` (
  `K_Product_Type` varchar(100) NOT NULL,
  `N_Level` int DEFAULT NULL,
  PRIMARY KEY (`K_Product_Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `product_types` WRITE;
INSERT INTO `product_types` VALUES ('mobili_da_sala', 3), ('segnaletica_e_sicurezza', 3), ('aria_condizionata', 3), ('console_giochi', 3), ('SALA_E_GIARDINO', 2), ('SICUREZZA', 2), ('ARREDAMENTO', 2), ('CASA_E_GIARDINO', 2), ('RADICE', 1);
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
INSERT INTO `products` VALUES ('P1', 'mobili_da_sala'), ('P2', 'segnaletica_e_sicurezza'), ('P3', 'aria_condizionata'), ('P4', 'console_giochi'), ('P10', 'SALA_E_GIARDINO'), ('P11', 'SICUREZZA'), ('P12', 'ARREDAMENTO'), ('P13', 'CASA_E_GIARDINO'), ('P14', 'ARREDAMENTO'), ('P100', 'RADICE');
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
INSERT INTO `product_hierarchies` VALUES ('1', 'P100', 'P10'), ('2', 'P100', 'P11'), ('3', 'P10', 'P1'), ('4', 'P14', 'P1'), ('5', 'P100', 'P12'), ('6', 'P100', 'P13'), ('7', 'P100', 'P14'), ('8', 'P11', 'P2'), ('9', 'P13', 'P3'), ('10', 'P13', 'P4');
UNLOCK TABLES;

/*DROP TABLE IF EXISTS `receipt_lines`;

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
INSERT INTO `receipt_lines` VALUES (1,'1','4244733e06e7ecb4970a6e2683c13e61',1,58.90,NULL),(2,'2','e5f2d52b802189ee658865ca93d83a8f',1,239.90,NULL),(3,'3','c777355d18b72b67abbeef9df44fd0fd',1,199.00,NULL),(4,'4','7634da152a4610f1595efa32f14722fc',1,12.99,NULL),(5,'5','ac6c3623068f30de03045865e4e10089',1,199.90,NULL),(6,'6','ef92defde845ab8450f9d70c526ef70f',1,21.90,NULL),(7,'7','8d4f2bb7e93e6710a28f34fa83ee7d28',1,19.90,NULL),(8,'8','557d850972a7d6f792fd18ae1400d9b6',1,810.00,NULL),(9,'9','310ae3c140ff94b03219ad0adc3c778f',1,145.95,NULL),(10,'10','4535b0e1091c278dfd193e5a1d63b39f',1,53.99,NULL),(11,'11','d63c1011f49d98b976c352955b1c4bea',1,59.99,NULL),(12,'12','f177554ea93259a5b282f24e33f65ab6',1,45.00,NULL),(13,'13','99a4788cb24856965c36a24e339b6058',1,74.00,NULL),(14,'14','368c6c730842d78016ad823897a372db',1,99.80,NULL),(15,'15','368c6c730842d78016ad823897a372db',1,99.80,NULL),(16,'16','8cab8abac59158715e0d70a36c807415',1,99.90,NULL),(17,'17','3f27ac8e699df3d300ec4a5d8c5cf0b2',1,639.00,NULL),(18,'18','4fa33915031a8cde03dd0d3e8fb27f01',1,144.00,NULL),(19,'19','b50c950aba0dcead2c48032a690ce817',1,99.00,NULL),(20,'20','5ed9eaf534f6936b51d0b6c5e4d5c2e9',1,25.00,NULL),(21,'21','553e0e7590d3116a072507a3635d2877',1,47.90,NULL),(22,'22','57d79905de06d8897872c551bfd09358',1,21.99,NULL),(23,'23','1c05e0964302b6cf68ca0d15f326c6ba',1,119.99,NULL),(24,'24','5d7c23067ed3fc8c6e699b9373d5890b',1,49.00,NULL),(25,'25','5a419dbf24a8c9718fe522b81c69f61a',1,48.90,NULL),(26,'26','21b1c2f67a9aafb5af0eb06c13b9dbda',1,219.90,NULL),(27,'27','c389f712c4b4510bc997cee93e8b1a28',1,289.00,NULL),(28,'28','1c0c0093a48f13ba70d0c6b0a9157cb7',1,109.90,NULL),(29,'29','89321f94e35fc6d7903d36f74e351d40',1,27.90,NULL),(30,'30','38afdf723b95d455b418a0f57d623c6b',1,119.90,NULL),(31,'31','672e757f331900b9deea127a2a7b79fd',1,397.00,NULL),(32,'32','28b4eced95a52d9c437a4caf9d311b95',1,59.90,NULL),(33,'33','e95ee6822b66ac6058e2e4aff656071a',1,63.99,NULL),(34,'34','e95ee6822b66ac6058e2e4aff656071a',1,63.99,NULL),(35,'35','e95ee6822b66ac6058e2e4aff656071a',1,63.99,NULL),(36,'36','23365beed316535b4105bd800c46670e',1,16.50,NULL),(37,'37','50fd2b788dc166edd20512370dac54df',1,21.90,NULL),(38,'38','b10eba910a974df70b8a12d0665cdb9e',1,39.00,NULL),(39,'39','4089861a1bd4685da70bddd6b4f974f1',1,49.75,NULL),(40,'40','fe59a1e006df3ac42bf0ceb876d70969',1,809.10,NULL),(41,'41','c6dd917a0be2a704582055949915ab32',1,99.99,NULL),(42,'42','28b4eced95a52d9c437a4caf9d311b95',1,59.90,NULL),(43,'43','0b0172eb0fd18479d29c3bc122c058c2',1,74.67,NULL),(44,'1','0b0172eb0fd18479d29c3bc122c058c2',1,74.67,NULL),(45,'2','0b0172eb0fd18479d29c3bc122c058c2',1,74.67,NULL),(46,'3','dbaee28f4ee64465838a229582d77520',1,54.00,NULL),(47,'4','dbb67791e405873b259e4656bf971246',1,81.99,NULL),(48,'5','84f456958365164420cfc80fbe4c7fab',1,99.00,NULL),(49,'6','e67307ff0f15ade43fcb6e670be7a74c',1,37.98,NULL),(50,'7','e67307ff0f15ade43fcb6e670be7a74c',1,37.98,NULL),(51,'8','30c01cc81c9eb80469371743813789cc',1,38.33,NULL),(52,'9','777d2e438a1b645f3aec9bd57e92672c',1,69.90,NULL),(53,'10','884fa3cd42986ba480ea2f8ae4e25ff7',1,195.00,NULL),(54,'11','bdcf6a834e8faa30dac3886c7a58e92e',1,35.90,NULL),(55,'12','a5341e3f8155dbb3e62323d3ea289729',1,79.50,NULL),(56,'13','e19ddcc85537b41f22116c8d5425ef46',1,29.99,NULL),(57,'14','e6b6e13cf71449a457269f425b89dc74',1,109.90,NULL),(58,'1','13fcfc313dfb2217e5ee3000a702f9ef',1,74.90,NULL),(59,'2','4e3f399366b0047a572b6682f9bb166e',1,14.95,NULL);
UNLOCK TABLES;*/