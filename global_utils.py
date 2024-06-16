# Adds some global utility functions.

def name_capitalise(name):
    """
    Capitalises all words of a name for titles.

    Args:
        name: The name to be capitalised. (str)
        
    Returns:
        new_name: The new, capitalised name. (str)
    """ 
    name_list = name.split()
    new_name = ''
    for name in name_list:
        if name[0].islower():
            new_name = new_name + name.capitalize() + ' '
        else:
            new_name = new_name + name + ' '
    new_name = new_name[:-1]
    return new_name

def amount_format(amount):
    """
    Adds an additional 0 to an obtained float value so money can be viewed properly in tables. Only use in place.

    Args:
        amount: The amount that requires an additional 0. (float)
        
    Returns:
        amount: The original amount plus an additional 0. (str)
    """ 
    amount = str(amount)
    if amount[-2] == '.':
        amount = amount + '0'
    return amount