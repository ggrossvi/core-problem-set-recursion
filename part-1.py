# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    # base case 
    if num < 0:
        raise ValueError("num is less than 0")
    elif num == 0:
        # print("num is 0")
        return 1
        
    # print(num - 1)
    #recursive    
    return factorial(num -1) * num


# reverse

def factorial(num):
    # base case 
    if num < 0:
        raise ValueError("num is less than 0")
    elif num == 0:
        # print("num is 0")
        return 1
        
    # print(num - 1)
    #recursive    
    return factorial(num -1) * num


# bunny

def bunny(count):
    #base case
    if count == 0: 
        return 0
    if count == 1:
        return 2
        
    #recursive  
    return bunny(count-1) + 2


# is_nested_parens

def is_nested_parens(parens):  
    #base cases - stopping condition
    if parens == "":
        return True
    if parens[0] != "(":
        return False
    if parens[-1] != ")":
        return False

    #recursion
    return True and is_nested_parens(parens[1:-1])


