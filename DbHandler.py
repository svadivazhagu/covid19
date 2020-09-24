# File that handles the pulling of Data from GitHub, and insertion into the Database cases.db
import sqlite3
from sqlite3 import Error
import pandas as pd
import requests as re


def create_conn(db):
    '''
    Creates connection with the SQlite database
    :param db:
    :return: Connection object or None
    '''
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    return conn


def create_table(conn, query):
    '''
    Creates a table given the connection and the table parameters
    :param conn:
    :param query:
    :return: Nothing
    '''
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)


def csv_sql(name, csv_fp, conn):
    df = pd.read_csv(csv_fp)
    df.columns = df.columns.str.strip()
    df.to_sql(name, conn, if_exists='replace')
    #print(name + ' inserted.')


def main():
    db = 'cases.db'
    conn = create_conn(db)

    # create tables
    if conn is not None:
        fp = 'data/'
        for i in ['country', 'states', 'counties']:
            csv_sql(i, fp + i + '.csv', conn)

    else:
        print("Error, connection failed")

    df = pd.read_csv('data/extracted/counties.csv')
    for i, row in df.iterrows():
        if df.at[i, 'fips'] != df.at[i, 'fips']:
            df = df.drop(i)
    # df.drop('Joplin', axis = 2)
    # df.drop('Kansas City', axis =2)
    df.to_csv('data/extracted/counties.csv', index=False)


if __name__ == '__main__':
    mapping = {'country': re.get('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us.csv'),
               'states': re.get('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv'),
               'counties': re.get('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv')}

    for i in mapping.keys():
        with open('data/' + i + '.csv', 'wb') as f:
            f.write(mapping[i].content)
        #print(i + ' downloaded.')

    main()


#adding the fips code for Joplin, MO and Kansas City MO


