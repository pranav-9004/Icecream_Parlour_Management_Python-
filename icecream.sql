-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: icecream
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `custid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  PRIMARY KEY (`custid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('1621','Unmesh_Shelar','9834782961'),('1656','Swati_Sarkale','8329804636'),('3921','Harry_Potter','7219734878'),('4159','Alia_Bhatt','1324357912'),('4235','Ash_Ketchum','9723712961'),('4310','Rohit_Raval','8080154271'),('5288','Anthony_Bridgerton','9014780745'),('7415','Dhanu_Chavat','3692581470'),('7751','Om_Mavale','9975374769'),('7752','Daphne_Bridgerton','6789023456'),('7909','Pravin_Sarkale','1234567890'),('9279','Misty_Ketchum','7720046336');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `icregister`
--

DROP TABLE IF EXISTS `icregister`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `icregister` (
  `firname` varchar(100) DEFAULT NULL,
  `laname` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `securityQ` varchar(100) DEFAULT NULL,
  `securityA` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `icregister`
--

LOCK TABLES `icregister` WRITE;
/*!40000 ALTER TABLE `icregister` DISABLE KEYS */;
INSERT INTO `icregister` VALUES ('Jayesh','Kawade','9834782961','jayesh@gmail.com','Favourite Cousin','Pranav','jayesh123'),('Kate','Bridgerton','1029384756','kate@gmail.com','Your Birth Place','Mumbai','kate123'),('Om','Kharote','9922191980','omkharote7@gmail.com','Your Birth Place','Wai','om123'),('Pranav','Sarkale','7219734878','pranav22sarkale@gmail.com','Your Birth Place','Pune','pranav123'),('Urvi','Kulkarni','9087654321','urvi@gmail.com','Father\'s Name','Prakash','urvi123');
/*!40000 ALTER TABLE `icregister` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report` (
  `billid` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `flavour` varchar(100) DEFAULT NULL,
  `quan` int DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
INSERT INTO `report` VALUES ('5102','7720046336','Misty_Ketchum','5/18/22','Strawberry',1,'Rs.50.00'),('5102','7720046336','Misty_Ketchum','5/18/22','SweetVanilla',1,'Rs.80.50'),('5774','9834782961','Unmesh_Shelar','5/16/22','BlackCurrent',1,'Rs.60.00'),('5774','9834782961','Unmesh_Shelar','5/16/22','Chocolate',1,'Rs.100.60'),('5774','9834782961','Unmesh_Shelar','5/16/22','SaltedCaremal',1,'Rs.151.00'),('5065','8329804636','Swati_Sarkale','5/15/22','Watermelon',1,'Rs.50.00'),('5065','8329804636','Swati_Sarkale','5/15/22','Butterscotch',1,'Rs.95.50'),('5065','8329804636','Swati_Sarkale','5/15/22','KesharPista',1,'Rs.125.95'),('5065','8329804636','Swati_Sarkale','5/15/22','JuicyPineapple',1,'Rs.161.25'),('5065','8329804636','Swati_Sarkale','5/15/22','CookiesAndCream',1,'Rs.231.60'),('5065','8329804636','Swati_Sarkale','5/15/22','Chocolate',4,'Rs.393.50'),('9110','7219734878','Harry_Potter','5/14/22','KesharPista',1,'Rs.30.00'),('9110','7219734878','Harry_Potter','5/14/22','BlackCurrent',4,'Rs.272.10'),('9110','7219734878','Harry_Potter','5/14/22','Rasberry',3,'Rs.438.80'),('9110','7219734878','Harry_Potter','5/14/22','JuicyPineapple',1,'Rs.474.35'),('9110','7219734878','Harry_Potter','5/14/22','DarkChocolate',5,'Rs.777.10'),('9110','7219734878','Harry_Potter','5/14/22','WateryCoconut',3,'Rs.989.10'),('3275','1324357912','Alia_Bhatt','5/8/22','Rasberry',7,'Rs.388.30'),('3275','1324357912','Alia_Bhatt','5/8/22','SweetVanilla',4,'Rs.509.75'),('3275','1324357912','Alia_Bhatt','5/8/22','RedGulkhand',5,'Rs.812.45'),('3275','1324357912','Alia_Bhatt','5/8/22','CrashewNut',5,'Rs.1065.05'),('3275','1324357912','Alia_Bhatt','5/8/22','RawMango',2,'Rs.1166.05'),('3275','1324357912','Alia_Bhatt','5/8/22','JuicyPineapple',1,'Rs.1201.55'),('9051','8080154271','Rohit_Raval','5/5/22','ChocoChipNut',5,'Rs.352.80'),('9051','8080154271','Rohit_Raval','5/5/22','BlackCurrent',6,'Rs.716.50'),('9051','8080154271','Rohit_Raval','5/5/22','CandiedPapaya',4,'Rs.918.60'),('9051','8080154271','Rohit_Raval','5/5/22','SaltedCaremal',6,'Rs.1221.60'),('8557','1029384756','Tejal_Rathi','5/10/22','Rasberry',7,'Rs.388.30'),('8557','1029384756','Tejal_Rathi','5/10/22','SweetVanilla',8,'Rs.630.95'),('8557','1029384756','Tejal_Rathi','5/10/22','CandiedPapaya',3,'Rs.782.25'),('8557','1029384756','Tejal_Rathi','5/10/22','JuicyPineapple',6,'Rs.994.50'),('8557','1029384756','Tejal_Rathi','5/10/22','WateryCoconut',8,'Rs.1559.75'),('1454','9975374769','Om_Mavale','5/21/22','BlackCurrent',2,'Rs.120.60'),('1454','9975374769','Om_Mavale','5/21/22','Butterscotch',7,'Rs.438.90'),('1454','9975374769','Om_Mavale','5/21/22','SaltedCaremal',2,'Rs.539.85'),('1454','9975374769','Om_Mavale','5/21/22','SaltedCaremal',4,'Rs.741.85'),('6618','9975374769','Om_Mavale','5/21/22','SweetVanilla',4,'Rs.863.25'),('6524','9975374769','Om_Mavale','5/21/22','Watermelon',3,'Rs.151.00'),('6524','9975374769','Om_Mavale','5/21/22','JuicyPineapple',6,'Rs.363.25'),('3351','9975374769','Om_Mavale','5/21/22','KesharPista',3,'Rs.151.00'),('3351','9975374769','Om_Mavale','5/21/22','SweetVanilla',4,'Rs.272.40'),('3351','9975374769','Om_Mavale','5/21/22','Butterscotch',3,'Rs.408.60'),('8921','9087654321','Karan_Shinde','5/22/22','HoneyDate',2,'Rs.120.60'),('8921','9087654321','Karan_Shinde','5/22/22','DarkChocolate',1,'Rs.181.20'),('8921','9087654321','Karan_Shinde','5/22/22','ColdCoffe',2,'Rs.312.45'),('8921','9087654321','Karan_Shinde','5/22/22','KesharPista',1,'Rs.363.10'),('8921','9087654321','Karan_Shinde','5/22/22','RawMango',1,'Rs.413.60'),('2980','8080154271','Rohit_Raval','5/23/22','ChocoBrownie',1,'Rs.55.00'),('2980','8080154271','Rohit_Raval','5/23/22','BlackCurrent',9,'Rs.600.35'),('5724','3692581470','Dhanu_Chavat','6/2/22','ChocoBrownie',8,'Rs.443.85'),('5724','3692581470','Dhanu_Chavat','6/2/22','SweetVanilla',3,'Rs.535.00'),('5724','3692581470','Dhanu_Chavat','6/2/22','Butterscotch',1,'Rs.580.30'),('3465','7219734878','Harry_Potter','7/11/22','Butterscotch',1,'Rs.45.00'),('3465','7219734878','Harry_Potter','7/11/22','ChocoBrownie',6,'Rs.378.20'),('7643','8329804636','Swati_Sarkale','7/11/22','BlackCurrent',1,'Rs.60.00'),('7643','8329804636','Swati_Sarkale','7/11/22','ChocoChipNut',1,'Rs.130.60'),('7643','8329804636','Swati_Sarkale','7/11/22','CookiesAndCream',1,'Rs.201.30'),('7787','7219734878','Harry_Potter','7/11/22','KesharPista',1,'Rs.50.00'),('1307','7219734878','Harry_Potter','7/11/22','Rasberry',1,'Rs.105.50'),('6879','9975374769','Om_Mavale','7/11/22','BlackCurrent',6,'Rs.363.00'),('6879','9975374769','Om_Mavale','7/11/22','Butterscotch',7,'Rs.681.30'),('6879','9975374769','Om_Mavale','7/11/22','SweetVanilla',7,'Rs.893.55'),('7303','9087654321','Rohan_Nanda','7/12/22','BlackCurrent',1,'Rs.60.00'),('7303','9087654321','Rohan_Nanda','7/12/22','ChocoChipNut',1,'Rs.130.60'),('7303','9087654321','Rohan_Nanda','7/12/22','Watermelon',7,'Rs.484.30'),('7303','9087654321','Rohan_Nanda','7/12/22','Butterscotch',3,'Rs.620.70'),('8617','8421459209','Purva_Sarkale','7/12/22','ChocoChipNut',2,'Rs.140.70'),('8617','8421459209','Purva_Sarkale','7/12/22','KesharPista',3,'Rs.292.40'),('8617','8421459209','Purva_Sarkale','7/12/22','Butterscotch',2,'Rs.383.35'),('4380','9014780745','Anthony_Bridgerton','7/13/22','Butterscotch',3,'Rs.135.90'),('4380','9014780745','Anthony_Bridgerton','7/13/22','ChocoBrownie',2,'Rs.246.90'),('4380','9014780745','Anthony_Bridgerton','7/13/22','SweetVanilla',3,'Rs.338.05'),('4380','9014780745','Anthony_Bridgerton','7/13/22','CookiesAndCream',2,'Rs.479.05'),('4380','9014780745','Anthony_Bridgerton','7/13/22','ColdChocoCoffe',5,'Rs.807.35'),('4380','9014780745','Anthony_Bridgerton','7/13/22','DarkChocolate',2,'Rs.928.60'),('7846','6789023456','Daphne_Bridgerton','7/13/22','SweetVanilla',4,'Rs.120.90'),('7846','6789023456','Daphne_Bridgerton','7/13/22','ChocoChipNut',4,'Rs.403.30'),('7846','6789023456','Daphne_Bridgerton','7/13/22','HoneyDate',5,'Rs.706.40'),('7846','6789023456','Daphne_Bridgerton','7/13/22','DarkChocolate',3,'Rs.888.20'),('7846','6789023456','Daphne_Bridgerton','7/13/22','SaltedCaremal',3,'Rs.1039.80'),('1702','9014780745','Anthony_Bridgerton','7/14/22','ChocoChipNut',1,'Rs.70.00'),('1702','9014780745','Anthony_Bridgerton','7/14/22','HoneyDate',2,'Rs.191.30'),('1702','9014780745','Anthony_Bridgerton','7/14/22','ColdChocoCoffe',3,'Rs.388.20'),('1702','9014780745','Anthony_Bridgerton','7/14/22','WateryCoconut',4,'Rs.670.95'),('1702','9014780745','Anthony_Bridgerton','7/14/22','CrashewNut',5,'Rs.923.65'),('7391','9014780745','Anthony_Bridgerton','7/14/22','Coffee',10,'Rs.655.85'),('1809','9014780745','Anthony_Bridgerton','7/14/22','CoffeeNut',1,'Rs.65.00'),('1672','7219734878','Harry_Potter','7/14/22','ChocoBrownie',2,'Rs.110.55'),('1672','7219734878','Harry_Potter','7/14/22','ChocoChipNut',1,'Rs.181.10'),('1672','7219734878','Harry_Potter','7/14/22','CookiesAndCream',3,'Rs.393.20');
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock` (
  `id` varchar(100) NOT NULL,
  `flavour` varchar(100) NOT NULL,
  `wt` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
INSERT INTO `stock` VALUES ('1087','Pistachio',10,35),('1420','Rasberry',10,55),('2628','Strawberry',20,50),('2929','ChocoBrownie',5,55),('3643','Watermelon',10,50),('3976','KesharPista',30,50),('4193','BlackCurrent',10,60),('5186','SweetVanilla',20,30),('5231','ChocoChipNut',10,70),('5263','Butterscotch',5,45),('5706','RawMango',10,50),('5963','Chocolate',30,40),('6559','SaltedCaremal',10,50),('6602','DarkChocolate',20,60),('6887','Blueberry',10,60),('6919','CoffeeNut',10,65),('7203','CookiesAndCream',10,70),('7785','CandiedPapaya',10,50),('7885','HoneyDate',5,60),('8066','JuicyPineapple',5,35),('8804','WateryCoconut',10,70),('9348','RedGulkhand',10,60),('9447','CrashewNut',20,50);
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-16 23:24:01
