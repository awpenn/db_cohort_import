import psycopg2 as psy
import csv
import sys

def load_table(file_path, table_name, db, host, port, user, pwd):
    try:
        print('start')

        conn = psy.connect(dbname=db, host=host, port=port,\
        user=user, password=pwd)
        print('connected')
        
        cursor = conn.cursor()
        # cursor.execute('SELECT * FROM cohorts')
        # open csv, for each file make insert and cursor.execute(//insert//) 
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['note'])       




        conn.close()
    except Exception as e:
        print(str(e))
        sys.exit(1)

file_path = './update_test.csv'
table_name = 'cohorts'
db = 'consent_sandbox'
host = '158.130.176.63'
user = 'postgres'
port = 5432
pwd = 'root'

load_table(file_path, table_name, db, host, port, user, pwd)


