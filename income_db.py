# Contains all the functions that interact with the income table in the db.

## Imports ##

import sqlite3
import os

## Functions ##

# Creates income database if it doesn't exist.
def create_income():
    """
    Creates the income database if it doesn't already exist.

    Args:
        None
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
    except sqlite3.OperationalError:
        os.mkdir('data')
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS income(
                        category TEXT,
                        name TEXT UNIQUE PRIMARY KEY,
                        amount FLOAT,
                        date_added TEXT)''')
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()

    return [0, 0]

# Creates income_cats database if it doesn't exist.
def create_income_cats():
    """
    Creates the income categories database if it doesn't already exist.

    Args:
        None
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """  
    try:
        db = sqlite3.connect('data/tracker')
    except sqlite3.OperationalError:
        os.mkdir('data')
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS income_cats(name TEXT)')
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()

    return [0, 0]

# Gets a list of categories.
def get_cat_list():
    """
    Gets a list of income categories from the database.

    Args:
        None
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    cat_list = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT name
                          FROM income_cats''')
        for row in cursor:
            for category in row:
                cat_list.append(category)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return cat_list

# Gets a list of income names.
def get_name_list():
    """
    Gets a list of names from the income database.

    Args:
        None
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    name_list = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT name
                          FROM income''')
        for row in cursor:
            for name in row:
                name_list.append(name)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return name_list
        
# Gets specific income data.
def get_income(search_term):
    """
    Gets data for a specific income.

    Args:
        search_term: The search term to search the database for. (str or float)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        income_info: The info of a specific income. (list of strings and floats)
    """
    income_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM income WHERE 
                       category = ? OR name = ? OR amount = ? OR date_added = ?''',
                       (search_term, search_term, search_term, search_term))
        for row in cursor:
            income_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return income_info

# Gets all income data.
def get_all_income():
    """
    Gets data for all income.

    Args:
        None
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        income_info: A list of info of a specific income. (list of tuples of strings and floats)
    """
    income_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM income')
        for row in cursor:
            income_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return income_info

# Gets the total income amount of a category.
def get_cat_income(category):
    """
    Gets the total income of a category.

    Args:
        category: The category to get the amount of income from. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        income_total: The total amount of income for an income category. (float)
    """
    income_total = 0.0
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT amount FROM income WHERE
                       category = ?''',
                       (category,))
        for row in cursor:
            for amount in row:
                income_total += amount
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return income_total

# Gets income data from a single category.
def get_income_from_category(category):
    """
    Gets the income data of a single category.

    Args:
        category: The category to get the income data from. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        income_info: The income information from the database. (list of str, floats)
    """
    income_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM income WHERE
                       category = ?''',
                       (category,))
        for row in cursor:
            income_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return income_info    

# Adds an income.
def add_income(income_info):
    """
    Adds an income to the database.

    Args:
        income_info: A list of income information. (list of str, floats)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO income
                       (category, name, amount, date_added)
                       VALUES(?, ?, ?, ?)''',
                       (income_info[0], income_info[1], income_info[2], income_info[3]))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes an income.
def delete_income(name):
    """
    Deletes an income from the database.

    Args:
        name: The name of an income. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM income WHERE
                       name = ?''',
                       (name,))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Updates the information of an income.
def update_income(updated_income_info, income_name):
    """
    Updates the income information in the database.

    Args:
        updated_income_info: A list of the new income information. (list of str, floats)
        income_name: The name of the income to be updated. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''UPDATE income SET
                       category = ?, name = ?, amount = ?, date_added = ?
                       WHERE name = ?''',
                       (updated_income_info[0], updated_income_info[1], updated_income_info[2], updated_income_info[3], income_name))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes income associated with a category.
def delete_income_from_cat(category):
    """
    Deletes the income associated with a category from the database.

    Args:
        category: The category to delete the income from. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM income WHERE
                       category = ?''',
                       (category,))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Adds a new income category.
def add_income_cat(name):
    """
    Adds an income category to the database.

    Args:
        name: The name of the new income category. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO income_cats(name)
                          VALUES(?)''', (name,))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes an income category.
def delete_income_cat(name):
    """
    Deletes an income category from the database.

    Args:
        name: The name of the new income category. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM income_cats WHERE
                       name = ?''',
                       (name,))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]
