#-*- coding: utf8 -*-

import psycopg2 as pdb


# CREATE THE DATABASE

def creatdb_postgres():
    con = pdb.connect(database="testdb", user="postgres",
                  password="PASSWORD", host="127.0.0.1", port="5432")
    print "Create database testdb"

# SET UP THE CONNECTION
try:
    con = pdb.connect(database="testdb", user="postgres",
                      password="PASSWORD", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print ver

except pdb.DatabaseError, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

creatdb_postgres()
