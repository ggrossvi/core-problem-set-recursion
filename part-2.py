# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array,query):
    #base case 
    print(array)
    if array == []:    
        return False
        
    if array[0] == query:
        return True
        
        
    return search(array[1:], query)
        
""" These are both the same
assert search([], "a") == False
assert not seach([], "a")
"""
    



# is_palindrome
def is_palindrome(text):
    #base case -- stoping point
    print(text)
    if len(text) == 1:
        return True
    if len(text) == 0:
        return True
    if text[0] != text[-1]:   
        return False
        
    return is_palindrome(text[1:-1])
        



# digit_match

def digit_match(param1,param2):
    #base case
    print(param1,param2)
    if param1 == 0 and param2 == 0: 
        return 1 
    
    if param1 == 0 or param2 == 0:
        return 0
        
    last_digit_param1 = param1  % 10  
    last_digit_param2 = param2 % 10
    
    param1 = param1 // 10
    param2 = param2 // 10
    if param1 == 0 and param2 == 0: 
        if last_digit_param1 == last_digit_param2:
            return 1 
        else:
            return 0
        
    if last_digit_param1 == last_digit_param2:
        return 1 + digit_match(param1,param2)
    return 0 + digit_match(param1,param2)
   
        
        
    
    
    


