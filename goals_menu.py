import goals_db
import goals_utils
import income_db
import global_utils

# Contains all the menu functions for the goals section.

def main_menu():
    """
    Lets the user select a goals option.

    Args:
        None

    Returns:
        None
    """
    print("\nGoal Options")

    while True:
        user_input = input('''\nPlease select from one of the following options:
1 - Create a saving goal
2 - Create an income goal
3 - Edit a goal
4 - Delete a goal
5 - Add money to saving goal
6 - View all goals 
0 - Return to previous menu
: ''')

        # Creates a saving goal.
        if user_input == '1':
            create_saving_goal()

        # Creates an income goal.
        elif user_input == '2':
            create_income_goal()

        # Edits a goal.
        elif user_input == '3':
            edit_goal()

        # Deletes a goal.
        elif user_input == '4':
            delete_goal()

        # Adds money to a saving goal.
        elif user_input == '5':
            add_to_saving_goal()

        # Views all goals.
        elif user_input == '6':
            view_all_goals()

        # Return to previous menu.
        elif user_input == '0':
            return

# Creates a saving goal.
def create_saving_goal():
    """
    Creates a saving goal.

    Args:
        None

    Returns:
        None
    """
    # Get list of current saving goals.
    current_saving_goals = goals_db.get_goals_list('saving')
    # If the list is not empty (there might be no goals added).
    if len(current_saving_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_saving_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the saving goal names from the database.")
            print(f"Error: {current_saving_goals[1]}")
            return
    
    # Tells the user what's happening.
    print("\nAdding a new saving goal.")

    # If there are goals already in the database, print them out to the user.
    if len(current_saving_goals) != 0:
        print("\nCurrent Saving Goals:")
        print("Name -- Goal Amount -- Current Progress")
        for goal in current_saving_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")

    new_goal_info = []

    # Gets the name of the new goal.
    new_goal_name = goals_utils.get_new_saving_goal_name(current_saving_goals)
    # If the result is 1, return to the previous menu.
    if new_goal_name == 1:
        return
    else:
        new_goal_info.append(new_goal_name)

    # Adds the category of goal to new_goal_info.
    new_goal_info.append('saving')

    # Gets the amount of the new goal.
    new_goal_amount = goals_utils.get_new_goal_amount()
    # If the result is 1, return to the previous menu.
    if new_goal_amount == 1:
        return
    else:
        new_goal_info.append(new_goal_amount)

    # Adds 0.0 to the progress index of the saving goal.
    new_goal_info.append(0.0)

    # Adds the new income to the tracker.
    add_new_goal_result = goals_db.add_goal(new_goal_info)
    if add_new_goal_result[0] == 1:
        print("\nSorry, something went wrong adding the goal to the database.")
        print(f"Error: {add_new_goal_result[1]}")
        return
    elif add_new_goal_result[0] == 0:
        print(f"\n{global_utils.name_capitalise(new_goal_info[0])} was successfully added to the database.")
        return
    else:
        print("\nSorry, an unexpected error has occurred and the goal could not be added to the database.")    

# Creates an income goal.
def create_income_goal():
    """
    Creates an income goal.

    Args:
        None

    Returns:
        None
    """
    # Get list of current income goals.
    current_income_goals = goals_db.get_goals_list('income')
    # If the list is not empty (there might be no goals added).
    if len(current_income_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_income_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the income goals from the database.")
            print(f"Error: {current_income_goals[1]}")
            return
    
    # Get list of current income categories.
    current_income_cats = income_db.get_cat_list()
    # If the list is not empty (there might be no categories added).
    if len(current_income_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_cats[0] == 1:
            print("\nSorry, something went wrong accessing the income categories database.")
            print(f"Error: {current_income_cats[1]}")
            return
    
    # Tells the user what's happening.
    print("\nAdding a new income goal.")

    # If there are goals already in the database, print them out to the user.
    if len(current_income_goals) != 0:
        print("\nCurrent Income Goals:")
        print("Category -- Target Income -- Current Progress")
        for goal in current_income_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")

    # If the list isn't empty, print the current categories.
    if len(current_income_cats) != 0:
        print("\nThe current income categories are:")
        for income_cat in current_income_cats:
            print(global_utils.name_capitalise(income_cat))

    new_goal_info = []

    # Gets the name of the category to add the goal to.
    cat_name = goals_utils.get_cat_name(current_income_cats)
    # If the result is 1, return to the previous menu.
    if cat_name == 1:
        return
    else:
        new_goal_info.append(cat_name)

    # Adds the category of goal to new_goal_info.
    new_goal_info.append('income')

    # Gets the amount of the new goal.
    new_goal_amount = goals_utils.get_new_goal_amount()
    # If the result is 1, return to the previous menu.
    if new_goal_amount == 1:
        return
    else:
        new_goal_info.append(new_goal_amount)

    # Gets the total income of a category.
    new_goal_progress = goals_utils.get_income_of_category(cat_name)
    if new_goal_progress == 1:
        return
    new_goal_info.append(new_goal_progress)

    # Adds the new income to the tracker.
    add_new_goal_result = goals_db.add_goal(new_goal_info)
    if add_new_goal_result[0] == 1:
        print("\nSorry, something went wrong adding the goal to the database.")
        print(f"Error: {add_new_goal_result[1]}")
        return
    elif add_new_goal_result[0] == 0:
        print(f"\nAn income goal for {global_utils.name_capitalise(new_goal_info[0])} was successfully added to the database.")
        return
    else:
        print("\nSorry, an unexpected error has occurred and the goal could not be added to the database.") 

# Edits a goal.
def edit_goal():
    """
    Edits a goal.

    Args:
        None

    Returns:
        None
    """
    # Get list of current saving goals.
    current_saving_goals = goals_db.get_goals_list('saving')
    # If the list is not empty (there might be no goals added).
    if len(current_saving_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_saving_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the saving goal names from the database.")
            print(f"Error: {current_saving_goals[1]}")
            return
        
    # Get list of current income goals.
    current_income_goals = goals_db.get_goals_list('income')
    # If the list is not empty (there might be no goals added).
    if len(current_income_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_income_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the income goal names from the database.")
            print(f"Error: {current_income_goals[1]}")
            return
        
    # If neither list has any goals, tell the user and return.
    if len(current_income_goals) == 0 and len(current_saving_goals) == 0:
        print("\nYou don't have any goals to edit.")
        return
    
    print("\nCurrent Saving Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_saving_goals) != 0:
        print("Name -- Goal Amount -- Current Progress")
        for goal in current_saving_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No saving goals present.")

    print("\nCurrent Income Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_income_goals) != 0:
        print("Category -- Current Income -- Current Progress")
        for goal in current_income_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No income goals present.")

    # Get the name and category of the goal to edit.
    goal_to_edit = goals_utils.get_goal_to_edit(current_income_goals, current_saving_goals)
    # Returns to the previous menu if goal_to_edit returns 1.
    if goal_to_edit == 1:
        return
    
    # Tells the user what's happening.
    print(f"\nYou are editing the {global_utils.name_capitalise(goal_to_edit[0])} {goal_to_edit[1]} goal.")

    # Gets the current goal info.
    if goal_to_edit[1] == 'saving':
        for goal in current_saving_goals:
            for item in goal:
                if goal_to_edit[0] == item:
                    goal_info = list(goal)
    else:
        for goal in current_income_goals:
            for item in goal:
                if goal_to_edit[0] == item:
                    goal_info = list(goal)
    
    new_goal_info = []

    # Gets a change of name if the goal is a saving goal.
    if goal_to_edit[1] == 'saving':
        edited_goal_name = goals_utils.get_edit_goal_name(current_saving_goals, goal_to_edit[0])
        # If the result is 1, return to the previous menu.
        if edited_goal_name == 1:
            return
        # If the result is 2, no change so add current info to new_income_info
        elif edited_goal_name == 2:
            new_goal_info.append(goal_info[0])
        # Otherwise add the new name to new_income_info.
        else:
            new_goal_info.append(edited_goal_name)
    # If it's an income goal as you can't change the category for the goal.
    else:
        new_goal_info.append(goal_info[0])
    
    # Adds the category of the goal to the new info.
    new_goal_info.append(goal_info[1])

    # Gets the change of target value if required.
    edited_target_amount = goals_utils.get_edit_goal_target(goal_info[2])
    # If the result is 1, return to the previous menu.
    if edited_target_amount == 1:
        return
    # If the result is 2, no change so add current info to new_income_info
    elif edited_target_amount == 2:
        new_goal_info.append(goal_info[2])
    # Otherwise add the new amount to new_goal_info.
    else:
        new_goal_info.append(edited_target_amount)

    # Gets a change of progress value if the goal is a saving goal.
    if goal_to_edit[1] == 'saving':
        # Gets the change of saving progress value if required.
        edited_progress_amount = goals_utils.get_edit_goal_progress(goal_info[3])
        # If the result is 1, return to the previous menu.
        if edited_progress_amount == 1:
            return
        # If the result is 2, no change so add current info to new_income_info
        elif edited_progress_amount == 2:
            new_goal_info.append(goal_info[3])
        # Otherwise add the new amount to new_goal_info.
        else:
            new_goal_info.append(edited_target_amount)
    # If the goal is income, the progress is calculated automatically so can't be changed.
    else:
        new_goal_info.append(goal_info[3])
        
    # Checks if anything has changed. If not, returns.
    if goal_info == new_goal_info:
        print("\nNo changes were made to the goal.")
        return
    
    # Updates the income with the new info.
    edit_goal_result = goals_db.update_goal(goal_to_edit[0], new_goal_info)
    if edit_goal_result[0] == 1:
        print("\nSorry, something went wrong while updating the goal.")
        print(f"Error: {edit_goal_result[1]}")
        return
    if edit_goal_result[0] == 0:
        print(f"\n{global_utils.name_capitalise(new_goal_info[0])} has been successfully updated.")
    else:
        print("\nSorry, an unexpected error has occurred and the goal could not be updated.")

# Deletes a goal.
def delete_goal():
    """
    Deletes a goal.

    Args:
        None

    Returns:
        None
    """
    # Get list of current saving goals.
    current_saving_goals = goals_db.get_goals_list('saving')
    # If the list is not empty (there might be no goals added).
    if len(current_saving_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_saving_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the saving goal names from the database.")
            print(f"Error: {current_saving_goals[1]}")
            return
        
    # Get list of current income goals.
    current_income_goals = goals_db.get_goals_list('income')
    # If the list is not empty (there might be no goals added).
    if len(current_income_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_income_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the income goal names from the database.")
            print(f"Error: {current_income_goals[1]}")
            return
        
    # If neither list has any goals, tell the user and return.
    if len(current_income_goals) == 0 and len(current_saving_goals) == 0:
        print("\nYou don't have any goals to delete.")
        return
    
    print("\nCurrent Saving Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_saving_goals) != 0:
        print("Name -- Goal Amount -- Current Progress")
        for goal in current_saving_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No saving goals present.")

    print("\nCurrent Income Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_income_goals) != 0:
        print("Category -- Current Income -- Current Progress")
        for goal in current_income_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No income goals present.")

    # Get the name and category of the goal to delete.
    goal_to_delete = goals_utils.get_goal_to_delete(current_income_goals, current_saving_goals)
    # Returns to the previous menu if goal_to_delete returns 1.
    if goal_to_delete == 1:
        return
    
    # Tells the user what's happening.
    print(f"\nDeleting {global_utils.name_capitalise(goal_to_delete[0])} from the database...")

    # Deletes the existing goal from the database.
    delete_goal_result = goals_db.delete_goal(goal_to_delete[0], goal_to_delete[1])
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(delete_goal_result) == 0:
        print(f"\nAn unexpected error occurred while trying to delete {global_utils.name_capitalise(goal_to_delete[0])} from the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if delete_goal_result[0] == 0:
        print(f"\n{global_utils.name_capitalise(goal_to_delete[0])} was successfully deleted from the database.")
    # If unsuccessful, the first index will be 1.
    elif delete_goal_result[0] == 1:
        print(f"\nSorry, something went wrong and {global_utils.name_capitalise(goal_to_delete[0])} could not be deleted from the database.")
        print(f"Error: {delete_goal_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to delete {global_utils.name_capitalise(goal_to_delete[0])} from the database.")
        return
    

# Adds money to a saving goal.
def add_to_saving_goal():
    """
    Adds money into a saving goal.

    Args:
        None

    Returns:
        None
    """
    # Get list of current saving goals.
    current_saving_goals = goals_db.get_goals_list('saving')
    # If the list is not empty (there might be no goals added).
    if len(current_saving_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_saving_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the saving goal names from the database.")
            print(f"Error: {current_saving_goals[1]}")
            return
        
    print("\nCurrent Saving Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_saving_goals) != 0:
        print("Name -- Goal Amount -- Current Progress")
        for goal in current_saving_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user and return to the previous menu.
    else:
        print("No saving goals present.")
        return
    
    # Get the name of the goal to add to.
    goal_to_add_to = goals_utils.get_goal_to_add_to(current_saving_goals)
    # Returns to the previous menu if goal_to_add_to returns 1.
    if goal_to_add_to == 1:
        return
    
    # Gets the amount of money to add to the goal.
    amount_to_add = goals_utils.get_amount_to_add_to_goal()
    # Returns to the previous menu if amount_to_add returns 1.
    if amount_to_add == 1:
        return
    
    # Gets the amount currently saved.
    for goal in current_saving_goals:
        if goal_to_add_to == goal[0]:
            current_amount_saved = goal[3]

    # Adds the amount of money to add to the amount currently saved.
    new_amount = amount_to_add + current_amount_saved

    # Updates the goal to include the new amount.
    update_saving_goal_result = goals_db.update_saving_goal_progress(goal_to_add_to, new_amount)
    if update_saving_goal_result[0] == 1:
        print("\nSorry, something went wrong adding money to your goal.")
        print(f"Error: {update_saving_goal_result[1]}")
        return
    elif update_saving_goal_result[0] == 0:
        print(f"\n{global_utils.amount_format(amount_to_add)} has been added to {global_utils.name_capitalise(goal_to_add_to)}.")
        return
    else:
        print("\nSorry, an unexpected error has occurred and the goal could not be updated.") 

# Views all goals.
def view_all_goals():
    """
    Prints all goals to the user.

    Args:
        None

    Returns:
        None
    """
    # Get list of current saving goals.
    current_saving_goals = goals_db.get_goals_list('saving')
    # If the list is not empty (there might be no goals added).
    if len(current_saving_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_saving_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the saving goal names from the database.")
            print(f"Error: {current_saving_goals[1]}")
            return
        
    # Get list of current income goals.
    current_income_goals = goals_db.get_goals_list('income')
    # If the list is not empty (there might be no goals added).
    if len(current_income_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_income_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the income goal names from the database.")
            print(f"Error: {current_income_goals[1]}")
            return
        
    # If neither list has any goals, tell the user and return.
    if len(current_income_goals) == 0 and len(current_saving_goals) == 0:
        print("\nYou don't have any goals to view.")
        return
    
    print("\nCurrent Saving Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_saving_goals) != 0:
        print("Name -- Goal Amount -- Current Progress")
        for goal in current_saving_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No saving goals present.")

    print("\nCurrent Income Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_income_goals) != 0:
        print("Category -- Current Income -- Current Progress")
        for goal in current_income_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No income goals present.")