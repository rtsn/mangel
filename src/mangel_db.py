""" mostly stolen from http://www.sqlitetutorial.net/sqlite-python/ """
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import sqlite3
from sqlite3 import Error
#import datetime


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    logging.debug("createConnection(db_file)")
    logging.debug("trying to create connection to db")
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as error:
        print(error)
        logging.debug(error)

    return None

def create_event_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param createTable_sql: a CREATE TABLE statement
    :return:
    """
    logging.debug("createTable(conn, createTable_sql)")
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as error:
        print(error)
        logging.debug(error)

def add_event_to_db(conn, event):
    """ description
        :param conn:
        :param id integer PRIMARY KEY,
        :param title      text NOT NULL,
        :param location   text NOT NULL,
        :param country    text NOT NULL,
        :param [date] timestamp NOT NULL,
        :param organizer  text NOT NULL,
        :param body       text NOT NULL,
        :param img        text,
        :param link       text,
        :param disability text NOT NULL
        :return event_id
    """
#    now = datetime.datetime.now()

    sql = '''INSERT INTO events (title,location,country,date,organizer,
        body,img,link,disability) VALUES(?,?,?,?,?,?,?,?,?)'''

#    logging.debug("insertMember(conn, member)")
#    logging.debug(sql)

    try:
        cur = conn.cursor()
        cur.execute(sql, event)
    #    logging.debug(cur.lastrowid)
        return cur.lastrowid
    except Error as error:
        print(error)
        logging.debug(error)
        return None

def get_all_events(conn):
    """ returns all rows in table members from db as a list of rows
    :param conn:
    :return: rows
    """
    try:
    #    logging.debug("getAllMembers(conn)")
        cur = conn.cursor()
        sql = "SELECT * FROM events;"
        cur.execute(sql)

        rows = cur.fetchall()
#        logging.debug("found " +numb)
        print(str(len(rows))+" members in db")

        return rows
    except Error as error:
        print(error)
        logging.debug(error)
        return None

#def get_event(conn,event_id):
#    pass
