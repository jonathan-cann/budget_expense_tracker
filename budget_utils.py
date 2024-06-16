# Utility functions for the budget part of the tracker.
import global_utils

# Gets the name of the expense category to change the budget of.
def get_cat_to_set(expense_categories):
    """
    Gets the name of the expense category to change the budget of.

    Args:
        expense_categories: A list of the names of expense categories (list of str).
        
    Returns:
        cat_input: The name of the category the user wishes to change the budget of (str).
        1: If the user wishes to return to the previous menu (int).
    """
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you wish to change the budget of.
Enter 0 to return to the previous menu.
: ''')
        if cat_input == '0':
            return 1
        for cat in expense_categories:
            if cat_input == cat[0]:
                return cat_input
        print("\nThe name you entered does not match an existing category.")

# Gets the name of a category the user would like to view a breakdown of.
def get_cat_to_view(expense_categories):
    """
    Gets the name of a category the user would like to view a breakdown of.

    Args:
        expense_categories: A list of the names of expense categories (list of str).
        
    Returns:
        cat_input: The name of the category the user wishes to view the breakdown of (str).
        1: If the user wishes to return to the previous menu (int).
    """
    while True:
        print('')
        cat_input = input('''If you'd like to view the breakdown for a particular category, enter its name now.
Otherwise, enter 0 to return to the previous menu.
: ''')
        if cat_input == '0':
            return 1
        for cat in expense_categories:
            if cat_input == cat[0]:
                return cat_input
        print("\nThe name you entered does not match an existing category.")

# Gets the budget for a category from the user.
def get_budget_to_set(expense_category):
    """
    Gets the budget for a category from the user.

    Args:
        expense_category: The name of the expense category whose budget is being set (str).
        
    Returns:
        budget: The value of the category budget (float).
        1: If the user wishes to return to the previous menu (int).
    """
    while True:
        print('')
        budget_input = input(f'''Please enter a budget for {global_utils.name_capitalise(expense_category)}. Enter 0 to return to the previous menu.
: ''').lower()
        if budget_input == '0':
            return 1
        if len(budget_input[budget_input.rfind('.')+1:]) != 2:
            print("\nPlease enter a valid amount.")
            continue
        try:
            budget = float(budget_input)
        except ValueError:
            print("\nPlease enter a valid amount.")
            continue
        return budget

# Shows the user a breakdown of a selected category.    
def cat_breakdown(category_name, cat_data):
    """
    Shows the user a breakdown of a selected category.

    Args:
        category_name: The name of the category to be broken down (str).
        cat_data: Category data from the database (list of tuples of strings and floats).
        
    Returns:
        None
    """
    # Gets rid of the rest of the category data.
    for cat in cat_data:
        if category_name == cat[0]:
            current_cat_data = cat
            break

    expense_total = 0.0

    print(f'\n{global_utils.name_capitalise(cat[0])} Expense Category Breakdown:')

    if cat[1] == 0.0:
        print("\nYou haven't set a budget for this category.")
    else:
        budget = str(cat[1])
        if budget[-2:] == '.0':
            budget = budget + '0'
        print(f'\nBudget: {budget}')

    if len(cat) == 3:
        print("\nYou haven't added any expenses to this category,")
    else:
        print('\nExpenses:')
        print('    Name -- Amount -- Date Added')
        for item in current_cat_data:
            if type(item) is tuple:
                expense_total += item[2]
                amount = str(item[2])
                if amount[-2:] == '.0':
                    amount = amount + '0'
                print(f'    {global_utils.name_capitalise(item[1])} -- {amount} -- {item[3]}')

        expense_total = str(expense_total)
        if expense_total[-2:] == '.0':
            expense_total = expense_total + '0'
        print(f'\nExpense Total: {expense_total}')

        print(f"\n{current_cat_data[-1]}")