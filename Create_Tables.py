# Imports
import sqlite3
import time
from pprint import pprint

# Create rdb and cursor object

conn = sqlite3.connect('classicmodels.db')
cur = conn.cursor()

# If table customers  exists then the table is dropped
cur.execute('DROP TABLE IF EXISTS customers;')

# Else
cur.execute('''CREATE TABLE `customers` (
  `customerNumber` int(11) NOT NULL,
  `customerName` varchar(50) NOT NULL,
  `contactLastName` varchar(50) NOT NULL,
  `contactFirstName` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `addressLine1` varchar(50) NOT NULL,
  `addressLine2` varchar(50) DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) DEFAULT NULL,
  `postalCode` varchar(15) DEFAULT NULL,
  `country` varchar(50) NOT NULL,
  `salesRepEmployeeNumber` int(11) DEFAULT NULL,
  `creditLimit` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`customerNumber`)) ;''')


# If table orders  exists then the table is dropped
cur.execute('''DROP TABLE IF EXISTS `orders`;''')
# Else
cur.execute('''CREATE TABLE `orders` (
  `orderNumber` int(11) NOT NULL,
  `orderDate` date NOT NULL,
  `requiredDate` date NOT NULL,
  `shippedDate` date DEFAULT NULL,
  `status` varchar(15) NOT NULL,
  `comments` text,
  `customerNumber` int(11) NOT NULL,
  PRIMARY KEY (`orderNumber`));''')

# NULL value handler
NULL='NULL'

# Values for the table orders  read from orders.txt file
my_file = open('orders.txt', 'r')
values = my_file.readlines()

# Select the number of values by changing N
N = 5
# Loop for inserting values to the table
for i in values:
    if i != '\n':
        print(i)
        cur.execute('''insert  into `orders`(`orderNumber`,`orderDate`,`requiredDate`,`shippedDate`,`status`,`comments`,`customerNumber`)values '''+str(i))

# Commit to the database
conn.commit()


# Values for the table customers  read from customers.txt file
my_file = open('customers.txt', 'r')
values = my_file.readlines()

# Select the number of values by changing N
N = 5
# Loop for inserting values to the table
for i in values:
    if i != '\n':
        print(i)
        cur.execute('''insert  into `customers`(`customerNumber`,`customerName`,`contactLastName`,`contactFirstName`,`phone`,`addressLine1`,`addressLine2`,`city`,`state`,`postalCode`,`country`,`salesRepEmployeeNumber`,`creditLimit`) values'''+str(i))

# Commit to the database
conn.commit()

print("*-*-*-*-*-**-*-* TABLES CREATED SUCESSSFULLY *-*-*-*-*-*-*-*-*-*")