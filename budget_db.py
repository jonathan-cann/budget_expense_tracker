# Contains all the functions that interact with the budget table in the db.

## Imports ##

import sqlite3
import os

## Functions ##

# Creates database if it doesn't exist.
def create():
    try:
        db = sqlite3.connect('data/tracker')
    except sqlite3.OperationalError:
        os.mkdir('data')
    finally:
        db = sqlite3.connect('data/tracker')
    try:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS budget(
                        id INTEGER PRIMARY KEY,
                        category TEXT,
                        name TEXT,
                        date_added TEXT)''')
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Searches a specific db for something.
def get_info(search_term, db):
    db_info = []
    book_info = []
    try:
        db = sqlite3.connect('data/ebookstore')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM book WHERE 
                       id = ? OR title = ? OR author = ?''',
                       (search_term, search_term, search_term))
        for row in cursor:
            db_info.append(row)
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
    # Adds the search term to the end of each tuple.
    for book in db_info:
        temp = list(book)
        temp.append(search_term)
        book = tuple(temp)
        book_info.append(book)
    # Returns a list of tuples containing book information.
    return book_info