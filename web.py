# Imports
from flask import Flask, render_template,request
import sqlite3
import rdflib
import time



# Access RDB and cursor object



def RDB2RDF():
    import sqlite3
    conn = sqlite3.connect('classicmodels.db')
    cur = conn.cursor()
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


# Creating flask app
app = Flask(__name__)
content=""
@app.route('/')
def main_page():
    return render_template("main.html")
@app.route('/RDBTORDF')
def main_page1():
    # Access RDB and cursor object
    RDB2RDF()


    return render_template("progress.html", content=content)
@app.route('/SQL/',methods = ['POST', 'GET'])
def main_page2(query='  '):
    if request.method == 'POST':
        result = request.form
        print(result['Query'])
        query = result['Query']
        conn = sqlite3.connect('classicmodels.db')
        cur = conn.cursor()
        a = cur.execute(query)
        o=[]
        for i in a:
            o+=i
        return render_template("SQL.html",query=query, content=o)
@app.route('/SPARQL/',methods = ['POST', 'GET'])
def main_page3():
    if request.method == 'POST':
        result = request.form
        query = result['Query']
        g = rdflib.Graph()
        g.parse('classicmodels.rdf')
        qres = g.query(query)
        print(qres)
        o = []
        for i in qres:
            o += i
            print(i)
        return render_template("SPARQL.html", query=query, content=o)
    return render_template("SPARQL.html", query='', content='')

@app.route('/Queries')
def page4():
    return render_template("QUERIES.html", content=content)
@app.route('/credits')
def main_page5():
    return render_template("credits.html", content=content)
@app.route('/RDF')
def main_page6():
    import rdflib
    g = rdflib.Graph()
    g.parse('classicmodels.rdf')
    print("--- printing raw triples ---")
    table = ""
    for s, p, o in g:
        table += "<tr>\n"
        table += "<td>" + str(s) + "</td>\n"
        table += "<td>" + str(p) + "</td>\n"
        table += "<td>" + str(o) + "</td>\n"
        table += "</tr>\n"
    print(table)
    my_file=open('classicmodels.rdf','r')
    content2=''
    for i in my_file.readlines():
        content2 += str(i)
    print(content2)
    return render_template("table2.html", content=table, content2 = content2)

@app.route('/RDB')
def main_page7():
    conn = sqlite3.connect('classicmodels.db')
    cur = conn.cursor()
    a = cur.execute("select * from customers ;")
    table=''
    for row in cur:
        table += "<tr>\n"
        for i in range(len(row)):
            table += "<td>" + str(row[i]) + "</td>\n"
        table += "</tr>\n"

    print(table)
    b = cur.execute("select * from orders ;")
    table2 = ''
    for row in cur:
        table2 += "<tr>\n"
        for i in range(len(row)):
            table2 += "<td>" + str(row[i]) + "</td>\n"
        table2+= "</tr>\n"

    print(table2)
    return render_template("table.html", content=table,content2=table2)



if __name__ == "__main__":
    app.run()
