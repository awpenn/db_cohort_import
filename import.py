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
        with open(file_path, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # build insert string of columns to insert on from keys of dictr

                colname_list = ''
                for i in row.keys():
                    print(row[i])
                    if len(row[i]) > 0:
                        colname_list += f'{i},'

                colname_list_trim = colname_list[:-1]

                # build insert string of values to insert from dictr
                values_list = ''
                for i in row.keys():
                    if len(row[i]) > 0:
                        values_list += f'\'{row[i]}\','
                
                values_list_trim = values_list[:-1]
                
                # write INSERT statement
                insert_statement = f'INSERT INTO cohorts ({colname_list_trim}) VALUES ({values_list});'

                







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


