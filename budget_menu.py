import budget_utils
import expenses_db
import expenses_menu
import global_utils

# Contains all the menu functions for the budget section.

def main_menu():
    """
    Lets the user select a budget option.

    Args:
        None

    Returns:
        None
    """
    print("\nBudgeting Options")

    while True:
        user_input = input('''\nPlease select from one of the following options:
1 - Set or edit an expense budget
2 - View expense budgets
3 - Add a new expense category
4 - Delete an expense category 
0 - Return to previous menu
: ''')

        # Sets or edits a budget.
        if user_input == '1':
            edit_budget()

        # View all budgets.
        elif user_input == '2':
            view_budget()

        # Add a new expense category.
        elif user_input == '3':
            expenses_menu.add_category()

        # Delete an expense category.
        elif user_input == '4':
            expenses_menu.delete_category()

        # Return to previous menu.
        elif user_input == '0':
            return
        
# Sets or edits a budget.
def edit_budget():
    """
    Sets or edits a budget for an expense category.

    Args:
        None
        
    Returns:
        None
    """
    # Get list of current expense categories.
    current_expense_cats = expenses_db.get_cat_list()
    # If the list is empty.
    if len(current_expense_cats) == 0:
        print("\nYou haven't added any expense categories.")
        return
    # If the list is not empty.
    elif len(current_expense_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_cats[0] == 1:
            print("\nSorry, something went wrong accessing the expense categories database.")
            print(f"Error: {current_expense_cats[1]}")
            return
    
    # Prints a list of expense categories and their budgets.
    if len(current_expense_cats) != 0:
        print("\nThe current expense categories are:")
        print("\nCategory -- Budget")
        for expense_cat in current_expense_cats:
            # Changes the budget depending on what it is.
            expense_cat_budget_ph = str(expense_cat[1])
            if expense_cat_budget_ph == '0.0':
                expense_cat_budget_ph = 'N/A'
            # Prints the categories and budgets.
            print(f'{global_utils.name_capitalise(expense_cat[0])} -- {global_utils.amount_format(expense_cat_budget_ph)}')

    # Gets the expense category to set the budget of.
    cat_to_set = budget_utils.get_cat_to_set(current_expense_cats)
    # If the result is 1, return to the previous menu.
    if cat_to_set == 1:
        return
    
    # Gets the budget to set.
    budget_to_set = budget_utils.get_budget_to_set(cat_to_set)
    # If the result is 1, return to the previous menu.
    if budget_to_set == 1:
        return
    
    # Edits the budget of an expense category.
    edit_cat_result = expenses_db.update_cat_budget(cat_to_set, budget_to_set)
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(edit_cat_result) == 0:
        print(f"\nAn unexpected error occurred while trying to edit {global_utils.name_capitalise(cat_to_set)}.")
        return
    
    # If successful, the first index of the result list is 0.
    if edit_cat_result[0] == 0:
        print(f"\n{global_utils.name_capitalise(cat_to_set)}'s budget was successfully set.")
        return
    # If unsuccessful, the first index will be 1.
    elif edit_cat_result[0] == 1:
        print(f"\nSorry, something went wrong and {global_utils.name_capitalise(cat_to_set)} could not be changed.")
        print(f"Error: {edit_cat_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to edit {global_utils.name_capitalise(edit_cat_result)}.")
        return

# Shows budgets.
def view_budget():
    """
    Views expense category budgets.

    Args:
        None
        
    Returns:
        None
    """
    # Get list of current expense categories.
    current_expense_cats = expenses_db.get_cat_list()
    # If the list is empty.
    if len(current_expense_cats) == 0:
        print("\nYou haven't added any expense categories.")
        return
    # If the list is not empty.
    elif len(current_expense_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_cats[0] == 1:
            print("\nSorry, something went wrong accessing the expense categories database.")
            print(f"Error: {current_expense_cats[1]}")
            return
        
    # Gets a list of all expenses.
    expense_data = expenses_db.get_all_expenses()
    # If the list is not empty.
    if len(expense_data) != 0:
        # If the get_cat_list() function has returned an error.
        if expense_data[0] == 1:
            print("\nSorry, something went wrong accessing the expenses database.")
            print(f"Error: {expense_data[1]}")
            return
    
    # Creates an empty list of cat data.
    cat_data = []
    # Adds expense data to the category: [[cat_name_0], [cat_budget_0], [expense_data_0], [expense_data_1]...],
    # [[cat_name_1], [cat_budget_1], [expense_data_0], [expense_data_1]...].
    for cat in current_expense_cats:
        temp_cat_data = []
        temp_cat_data.append(cat[0])
        temp_cat_data.append(cat[1])
        for expense in expense_data:
            # If the name of the category is the same as the expense category.
            if cat[0] == expense[0]:
                temp_cat_data.append(expense)
        cat_data.append(temp_cat_data)

    # Calculates how the expenses in a category compare to the budget.
    for cat in cat_data:
        budget = cat[1]
        total = 0.0
        # Adds the expense amounts to the running total.
        for count, expense_data in enumerate(cat):
            if count <= 1:
                continue
            else:
                total += expense_data[2]
        # Gets a difference.
        diff = str(abs(total - budget))
        # Adds an extra 0 if required.
        if diff[-2] == '.':
            diff = diff + '0'

        # Chooses a comment for the category.
        if budget == 0.0:
            comment = "You haven't added a budget yet."
        elif budget > 0.0 and total == 0.0:
            comment = "You haven't added any expenses to this category." 
        elif budget > 0.0 and total > 0.0 and total < budget:
            comment  = f'You are {diff} under your budget.'
        elif budget > 0.0 and total > 0.0 and total > budget:
            comment = f'You are {diff} over your budget!'
        elif budget > 0.0 and total > 0.0 and total == budget:
            comment = "You've spent all your budget."
        else:
            comment = "We don't have a comment for you."
        cat.append(comment)
    
    # Prints a list of expense categories, their budgets, and a comment.
    if len(current_expense_cats) != 0:
        print("\nThe current expense categories are:")
        print("\nCategory -- Budget -- Comment")
        for cat in cat_data:
            # Changes the budget depending on what it is.
            cat_budget = str(cat[1])
            if cat_budget == '0.0':
                cat_budget = 'N/A'
            # Prints the catgeories and budgets.
            print(f'{global_utils.name_capitalise(cat[0])} -- {global_utils.amount_format(cat_budget)} -- {cat[-1]}')

    # Gets the expense category to view a breakdown for.
    cat_to_view = budget_utils.get_cat_to_view(current_expense_cats)
    # If the result is 1, return to the previous menu.
    if cat_to_view == 1:
        return
    
    # Prints a breakdown of the category for the user.
    budget_utils.cat_breakdown(cat_to_view, cat_data)