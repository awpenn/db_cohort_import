import psycopg2 as psy
import pandas as pd 
import sys

def load_table(file_path, table_name, db, host, port, user, pwd):
    try:
        print('start')
        print(host)
        conn = psy.connect(dbname=db, host=host, port=port,\
        user=user, password=pwd)
        print('connecting')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cohorts')
        conn.close()
    except Exception as e:
        print(str(e))
        sys.exit(1)

file_path = 'wow.txt'
table_name = 'consent_sandbox'
db = 'consent_sandbox'
host = '158.130.176.63'
user = 'postgres'
port = 5432
pwd = 'root'

load_table(file_path, table_name, db, host, port, user, pwd)