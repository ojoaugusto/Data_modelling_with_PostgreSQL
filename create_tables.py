import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    # connect to default database
    conn = psycopg2.connect('host= localhost dbname = postgres user = joao password = admin')
    cur = conn.cursor()
    conn.set_session(autocommit=True)

    # create sparkify database
    cur.execute('DROP DATABASE IF EXISTS sparkifydb')
    cur.execute('CREATE DATABASE sparkifydb')

    # close connection
    cur.close()
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect('host= 127.0 dbname = sparkifydb user = joao password = admin')
    cur = conn.cursor()
    conn.set_session(autocommit=True)

    return conn, cur

def drop_tables(conn, cur):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(conn, cur):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    conn, cur = create_database()

    drop_tables(conn, cur)
    create_tables(conn, cur)

    conn.close()

if __name__ == '__main__':
    main()