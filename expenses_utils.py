# Utility functions for the expenses part of the tracker.
import global_utils

# Gets the name of a new category.
def get_new_cat_name(current_expense_cats):
    """
    Gets the name of a new expense category.

    Args:
        current_expense_cats: A list of the names of the current expense categories. (list of str)
        
    Returns:
        cat_input: The name of the new expense category. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        cat_input = input('''Please describe the expense category. The name must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_expense_cats:
            print("\nThe category you entered matches an existing category.")
            continue
        return cat_input

# Gets the name of an expense category for a new expense.
def get_new_expense_cat(current_expense_cats):
    """
    Gets the name of the expense category of a new expense.

    Args:
        current_expense_cats: A list of the names of the current expense categories. (list of str)
        
    Returns:
        cat_input: The name of the expense category of the new expense. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you wish to add the expense to. Enter 0 to cancel.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_expense_cats:
            return cat_input
        else:
            print("\nYou did not enter the name of a category.")

# Gets the name of a new expense.
def get_new_expense_name(current_expense_names):
    """
    Gets the name of a new expense.

    Args:
        current_expense_names: A list of the names of the existing expenses. (list of str)
        
    Returns:
        name_input: The name of the new expense. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        name_input = input('''Please describe the expense. It must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_expense_names:
            print("\nThe expense name you entered matches an existing name.")
            continue
        return name_input

# Gets the amount of a new expense.
def get_new_expense_amount():
    """
    Gets the value of the new expense.

    Args:
        None
        
    Returns:
        amount: The value of the new expense. (float)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        amount_input = input('''Please enter the amount of the expense. Enter 0 to return to the previous menu.
: ''').lower()
        if amount_input == '0':
            return 1
        if len(amount_input[amount_input.rfind('.')+1:]) != 2:
            print("\nPlease enter a valid amount.")
            continue
        try:
            amount = float(amount_input)
        except ValueError:
            print("\nPlease enter a valid amount.")
            continue
        return amount

