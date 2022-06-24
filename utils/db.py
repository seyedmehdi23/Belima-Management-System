import sqlite3

conn = sqlite3.connect("../data.dcr")

def create_tables():
    conn.execute('''
    CREATE TABLE 
    ''')