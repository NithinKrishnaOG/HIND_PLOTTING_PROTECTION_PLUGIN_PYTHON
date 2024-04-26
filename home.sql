/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.36-log : Database - home
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`home` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `home`;

/*Table structure for table `bill` */

DROP TABLE IF EXISTS `bill`;

CREATE TABLE `bill` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `tamt` int(20) NOT NULL,
  `downp` int(10) NOT NULL,
  `bal` int(10) NOT NULL,
  `mp` int(10) NOT NULL,
  `duration` int(20) NOT NULL,
  `bda` varchar(20) NOT NULL,
  `fr` varchar(20) NOT NULL,
  `wto` varchar(20) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `bill` */

insert  into `bill`(`bid`,`name`,`email`,`tamt`,`downp`,`bal`,`mp`,`duration`,`bda`,`fr`,`wto`) values (1,'grgrg','qwe@gmail.com',233333,3222,0,0,0,'','',''),(2,'rrrrrrrrrrrr','rtr@gmail.com',3444444,2147483647,222222222,12244,0,'','',''),(3,'gggg','qwe@gmail.com',343444,454545,45454,454545,0,'12/10/2016','',''),(4,'gfffffffffffffffff','fgfgfgfg@gmail.com',687687868,88989898,89898989,89898989,0,'12/10/2016','14/87/90090',''),(5,'eeer','qwe@gmail.com',343434,3433,34343,43343,0,'12/10/2016','14/87/90090','21/10/2010'),(6,'priya','priya321@gmail.com',44565455,12000,41444,1250,0,'12/10/2017','12/10/2017','12/10/2019'),(7,'priya','priya321@gmail.com',18000,1000,17000,3000,0,'12/10/2017','12/10/2017','12/10/2019'),(8,'rizana','rizana123@gmail.com',48000,20000,28000,2000,7,'12/10/2017','12/10/2017','12/10/2019');

/*Table structure for table `cartdetails` */

DROP TABLE IF EXISTS `cartdetails`;

