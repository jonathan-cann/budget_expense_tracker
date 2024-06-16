# Contains all the functions that interact with the goals table in the db.

## Imports ##

import sqlite3
import os

## Functions ##

# Creates database if it doesn't exist.
def create():
    """
    Creates the goals database if it doesn't already exist.

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
    finally:
        db = sqlite3.connect('data/tracker')
    try:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS goals(
                        name TEXT UNIQUE PRIMARY KEY,
                        category TEXT,
                        amount FLOAT,
                        progress FLOAT)''')
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Gets goal info based on a name.
def get_goal_info(name):
    """
    Gets the info for a goal based on a given name.

    Args:
        name: The name of the goal to get the info of. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        goal_info: The goal information as a list. (list of str, float)
    """
    goal_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM goals WHERE
                       name = ?''',
                       (name,))
        for row in cursor:
            goal_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return goal_info  

# Gets goals info based on the category.
def get_goals_list(category):
    """
    Gets the info for some goals based on a given category.

    Args:
        category: The name of the category of goals to get the info of. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        goals_info: The goal information as a list of tuples. (list of tuples of str, float)
    """
    goals_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM goals WHERE
                       category = ?''',
                       (category,))
        for row in cursor:
            goals_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return goals_info   

# Adds a goal.
def add_goal(goal_info):
    """
    Adds a new goal to the goals database.

    Args:
        goal_info: The goal info to add to the database. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO goals
                       (name, category, amount, progress)
                       VALUES(?, ?, ?, ?)''',
                       (goal_info[0], goal_info[1], goal_info[2], goal_info[3]))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Updates a goal.
def update_goal(name, updated_goal_info):
    """
    Updates a goal in the goals database.

    Args:
        name: The name of the goal to be updated. (str)
        updated_goal_info: The goal info used to update the database. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''UPDATE goals SET
                       name = ?, category = ?, amount = ?, progress = ?
                       WHERE name = ?''',
                       (updated_goal_info[0], updated_goal_info[1], updated_goal_info[2], updated_goal_info[3], name))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Updates the progress value of a saving goal.
def update_saving_goal_progress(goal_name, new_progress):
    """
    Updates the progress value of a saving goal.

    Args:
        goal_name: The name of the goal to update. (str)
        new_progress: The value of progress. (float)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''UPDATE goals SET
                       progress = ? WHERE name = ?''',
                       (new_progress, goal_name))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes a goal.
def delete_goal(name, category):
    """
    Deletes a goal in the goals database.

    Args:
        name: The name of the goal to be deleted. (str)
        category: The category of the goal to be deleted. (str)
        
    Returns:
        [1, e]: 1 is a fault code to show something has gone wrong and e is the sqlite3 error. (str)
        [0, 0]: 0 shows that nothing has gone wrong.
    """
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM goals WHERE
                       name = ? AND category = ?''',
                       (name, category))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]