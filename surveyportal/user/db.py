import mysql.connector

def connectDB():
    mydb = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'surveyportaldb'
    }
    return mydb
