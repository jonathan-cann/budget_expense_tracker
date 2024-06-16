# Utility functions for the income part of the tracker.
import global_utils

# Gets the name of a new category.
def get_new_cat_name(current_income_cats):
    """
    Gets the name of a new income category.

    Args:
        current_income_cats: A list of the existing income categories. (list of strings)
        
    Returns:
        cat_input: The name of the new income category. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        cat_input = input('''Please describe the income category. The name must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            print("\nThe category you entered matches an existing category.")
            continue
        return cat_input

# Gets the name of an income category for a new income.
def get_new_income_cat(current_income_cats):
    """
    Gets the name of an income category for a new income.

    Args:
        current_income_cats: A list of the existing income categories. (list of strings)
        
    Returns:
        cat_input: The name of the income category for the new saving goal. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you wish to add the income to. Enter 0 to cancel.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            return cat_input
        else:
            print("\nYou did not enter the name of a category.")

# Gets the name of a new income.
def get_new_income_name(current_income_names):
    """
    Gets the name of a new income.

    Args:
        current_income_names: A list of the existing income names. (list of strings)
        
    Returns:
        name_input: The name for the new saving goal. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        name_input = input('''Please describe the income. The name must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_income_names:
            print("\nThe income name you entered matches an existing name.")
            continue
        return name_input

# Gets the amount of a new income.
def get_new_income_amount():
    """
    Gets the amount of a new income.

    Args:
        None
        
    Returns:
        amount: The amount of the new income. (float)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        amount_input = input('''Please enter the amount of the income. Enter 0 to return to the previous menu.
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

# Gets the category for an income edit. 
def get_edit_income_cat(current_income_cats, current_income_info):
    """
    Gets a new category when editing an income.

    Args:
        current_income_cats: A list of the existing income categories. (list of strings)
        current_income_info: A list of the information of the current income. (list of strings, floats)
        
    Returns:
        new_cat_input: The new name of the income category for a goal. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    # Checks if the user wants to edit the income category.
    while True:
        print('')
        confirm_input = input(f'''The current category is {global_utils.name_capitalise(current_income_info[0])}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Prints the current income categories.
    print('\nThe current income categories are:')
    for income_cat in current_income_cats:
        print(global_utils.name_capitalise(income_cat))

    # Gets the name of the new category.
    while True:
        print('')
        new_cat_input = input(f'''Please enter the category you wish to change the income to. Enter 0 to return to the previous menu.
: ''').lower()
        if new_cat_input == '0':
            return 1
        elif new_cat_input in current_income_cats:
            return new_cat_input
        else:
            print("\nYou did not enter the name of a category.")

# Gets a new name for an income edit.
def get_edit_income_name(current_income_names, current_income_info):
    """
    Gets the new name of an income when editing.

    Args:
        current_income_names: A list of the existing income names. (list of strings)
        current_income_info: A list of the information of the current income. (list of strings, floats)
        
    Returns:
        new_name_input: The new name of the saving goal. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    # Checks if the user wants to edit the income name.    
    while True:
        print('')
        confirm_input = input(f'''The name of the income is {global_utils.name_capitalise(current_income_info[1])}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Prints a list of current income names.
    print('\nThe current income names are:')
    for name in current_income_names:
        print(global_utils.name_capitalise(name))

    # Gets a new name if needed.
    while True:
        print('')
        new_name_input = input(f'''Please enter a new name for the income. It must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if new_name_input == '0':
            return 1
        if new_name_input in current_income_names:
            print("\nThe income name you entered matches an existing name.")
            continue
        return new_name_input

# Gets a new amount for an income edit.
def get_edit_income_amount(current_income_info):
    """
    Gets the new amount for an income when editing.

    Args:
        current_income_info: A list of the information of the current income. (list of strings, floats)
        
    Returns:
        new_amount: The new amount for the saving goal. (float)
        1: If the user wishes to return to the previous menu. (int)
    """
    # Checks if the user wants to edit the income amount.
    while True:
        print('')
        confirm_input = input(f'''The value of the income is {global_utils.amount_format(current_income_info[2])}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Gets a new income amount if required.
    while True:
        print('')
        new_amount_input = input('''Please enter the new amount of the income. Enter 0 to return to the previous menu.
: ''').lower()
        if new_amount_input == '0':
            return 1
        if len(new_amount_input[new_amount_input.rfind('.')+1:]) != 2:
            print("Please enter a valid amount.")
            continue
        try:
            new_amount = float(new_amount_input)
        except ValueError:
            print("Please enter a valid amount.")
            continue
        return new_amount
        
# Gets the name of the income to edit.        
def get_income_to_edit(current_income_names):   
    """
    Gets the name of the income to edit.

    Args:
        current_income_names: A list of the names of the current income. (list of strings)
        
    Returns:
        name_input: The name of the income to edit. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        name_input = input('''Please enter the name of the income you want to edit. Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_income_names:
            return name_input
        else:
            print("\nYou did not enter the name of a income.")     

# Gets the name of the income to delete.
def get_income_to_delete(current_income_names):
    """
    Gets the name of the income to delete.

    Args:
        current_income_names: A list of the names of the current income. (list of strings)
        
    Returns:
        name_input: The name of the income to delete. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        name_input = input('''Please enter the name of the income you want to delete. Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_income_names:
            return name_input
        else:
            print("\nYou did not enter the name of a income.")   

# Gets the name of the category to view.
def get_cat_to_view(current_income_cats):
    """
    Gets the name of the category to view.

    Args:
        current_income_cats: A list of the names of the current income categories. (list of strings)
        
    Returns:
        cat_input: The name of the income category to view. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you want to view. Enter 0 to return to the previous menu.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            return cat_input
        else:
            print("\nYou did not enter the name of a category.") 

# Gets the name of the category to delete.
def get_cat_to_delete(current_income_cats):
    """
    Gets the name of the category to delete.

    Args:
        current_income_cats: A list of the names of the current income categories. (list of strings)
        
    Returns:
        cat_input: The name of the income category to delete. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    # Gets the name.
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you want to delete. Enter 0 to return to the previous menu.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            break
        else:
            print("\nYou did not enter the name of a category.")
    
    # Confirms that the user does want to delete the category.
    while True:
        confirm_input = input(f'''\nAre you sure you want to delete the {global_utils.name_capitalise(cat_input)} category? All income in this
category will also be deleted. Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            return cat_input
        elif confirm_input == 'no' or confirm_input == 'n':
            return 1
        else:
            print("\nPlease enter yes or no.")