"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

def name_of_town(town):
    """Determines if the town name provided matches hometown"""
    hometown = 'mumbai'
    if town == hometown:
        return True
    else:
        return False


def name(first_name, last_name):
    """Joins the first and last name together in one string"""
    return first_name + ' ' + last_name


def name_and_place(hometown, first_name, last_name):
    """ Uses the functions above to see if the hometown provided here matches the one in the first function and prints an appropriate message"""
    
    if name_of_town(hometown) == True:
        print "Hi," + name(first_name,last_name) + ", we're from the same place!"
    else:
        print "Hi," + name(first_name, last_name) + ", I'd like to visit " + hometown


    


###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    if fruit == 'strawberry' or fruit == 'raspberry' or fruit == 'blackberry':  
        return True
    else:
        return False



def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """
    #returns 0 if the is_berry() function returns true and 5 if the is_berry() function returns false
    if is_berry(fruit) == True:
        return 0
    elif is_berry(fruit) == False:
        return 5



def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """
    new_list = []
    #adding the num argument to the end of the new list
    new_list = lst + [num]
    return new_list


#tax_rate is the optional variable
def calculate_price(base_price, state_abbr, tax_rate = 0.05):               
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """
    total_price = 0
    #using if conditions to check if a fee needs to be added based on the state_abbr
    if state_abbr == 'CA':
        total_price_before_fee = base_price + (tax_rate * base_price) 
        # added the state fee to the cost with tax
        total_price = total_price_before_fee + total_price_before_fee * 0.03    
        return total_price
    elif state_abbr == 'PA':
        #added the highway safety fee for PA
        total_price = base_price + (tax_rate * base_price) + 2                  
        return total_price
    elif state_abbr == 'MA':
        if base_price < 100:
            # added the commonwealth fund fee for MA based on the base price
            total_price = base_price + (tax_rate * base_price) + 1              
            return total_price
        elif base_price >= 100:
            total_price = base_price + (tax_rate * base_price) + 3
            return total_price
    else:
        total_price = base_price + (tax_rate * base_price)
        return total_price


    


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def append_list(list_name, *args):
    """ Returns a list with multiple arguments appended to the list """
    #looping over each of the multiple arguments passed in
    for arg in args:            
        list_name += [arg] 
    return list_name

def function_outer(word):
    """an outer function with a nested function calls the nested function"""
    def function_inner():
        #returns the argument passed to the outer function three times
        return word * 3
    result = function_inner()
    print tuple([word, result])



###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
