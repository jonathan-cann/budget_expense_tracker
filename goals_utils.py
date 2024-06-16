import income_db
import goals_db
import global_utils

# Gets the name of a new saving goal.
def get_new_saving_goal_name(current_saving_goals):
    """
    Gets the name of a new saving goal.

    Args:
        current_saving_goals: A list of the existing saving goals. (list of tuples of str, floats)
        
    Returns:
        name_input: The name of the new saving goal. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        name_input = input('''Please describe the goal. The name must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_saving_goals:
            print("\nThe income name you entered matches an existing name.")
            continue
        return name_input
        
# Gets the amount of a new goal.
def get_new_goal_amount():
    """
    Gets the target amount of a new saving goal.

    Args:
        None
        
    Returns:
        amount: The target amount of the new saving goal. (float)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        amount_input = input('''Please enter a target amount. Enter 0 to return to the previous menu.
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

# Gets the name of an income category for a new goal.
def get_cat_name(current_income_cats):
    """
    Gets the name of the income category for a new saving goal.

    Args:
        current_income_cats: A list of the existing income categories. (list of str)
        
    Returns:
        cat_input: The name of the saving goal category. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you wish to add a goal to. Enter 0 to cancel.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            return cat_input
        else:
            print("\nYou did not enter the name of a category.")

# Gets the total income of an income category.
def get_income_of_category(category):
    """
    Gets the total income of an income category.

    Args:
        category: The name of the income category. (str)
        
    Returns:
        category_income: The name of the category of the new saving goal. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    category_income = income_db.get_cat_income(category)
    if type(category_income) == float:
        return category_income
    # If get_income_from_category() has returned an error.
    if category_income[0] == 1:
        print("\nSorry, something went wrong getting the category's income.")
        print(f"Error: {category_income[1]}")
        return 1

# Gets the name of the goal to edit.
def get_goal_to_edit(income_goals, saving_goals):
    """
    Gets the name of a goal to edit and the category that it's in.

    Args:
        income_goals: A list of income goals. (list of str)
        saving_goals: A list of saving goals. (list of str)
        
    Returns:
        [name_input, choice_result]: A list of the name of the goal and the name of either income or saving. (list of str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        name_input = input('''Please enter the name of the goal you want to edit. Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        income_count = 0
        saving_count = 0
        for goal in income_goals:
            if name_input == goal[0]:
                income_count += 1
        for goal in saving_goals:
            if name_input == goal[0]:
                saving_count += 1
        if income_count == 1 and saving_count == 0:
            return [name_input, 'income']
        elif income_count == 0 and saving_count == 1:
            return [name_input, 'saving']
        elif income_count == 1 and saving_count == 1:
            choice_result = choose_income_or_savings(name_input, income_goals, saving_goals)
            if choice_result == 'income' or choice_result == 'saving':
                return [name_input, choice_result]
            else:
                return 1
        else:
            print("\nYou did not enter the name of a goal.")

# Gets a new name for the goal if required.
def get_edit_goal_name(current_saving_goals, goal_name):
    """
    Gets the new name of a saving goal.

    Args:
        current_saving_goals: A list of the existing saving goals. (list of tuples of str, floats)
        goal_name: The name of the goal to be edited. (str)
        
    Returns:
        new_name_input: The new name for a saving goal. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    # Checks if the user wants to edit the goal name.    
    while True:
        print('')
        confirm_input = input(f'''The name of the goal is {global_utils.name_capitalise(goal_name)}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Prints a list of current goal names.
    print('\nThe current goal names are:')
    for goal in current_saving_goals:
        print(global_utils.name_capitalise(goal[0]))

    # Gets a new name if needed.
    while True:
        print('')
        new_name_input = input(f'''Please enter a new name for the goal. It must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if new_name_input == '0':
            return 1
        if new_name_input in current_saving_goals:
            print("\nThe goal name you entered matches an existing name.")
            continue
        return new_name_input

# Gets a new target amount for the goal if required. 
def get_edit_goal_target(goal_target):
    """
    Gets a new target amount for a goal.

    Args:
        goal_target: The old target for the goal. (float)
        
    Returns:
        new_amount: The new amount for the goal target. (float)
        1: If the user wishes to return to the previous menu. (int)
    """
    # Checks if the user wants to edit the goal target.
    while True:
        print('')
        confirm_input = input(f'''The target value of the goal is {global_utils.amount_format(goal_target)}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Gets a new target amount if required.
    while True:
        print('')
        new_target_amount_input = input('''Please enter the new target value. Enter 0 to return to the previous menu.
: ''').lower()
        if new_target_amount_input == '0':
            return 1
        if len(new_target_amount_input[new_target_amount_input.rfind('.')+1:]) != 2:
            print("Please enter a valid amount.")
            continue
        try:
            new_amount = float(new_target_amount_input)
        except ValueError:
            print("Please enter a valid amount.")
            continue
        return new_amount

# Gets a new progress amount for the goal if required.
def get_edit_goal_progress(goal_progress):
    """
    Gets a new progress amount for a goal.

    Args:
        goal_progress: The current progress amount for a goal. (float)
        
    Returns:
        new_amount: The new amount for the progress. (float)
        1: If the user wishes to return to the previous menu. (int)
    """
    # Checks if the user wants to edit the goal progress.
    while True:
        print('')
        confirm_input = input(f'''Your progress towards the goal is {global_utils.amount_format(goal_progress)}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Gets a new progress amount if required.
    while True:
        print('')
        new_progress_amount_input = input('''Please enter the new amount. Enter 0 to return to the previous menu.
: ''').lower()
        if new_progress_amount_input == '0':
            return 1
        if len(new_progress_amount_input[new_progress_amount_input.rfind('.')+1:]) != 2:
            print("Please enter a valid amount.")
            continue
        try:
            new_amount = float(new_progress_amount_input)
        except ValueError:
            print("Please enter a valid amount.")
            continue
        return new_amount

# Gets the name of the goal to delete.
def get_goal_to_delete(income_goals, saving_goals):
    """
    Gets the name of a goal to delete.

    Args:
        income_goals: A list of the existing income goals. (list of tuples of str, floats)
        saving_goals: A list of the existing saving goals. (list of tuples of str, floats)    
        
    Returns:
        [name_input, choice_result]: A list of the name of the goal and the name of either income or saving. (list of str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        name_input = input('''Please enter the name of the goal you want to delete. Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        income_count = 0
        saving_count = 0
        for goal in income_goals:
            if name_input == goal[0]:
                income_count += 1
        for goal in saving_goals:
            if name_input == goal[0]:
                saving_count += 1
        if income_count == 1 and saving_count == 0:
            return [name_input, 'income']
        elif income_count == 0 and saving_count == 1:
            return [name_input, 'saving']
        elif income_count == 1 and saving_count == 1:
            choice_result = choose_income_or_savings(name_input, income_goals, saving_goals)
            if choice_result == 'income' or choice_result == 'saving':
                return [name_input, choice_result]
            else:
                return 1
        else:
            print("\nYou did not enter the name of a goal.")

# Gets the name of the goal to add to.
def get_goal_to_add_to(saving_goals):
    """
    Gets the name of a goal to add money to.

    Args:
        saving_goals: A list of the existing saving goals. (list of tuples of str, floats)    
        
    Returns:
        goal_input: The name of the goal to add money to. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        goal_input = input('''Please enter the name of the goal you want to add to. Enter 0 to return to the previous menu.
: ''').lower()
        if goal_input == '0':
            return 1
        for goal in saving_goals:
            if goal_input in goal:
                return goal_input
        else:
            print("\nYou did not enter the name of a goal.")

# Gets the amount to add to the goal.
def get_amount_to_add_to_goal():
    """
    Gets the amount of money to add to a goal.

    Args:
        None    
        
    Returns:
        amount: The amount of money to add to a goal. (float)
        1: If the user wishes to return to the previous menu. (int)
    """
    while True:
        print('')
        amount_input = input('''Please enter the amount you want to add to this goal. Enter 0 to return to the previous menu.
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

# Gets the choice if a goal is present in both the income and saving goals lists.
def choose_income_or_savings(name):
    """
    Gets a choice if a goal is present in both the income goals and saving goals lists.

    Args:
        name: The goal name. (str)    
        
    Returns:
        'saving' / 'income': The choice the user chooses. (str)
        1: If the user wishes to return to the previous menu. (int)
    """
    print(f"\n{global_utils.name_capitalise(name)} is present as both a saving goal and an income goal.")
    while True:
        choice_input = input('''Please enter 'saving' to select the saving goal, or 'income' to select the income goal.
Enter 0 to return to the previous menu.
: ''').lower()
        if choice_input == '0':
            return 1
        elif choice_input == 'saving':
            return 'saving'
        elif choice_input == 'income':
            return 'income'
        else:
            print('\nYour answer was not recognised.\n')

# Updates the income goals when income is updated.
def update_income_goals():
    """
    Updates all income goals based on the latest database information.

    Args:
        None    
        
    Returns:
        None
    """
    # Get list of current income categories.
    current_income_cats = income_db.get_cat_list()
    # If the list is not empty (there might be no categories added).
    if len(current_income_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_cats[0] == 1:
            print("\nSorry, something went wrong accessing the income categories database.")
            print(f"Error: {current_income_cats[1]}")
            return
    else:
        # Returns if there are no income categories.
        return

    for cat in current_income_cats:
        # Gets the goal info for a category if it exists.
        old_goal_info = goals_db.get_goal_info(cat)
        if len(old_goal_info) == 0:
            continue
        # Gets the total income for that category.
        cat_income = income_db.get_cat_income(cat)
        # Makes the tuple of old_goal_info into a list.
        new_goal_info = []
        for goal in old_goal_info:
            for item in goal:
                new_goal_info.append(item)
        # Removes the progress number from goal_info and adds on the new. updated number. 
        new_goal_info.pop()
        new_goal_info.append(cat_income)

        # Updates the goal in the database.
        update_goal_result = goals_db.update_goal(cat, new_goal_info)
        # If update_goal() has returned an error.
        if update_goal_result[0] == 1:
            print(f"\nSorry, something went wrong updating the {global_utils.name_capitalise(cat)} goal.")
            print(f"Error: {update_goal_result[1]}")
             