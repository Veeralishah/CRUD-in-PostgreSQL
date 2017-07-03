#-*- coding: utf8 -*-

''' MYSQL CRUD '''

import psycopg2 as pdb
import warnings
import psycopg2.extras
import sys


# CREATE A NEW TABLE


def createTable(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Emp")
        cur.execute(
            "CREATE TABLE Emp(Id SERIAL PRIMARY KEY, Name VARCHAR(25), Company_Name VARCHAR(25), Designation VARCHAR(25), Age VARCHAR(25), City VARCHAR(25));")
        print 'Employee Table created'

# INSERT VALUES


def insertTable(con):
    with con:

        try:
            cur = con.cursor()

            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS Emp(Id SERIAL PRIMARY KEY, Name VARCHAR(25), Company_Name VARCHAR(25), Designation VARCHAR(25), Age VARCHAR(25), City VARCHAR(25));")
                print 'Employee Table created'
                warnings.filterwarnings('ignore', 'unknown table')

            Name = raw_input("Enter Your Name ")
            Company_Name = raw_input("Enter Your Company Name")
            Designation = raw_input("Enter Your Designation")
            Age = raw_input("Enter Your Age")
            City = raw_input("Enter Your City")
            cur.execute("INSERT INTO Emp  (Name, Company_Name, Designation, Age, City) VALUES(%s, %s, %s, %s, %s)",
                        (Name, Company_Name, Designation, Age, City))
            print "Record Inserted"
            con.commit()
        except Exception as e:
            print e


# RETRIEVE TABLE ROWS
def retrieveTable(con):
    with con:

        cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
        cur.execute("SELECT * FROM Emp")

        rows = cur.fetchall()
        for row in rows:
            if rows == None:
                print 'Table is Empty'
                break
            else:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))


# UPDATE ROW
def updateRow(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            e_id = input("Enter id You want to update")
            name = raw_input("Enter Name for Update Record")
            cname = raw_input("Enter Company Name for Update Record")
            deg = raw_input("Enter Designation for Update Record")
            age = raw_input("Enter Age for Update Record")
            city = raw_input('Enter City Name For Update record')

            cur.execute("UPDATE Emp SET name =%s, Company_Name = %s, Designation = %s, Age = %s, City = %s WHERE Id = %s",
                        (name, cname, deg, age, city, e_id))

            print "Number of rows updated:",  cur.rowcount
            if cur.rowcount == 0:
                print 'Record Not Updated'
        except TypeError as e:
            print 'ID Not Exist '

#  # DELETE ROW


def deleteRow(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            id = raw_input("Enter ID for Delete Record")
            cur.execute("DELETE FROM Emp WHERE Id = %s", id)
            print "Number of rows deleted:", cur.rowcount

        except TypeError as e:
            print 'ID Not Exist '
