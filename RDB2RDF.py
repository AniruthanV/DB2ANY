# Imports
import sqlite3
import time

# Access RDB and cursor object

conn = sqlite3.connect('classicmodels.db')
cur = conn.cursor()

def RDB2RDF():

    # Record the start time
    t1 = time.time()

    # Create the rdf file
    file = open('classicmodels.rdf', 'w')

    # Create triple that holds the class/tablenames and writes to file
    triple = '''<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
                         xmlns:classicmodels="http://www.classicmodels.tms/classicmodels#"
                         xmlns:customers="http://www.classicmodels.tms/classicmodels/customers#"
                         xmlns:orders="http://www.classicmodels.tms/classicmodels/orders#"
                >'''
    file.write(triple+"\n")
    print(triple)

    # Read the table and get the values and column names
    a = cur.execute("select * from customers ;")
    col_name_list = [t[0] for t in cur.description]

    # Loop for creating triples
    for row in cur:
        # Creates the node using the customer id as primary key  and writes to file
        triple = "<rdf:Description rdf:about=\"http://www.classicmodels.tms/classicmodels/customers/" + str(row[0]).replace(" ", "") + "\">"
        file.write(triple + "\n")


        # Inner loop that get values from rows
        for i in range(len(row)):
            # Creates the subnodes conatining the attributes and writes to file
            triple = "<customers:" + str(col_name_list[i]).replace(" ", "") + ">" + str(row[i]).replace(" ", "") + "</customers:" + str(col_name_list[i]).replace(" ", "") + ">"
            file.write(triple + "\n")

        # Closes the node
        triple = "</rdf:Description>"
        file.write(triple + "\n")


    # Read the table and get the values and column names
    a = cur.execute("select * from orders ;")
    col_name_list = [t[0] for t in cur.description]

    # Loop for creating triples
    for row in cur:
        # Creates the node using the customer id as primary key  and writes to file
        triple = "<rdf:Description rdf:about=\"http://www.classicmodels.tms/classicmodels/orders/" + str(row[0]).replace(" ", "") + "\">"
        file.write(triple + "\n")

        # Inner loop that get values from rows
        for i in range(len(row)):
            # Creates the subnodes conatining the attributes and writes to file
            triple = "<orders:" + str(col_name_list[i]).replace(" ", "") + ">" + str(row[i]).replace(" ", "") + "</orders:" + str(col_name_list[i]).replace(" ", "") + ">"

            file.write(triple + "\n")

        # Closes the node
        triple = "</rdf:Description>"
        file.write(triple + "\n")

    # Closes rdf
    triple = "</rdf:RDF>"
    file.write(triple+"\n")

    # Closes file
    file.close()

    # Records end time and, Prints the time taken
    t2 = time.time()
    print("time taken :"+str(t2-t1))
RDB2RDF()