CREATE TABLE `cartdetails` (
  `ser_no` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(200) NOT NULL,
  `image1` varchar(200) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `price` varchar(200) NOT NULL,
  PRIMARY KEY (`ser_no`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `cartdetails` */

insert  into `cartdetails`(`ser_no`,`email`,`image1`,`product_name`,`price`) values (1,'rashmicsjm5@gmail.com','m1.jpg','HP Laptop','5000');

/*Table structure for table `contact` */

DROP TABLE IF EXISTS `contact`;

CREATE TABLE `contact` (
  `S.no` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(200) NOT NULL,
  `address` varchar(5000) NOT NULL,
  `phone_no` varchar(200) NOT NULL,
  `mobile_no` varchar(200) NOT NULL,
  `email_id` varchar(200) NOT NULL,
  PRIMARY KEY (`S.no`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `contact` */

insert  into `contact`(`S.no`,`company_name`,`address`,`phone_no`,`mobile_no`,`email_id`) values (1,'Himanshu Electronics & Communitation ','','45455455','q44234','');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mnum` int(12) NOT NULL,
  `msgg` varchar(100) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`name`,`email`,`mnum`,`msgg`) values (1,'dfdfdf','ass@gmail.com',2147483647,'fffffffffffffdddddddddddddddddddddddd'),(2,'priya','priya321@gmail.com',98556559,'ddfdfddfd');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `ser_no` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`ser_no`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`ser_no`,`user_name`,`password`) values (1,'admin','admin');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `id` int(30) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `pay_type` varchar(40) NOT NULL,
  `tamount` int(50) NOT NULL,
  `downp` int(40) NOT NULL,
  `balance` int(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`id`,`name`,`pay_type`,`tamount`,`downp`,`balance`) values (1,'priya','otp',20000,2000,18000),(2,'priya','cashondelivery',48000,2000,46000),(3,'priya','otp',18000,1000,17000);

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `ser_no` int(11) NOT NULL AUTO_INCREMENT,
  `product_code` varchar(200) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `pro_cat` varchar(200) NOT NULL,
  `product_price` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `brand` varchar(200) NOT NULL,
  `category` varchar(200) NOT NULL,
  `features` varchar(200) NOT NULL,
  `plateform` varchar(200) NOT NULL,
  `model` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL,
  `display` varchar(200) NOT NULL,
  `waranty` varchar(200) NOT NULL,
  `shipping_time` varchar(300) NOT NULL,
  `price` varchar(100) NOT NULL,
  `offer_price` varchar(100) NOT NULL,
  `save` varchar(200) NOT NULL,
  `image1` varchar(200) NOT NULL,
  PRIMARY KEY (`ser_no`)
) ENGINE=MyISAM AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`ser_no`,`product_code`,`product_name`,`pro_cat`,`product_price`,`description`,`brand`,`category`,`features`,`plateform`,`model`,`type`,`display`,`waranty`,`shipping_time`,`price`,`offer_price`,`save`,`image1`) values (26,'SNTVE1','Samsung SNTVE1','tv','6500','Samsung tv','Samsung','T.V','21 ','Samsung','Samsung','LED TV','Samsung','1 year warranty ','within 5-7 working days','6500','5500','500','tv1.png'),(4,'SNMO2','LG-L5II- E450SNMO2','mobile','9573','Sales Package Handset, USB Cable, Charger, Battery','LG','LG','LG','Primary Camera 5 MP, Secondary Camera 1.2 MP','Internal Memory Capacity 16 GB','LG','Display Type LED','1 year warranty ','within 15-20 working days','9573','9000','573','m2.png'),(5,'SNMO3','Samsung-GalaxySNMO3','mobile','30999','Sales Package Handset, USB Cable, Charger, Battery','Samsung ','Samsung-Galaxy','Samsung-Galaxy','Samsung-Galaxy','Samsung-Galaxy','Samsung-Galaxy','Samsung-Galaxy','2 years','within 15-20 working days','30999','30000','999','m3.png'),(6,' SNMO4','Nokia-301 SNMO4','mobile','5129','Sales Package Handset, USB Cable, Charger, Battery','Nokia','Nokia','single sim','Nokia','Nokia-301','Nokia','Nokia','1 year warranty ','within 15-20 working days','5129','5000','129','m4.png'),(7,'SNCAMERA1','CANON SNCAMERA1','camera','10000','CANON ','CANON ','CANON ','CANON ','CANON ','CANON ','CANON ','CANON ','1 year warranty ','within 5-7 working days','10000','9000','1000','camera1.png'),(8,'SNCAMERA2','SONY SNCAMERA1','camera','15000','SONY','SONY','SONY','SONY','SONY','SONY','LED ','Display Type LED','1 years','20-25 dayd','15000','12000','3000','camera2.png'),(11,'SNCAMERA3','SAMSUNG SNCAMERA3','camera','8000','SAMSUNG','samsung','SAMSUNG','SAMSUNG','SAMSUNG','SAMSUNG','LED ','Display Type LED','1 year','within 10-15 days','8000','7500','500','camera3.png'),(12,'SNCAMERA4','NIKON SNCAMERA4','camera','11000','NIKON','NIKON','NIKON','NIKON','NIKON','NIKON','LED ','Display Type LED','2 year','within 20 days','11000','10000','1000','camera4.png'),(15,'SNM1','SONYMUSIC1','music','39000','SONYMUSIC','SONYMUSIC','SONYMUSIC','SONYMUSIC','SONYMUSIC','SONYMUSIC','Home Theater','Display Type LED','1 year warranty ','within 15-20 working days','39000','35000','4000','music1.png'),(16,'SNM2','LGMUSIC2','music','30000','LGMUSIC','LGMUSIC','LGMUSIC','LGMUSIC','LGMUSIC','LGMUSIC','LGMUSIC','LGMUSIC','2 years','within 21 days','30000','28000','2000','music2.png'),(17,'SNM3','PANASONIC SNM3','music','28000','PANASONIC ','PANASONIC ','PANASONIC ','PANASONIC ','PANASONIC ','PANASONIC ','Home Theater','PANASONIC ','2 years','20 days','28000','27000','1000','music3.png'),(18,'SNM4','SAMSUNGMUSIC4','music','25000','SAMSUNG','SAMSUNG','SAMSUNG','SAMSUNG','SAMSUNG','SAMSUNG','SAMSUNG','SAMSUNG','5 year','15-20 days','25000','24000','1000','music4.png'),(20,'SNTVE2','SONYSNTVE2','tv','11000','Sales Package Handset, USB Cable, Charger, Battery','SONY','SONY','Processor A6X Dual Core','SONY','SONY','LED ','Display Type LED','5 years','20 days','11000','10500','500','tv2.png'),(21,'SNTVE3','VideoconSNTVE3','tv','20000','Videocon','Videocon','Videocon','Videocon','Videocon','Videocon','LED TV','Display Type LED','1 year warranty ','within 15-20 working days','20000','18000','2000','tv3.png'),(22,'SNTVE4','ONIDASNTVE4','tv','25000','ONIDA','ONIDA','ONIDA','ONIDA','ONIDA','ONIDA','LED ','Display Type LED','1 year warranty','within 30 days','25000','24000','1000','tv4.png'),(23,'SNTVE5','LGSNTVE5','tv','28000','LG','LG','LG','LG','LG','LG','LED TV','Display Type LED','2 years','15 days','28000','26000','2000','tv6.png'),(24,'SNTVE6','PhilipsSNTVE6','tv','20000','Philips','Philips','Philips','Philips','Philips','Philips','LED TV','Display Type LED','2 years ','20 days','20000','19000','1000','tv5.png'),(27,'SNL1','SONY LAPTOP','laptop','40000',' USB Cable, Charger, Battery','SONY','SONY LAPTOP','SONY LAPTOP','SONY LAPTOP','SONY LAPTOP','SONY LAPTOP','Display Type LED','1 year warranty ','within 15-20 working days','40000','38000','2000','laptop3.png'),(28,'SNL2','LENOVO Laptop','laptop','36000','LENOVO Laptop','LENOVO','LENOVO Laptop','LENOVO Laptop','LENOVO Laptop','LENOVO Laptop','LED TV','Display Type LED','1 year warranty ','within 15-20 working days','36000','35000','1000','laptop2.png'),(29,' PSP-1004E BL','SONY PLAY STATION PSP-1004E BL','game','10000','dsfrsetfgrdgtrdhtyh','sony','iPads ','gftgh','ghfth','ghftrhytuh','LED ','Display Type LED','1 year warranty ','within 15-20 working days','10000','9000','1000','game1.jpeg'),(30,' PSP-1004E WH','SONY PLAY STATION PSP-1004E WH','game','6000','dsfrsetfgrdgtrdhtyh','sony','GFRDTG','gftgh','ghfth','Internal Memory Capacity 16 GB','LED TV','hjkuhk','1 year warranty ','within 5-7 working days','6000','5200','800','game2.jpg'),(31,' PS2 DUAL PAC','SONY PLAY STATION PS2 DUAL PAC','game','12000','dsfrsetfgrdgtrdhtyh','sony','rtgrg','tygty','ygtyt','ytygr','htyhutf','tyhtfyh','1 year warranty ','within 15-20 working days','12000','10000','2000','game3.jpg'),(32,'SNTVE9','samsung SNTVE9','tv','20000','dsfrsetfgrdgtrdhtyh','samsung','iPads & Tablets','gftgh','ghfth','Internal Memory Capacity 16 GB','LED TV','Display Type LED','1 year warranty ','within 15-20 working days','20000','18000','2000','tv8.png'),(33,'MICRO A075','CANON SNCAMERA1','mobile','8000','2G Android Dual Core Phablet','Micromax','Micromax','8 MP With Video Recording,Front 0.3 MP Digital Camera5.2 Inch (13.20 c) Screen Size,Android 4.0.3 ICS Operating System','Android','A075','LED ','Display Type LED','1 year','within 5-7 working days','8000','6000','2010','m5.png');

/*Table structure for table `shopping_cart` */

DROP TABLE IF EXISTS `shopping_cart`;

CREATE TABLE `shopping_cart` (
  `ser_no` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(500) NOT NULL,
  `product_code` varchar(200) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `image1` varchar(500) NOT NULL,
  `quantity` varchar(200) NOT NULL,
  `price` varchar(200) NOT NULL,
  `txn_status` varchar(255) NOT NULL,
  PRIMARY KEY (`ser_no`)
) ENGINE=MyISAM AUTO_INCREMENT=133 DEFAULT CHARSET=latin1;

/*Data for the table `shopping_cart` */

insert  into `shopping_cart`(`ser_no`,`email`,`product_code`,`product_name`,`image1`,`quantity`,`price`,`txn_status`) values (105,'r@gmail.com','SNTVE1','Samsung SNTVE1','tv1.png','1','5500',''),(5,'rashmi@gmail.com','$code','Nokia SNTV3','m3.png','3','6000',''),(14,'rashmi@gmail.com','SNTVE2','philipsSNTVE2','tv3.png','1','',''),(64,'rashmicsjm5@gmail.com','SNM1','SONYMUSIC1','music1.png','1','35000',''),(21,'h@gmail.com','SNTVE2','philipsSNTVE2','tv3.png','1','',''),(70,'h@gmail.com','SNM2','LGMUSIC2','music2.png','1','28000',''),(67,'a@gmail.com','SNTVE2','SONYSNTVE2','tv2.png','1','10500',''),(125,'a@gmail.com','SNM3','PANASONIC SNM3','music3.png','1','27000',''),(68,'h@gmail.com','SNTVE1','Samsung SNTVE1','tv1.png','1','5500',''),(69,'h@gmail.com','SNTVE1','Samsung SNTVE1','tv1.png','1','5500',''),(95,'bsraazit@gmail.com','SNTVE2','SONYSNTVE2','tv2.png','1','10500',''),(89,'raj@gmail.com','SNCAMERA3','SAMSUNG SNCAMERA3','camera3.png','12','7500',''),(88,'raj@gmail.com','SNTVE3','VideoconSNTVE3','tv3.png','2','18000',''),(103,'rashmicsjm5@gmail.com','SNTVE4','ONIDASNTVE4','tv4.png','1','24000',''),(111,'amit@gmail.com','SNTVE3','VideoconSNTVE3','tv3.png','1','18000',''),(117,'anuj.lpu1@gmail.com','SNM1','SONYMUSIC1','music1.png','1','35000',''),(118,'anuj.lpu1@gmail.com','SNTVE2','SONYSNTVE2','tv2.png','1','10500',''),(120,'anuj.lpu1@gmail.com','SNM4','SAMSUNGMUSIC4','music4.png','1','24000',''),(121,'anuj.lpu1@gmail.com','SNTVE3','VideoconSNTVE3','tv3.png','2','18000',''),(122,'sree123@gmail.com',' SNMO4','Nokia-301 SNMO4','m4.png','1','5000',''),(123,'sree123@gmail.com','SNTVE3','VideoconSNTVE3','tv3.png','1','18000',''),(127,'priya321@gmail.com','SNTVE4','ONIDASNTVE4','tv4.png','2','24000',''),(128,'rizana123@gmail.com','SNTVE3','VideoconSNTVE3','tv3.png','2','18000',''),(130,'manish@gmail.com','SNTVE1','Samsung SNTVE1','tv1.png','1','5500',''),(131,'a@a.com','SNTVE1','Samsung SNTVE1','tv1.png','1','5500',''),(132,'a@a.com','MICRO A075','CANON SNCAMERA1','may-16-announcement-of-2014-election-results.png','1','6000','');

/*Table structure for table `static` */

DROP TABLE IF EXISTS `static`;

CREATE TABLE `static` (
  `static_id` int(11) NOT NULL AUTO_INCREMENT,
  `page` varchar(200) NOT NULL,
  `details` longtext NOT NULL,
  PRIMARY KEY (`static_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `static` */

insert  into `static`(`static_id`,`page`,`details`) values (1,'aboutus','\n<font style=\"font-family:Verdana, Geneva, sans-serif; color:#930;\">\n\n \n<font style=\"font-family:Verdana, Geneva, sans-serif; color:#930;\">\n\n <font style=\"font-family:Verdana, Geneva, sans-serif; color:#930;\">\n <font style=\"font-family: Verdana, Geneva, sans-serif;\">\n <div style=\"text-align: justify;\"><font face=\"times new roman\" color=\"#000033\"><b>Home Shopping - </b>in full bloom</font></div><div style=\"text-align: justify;\"><font face=\"times new roman\" color=\"#000033\"><br></font></div><div><font face=\"times new roman\"><div style=\"text-align: justify;\"><b style=\"color: rgb(0, 0, 51);\">Home Shopping</b><font color=\"#000033\">, holds the distinction of being the one-stop-destination for quality electronic Products in Central India. It offers an array of world-renowned brands like Apple, Sony, Samsung, LG, Philips, Nokia, Dell, Lenovo, Blackberry, Compaq, Nikon, Canon, Whirlpool, Hitachi etc. all under one roof.</font></div><div style=\"text-align: justify;\"><font color=\"#000033\"><br></font></div><div><div style=\"text-align: justify;\"><font color=\"#000033\">Online shopping - Great Brands, Great Value</font></div></div><div style=\"text-align: justify;\"><font color=\"#000033\"><br></font></div><div><div style=\"text-align: justify;\"><font color=\"#000033\">Apart from 9 mega showrooms in Delhi,&nbsp;</font><b style=\"color: rgb(0, 0, 51);\">HomeShopping</b><font color=\"#000033\">&nbsp;now boasts of a strong presence in the virtual world too. Its website&nbsp; facilitates safe &amp; convenient online shopping for the customers.&nbsp;</font></div></div><div><div style=\"text-align: justify;\"><font color=\"#000033\">There are many wonderful things that you can do on this website - Get acquainted with the vast number of brands available for each product. Get in-depth information about them, compare the options &amp; select the product of your choice. You can also chat online with our advisors - clear queries &amp; get expert guidance. Plus there are special schemes and offers for the customers. The buying process too is very easy &amp; convenient. Every purchase comes with an assurance of timely delivery, anywhere in India. The happiness does not fade away even after the purchase. The prompt after-sales service keeps the product and your smile intact - year after year.</font></div></div><div style=\"text-align: justify;\"><font color=\"#000033\"><br></font></div><div><div style=\"text-align: justify;\"><font color=\"#000033\">RishtaBehtarZindagi se: A way of life.</font></div></div><div style=\"text-align: justify;\"><font color=\"#000033\"><br></font></div><div><div style=\"text-align: justify;\"><font color=\"#000033\">A bond with a better life, this is the philosophy that we live by and it is reflected in each and every endeavor of the company.</font></div></div><div style=\"text-align: justify;\">&nbsp;</div></font></div></font>\n\n</font>\n\n</font>\n\n\n\n</font>\n\n\n\n'),(2,'contact','\n<font style=\"font-family:Verdana, Geneva, sans-serif; color:#930;\">\n\n <font style=\"font-family:Verdana, Geneva, sans-serif; color:#930;\">\n <font style=\"font-family:Verdana, Geneva, sans-serif; color:#930;\">\n <font style=\"font-family:Verdana, Geneva, sans-serif; color:#930;\">\n <font style=\"font-family:Verdana, Geneva, sans-serif; color:#930;\">\n <font style=\"font-family: Verdana, Geneva, sans-serif;\">\n <font style=\"font-family: Verdana, Geneva, sans-serif;\">\n <font style=\"font-family: Verdana, Geneva, sans-serif;\">\n <div><b>PHP Shopping</b></div><div><font face=\"Verdana, Geneva, sans-serif\" color=\"#000033\"><br></font></div><div><font face=\"Verdana, Geneva, sans-serif\" color=\"#000033\">&nbsp;Address : &nbsp; &nbsp; &nbsp;New Delhi</font></div><div><font face=\"Verdana, Geneva, sans-serif\" color=\"#000033\"><br></font></div><div><font face=\"Verdana, Geneva, sans-serif\" color=\"#000033\">&nbsp;Email-Id : &nbsp; &nbsp; shopping@gmail.com</font></div><div><font face=\"Verdana, Geneva, sans-serif\" color=\"#000033\"><br></font></div><div><font face=\"Verdana, Geneva, sans-serif\" color=\"#000033\">&nbsp;Contact No : &nbsp;+91-9120857868</font></div><div style=\"color: rgb(153, 51, 0);\"><font face=\"Verdana, Geneva, sans-serif\">&nbsp;</font></div></font>\n\n</font>\n\n</font>\n\n</font>\n\n</font>\n\n</font>\n\n</font>\n\n</font>\n\n\n\n'),(3,'Privacy&Policy',''),(4,'Terms&Condition','');

/*Table structure for table `txn_status` */

DROP TABLE IF EXISTS `txn_status`;

CREATE TABLE `txn_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `contact_no` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `txn_status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `txn_status` */

/*Table structure for table `user_details` */

DROP TABLE IF EXISTS `user_details`;

CREATE TABLE `user_details` (
  `ser_no` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `contact` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`ser_no`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `user_details` */

insert  into `user_details`(`ser_no`,`name`,`email`,`contact`,`password`) values (16,'rizana','rizana123@gmail.com','9566666665','rizana'),(4,'amit saini','amit@gmail.com','123456789','123'),(6,'Amit','a@gmail.com','123456789','12'),(7,'manish','manish@gmail.com','123456789','12'),(8,'himanshu','h@gmail.com','123456789','12345'),(9,'raj','raj@gmail.com','123456789','1234567890'),(10,'manisha','m@gmail.com','123456789','111'),(11,'naukri','m1@gmail.com','123456789','111'),(13,'demo','demouser@gmail.com','1234567891','php'),(14,'sreepriya','sree123@gmail.com','6536538956','sree'),(15,'priya','priya321@gmail.com','9856321256','pri'),(17,'dfg1','d1@d.com','1111121111','ass');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