# Gets the category for an expense edit. 
def get_edit_expense_cat(current_expense_cats, current_expense_info):
    """
    Checks if the user wants to edit the category of an expense and gets the new category if they do.

    Args:
        current_expense_cats: A list of the names of the current expense categories. (list of str)
        current_expense_info: A list of the current expense info. (list of strings, floats)
        
    Returns:
        new_cat_input: The name of the expense category of the edited expense. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    # Checks if the user wants to edit the expense category.
    while True:
        print('')
        confirm_input = input(f'''The current category is {global_utils.name_capitalise(current_expense_info[0])}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Prints the current expense categories.
    print('\nThe current expense categories are:')
    for expense_cat in current_expense_cats:
        print(global_utils.name_capitalise(expense_cat))

    # Gets the name of the new category.
    while True:
        print('')
        new_cat_input = input(f'''Please enter the category you wish to change the expense to. Enter 0 to return to the previous menu.
: ''').lower()
        if new_cat_input == '0':
            return 1
        elif new_cat_input in current_expense_cats:
            return new_cat_input
        else:
            print("\nYou did not enter the name of a category.")

# Gets a new name for an expense edit.
def get_edit_expense_name(current_expense_names, current_expense_info):
    """
    Checks if the user wants to edit the name of an expense and gets the new name if they do.

    Args:
        current_expense_names: A list of the names of the current expenses. (list of str)
        current_expense_info: A list of the current expense info. (list of strings, floats)
        
    Returns:
        new_name_input: The new name of the expense. (str)
        1: If the user wishes to return to the previous menu. (int)
    """    
    # Checks if the user wants to edit the expense name.    
    while True:
        print('')
        confirm_input = input(f'''The name of the expense is {global_utils.name_capitalise(current_expense_info[1])}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Prints a list of current expense names.
    print('\nThe current expense names are:')
    for name in current_expense_names:
        print(global_utils.name_capitalise(name))

    # Gets a new name if needed.
    while True:
        print('')
        new_name_input = input(f'''Please enter a new name for the expense. It must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if new_name_input == '0':
            return 1
        if new_name_input in current_expense_names:
            print("\nThe expense name you entered matches an existing name.")
            continue
        return new_name_input

# Gets a new amount for an expense edit.
def get_edit_expense_amount(current_expense_info):
    """
    Checks if the user wants to edit the value of an expense and gets the new value if they do.

    Args:
        current_expense_info: A list of the current expense info. (list of strings, floats)
        
    Returns:
        new_amount: The new value of the expense. (str)
        1: If the user wishes to return to the previous menu. (int)
    """ 
    # Checks if the user wants to edit the expense amount.
    while True:
        print('')
        confirm_input = input(f'''The value of the expense is {global_utils.amount_format(current_expense_info[2])}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Gets a new expense amount if required.
    while True:
        print('')
        new_amount_input = input('''Please enter the new amount of the expense. Enter 0 to return to the previous menu.
: ''').lower()
        if new_amount_input == '0':
            return 1
        if len(new_amount_input[new_amount_input.rfind('.')+1:]) != 2:
            print("Please enter a valid amount.")
            continue
        try:
            new_amount = float(new_amount_input)
        except ValueError:
            print("Please enter a valud amount.")
            continue
        return new_amount
        
# Gets the name of the expense to edit.        
def get_expense_to_edit(current_expense_names):
    """
    Gets the name of the expense the user wants to change.

    Args:
        current_expense_names: A list of the names of the current expenses. (list of str)
        
    Returns:
        name_input: The name of the expense the user wants to edit. (str)
        1: If the user wishes to return to the previous menu. (int)
    """ 
    while True:
        print('')
        name_input = input('''Please enter the name of the expense you want to edit. Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_expense_names:
            return name_input
        else:
            print("\nYou did not enter the name of a expense.")     

# Gets the name of the expense to delete.
def get_expense_to_delete(current_expense_names):
    """
    Gets the name of the expense the user wants to delete.

    Args:
        current_expense_names: A list of the names of the current expenses. (list of str)
        
    Returns:
        name_input: The name of the expense the user wants to edit. (str)
        1: If the user wishes to return to the previous menu. (int)
    """ 
    while True:
        print('')
        name_input = input('''Please enter the name of the expense you want to delete. Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_expense_names:
            return name_input
        else:
            print("\nYou did not enter the name of a expense.")   

# Gets the name of the category to view.
def get_cat_to_view(current_expense_cats):
    """
    Gets the name of the expense category the user wants to view.

    Args:
        current_expense_cats: A list of the names of the current expense categories. (list of str)
        
    Returns:
        cat_input: The name of the expense category the user wants to view. (str)
        1: If the user wishes to return to the previous menu. (int)
    """ 
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you want to view. Enter 0 to return to the previous menu.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_expense_cats:
            return cat_input
        else:
            print("\nYou did not enter the name of a category.") 

# Gets the name of the category to delete.
def get_cat_to_delete(current_expense_cats):
    """
    Gets the name of the expense category the user wants to delete.

    Args:
        current_expense_cats: A list of the names of the current expense categories. (list of str)
        
    Returns:
        cat_input: The name of the expense category the user wants to view. (str)
        1: If the user wishes to return to the previous menu. (int)
    """ 
    # Gets the name.
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you want to delete. Enter 0 to return to the previous menu.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_expense_cats:
            break
        else:
            print("\nYou did not enter the name of a category.")
    
    # Confirms that the user does want to delete the category.
    while True:
        confirm_input = input(f'''\nAre you sure you want to delete the {global_utils.name_capitalise(cat_input)} category? All expenses in this
category will also be deleted. Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            return cat_input
        elif confirm_input == 'no' or confirm_input == 'n':
            return 1
        else:
            print("\nPlease enter yes or no.")