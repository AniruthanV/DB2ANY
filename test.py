import rdflib
import sqlite3
g=rdflib.Graph()
g.parse('a.rdf')
print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))
print("******************************")

qres = g.query(
    """SELECT   ?name ?country
       WHERE {
       ?customer <http://www.classicmodels.tms/classicmodels/orders#customerNumber>  '121' .
       ?customer <http://www.classicmodels.tms/classicmodels/orders#orderDate> ?name .
       ?customer <http://www.classicmodels.tms/classicmodels/orders#status> ?country.
       }""")


conn = sqlite3.connect('classicmodels.db')
cur = conn.cursor()

# Select the values from the database using customer number to look at entries
c_number = '103'
for row in conn.execute('SELECT customerName , country FROM customers WHERE customerNumber = '+c_number):
    print(row)
for row in conn.execute('SELECT orderNumber , customerNumber FROM orders WHERE customerNumber = '+c_number):
    print(row)

# Select the values from the database using order number to look at entries
o_number = '10123'
for row in conn.execute('SELECT orderNumber , customerNumber FROM orders WHERE orderNumber = '+o_number):
    print(row)


for i in qres:
    print(i)