"""Module for adding an event manually to db from commandline"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import datetime
import mangel_db

#from importlib import reload #py3 conv
#reload(sys)

def add_mangel_event():
    """ add event from cmdline """

    now = datetime.datetime.now()
    log_filename = f'logs/mangel_log-{now:%Y-%m-%d}'

#    log_filename = 'logs/mangel_log-{:%Y-%m-%d}'.format(datetime.datetime.now())
    logging.basicConfig(filename=log_filename,level=logging.DEBUG)

    logging.debug('')

#    logging.debug('{:%Y-%m-%d %H:%M:%S} add event cmdline'.format(datetime.now()))

    event = []
    event.append(input("Title of event: ").encode('utf-8'))
    event.append(input("Location: ").encode('utf-8'))
    event.append(input("Country: ").encode('utf-8'))
    event_date = input("Date and time: yy-mm-dd mm:hh ")
    #memberDate = datetime.strptime(memberDate, "%Y-%m-%d %H:%M:00")
    event.append(event_date)
    event.append(input("Organizer: ").encode('utf-8'))

    body_input = input("(l)ink to body doc or (w)rite: ").encode('utf-8')
    if body_input == "l":
        #read file and put into variable
        body = "read something from file"
    else:
        body = input("body: ").encode('utf-8')
    event.append(body)

    event.append(input("path to image: "))
    #cp img to proper place. rename to unique and save ref

    event.append(input("link to event: "))

    event.append(input("Disability friendly: yes/no "))

    mangel_db_file = "mangel.db"

    # create a database connection
#    logging.debug('{:%Y-%m-%d %H:%M:%S} Create con to db'.format(datetime.now()))
    conn = mangel_db.create_connection(mangel_db_file)
    conn.text_factory = str

    sql_create_table= """
        CREATE TABLE IF NOT EXISTS events(
            id integer PRIMARY KEY,
            title      text NOT NULL,
            location   text NOT NULL,
            country    text NOT NULL,
            [date] timestamp NOT NULL,
            organizer  text NOT NULL,
            body       text NOT NULL,
            img        text,
            link       text,
            disability text NOT NULL
            ); """

    with conn:

        #logging.debug('{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())+str(member))
        mangel_db.create_event_table(conn,sql_create_table)
        #maybe event must be tuple
        event_id = mangel_db.add_event_to_db(conn, event) #tuple?
        if event_id:
            print(str(event_id)+" success")
