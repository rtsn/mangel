"""Module for adding an event manually to db from commandline"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import add_event
import mangel_db

def main():
    """proof of concept"""
    print(add_event.add_mangel_event())

    mangel_db_file = "mangel.db"
    conn = mangel_db.create_connection(mangel_db_file)
    events = mangel_db.get_all_events(conn)
    for event in events:
        print(event)

if __name__ == '__main__':
    main()
