#Instructions: Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    #seperate the string into characters
    #remove the character at position 0 and position -1
    #return that string
    '''
    Method 1: 
    seperate = list(s)
    del seperate[0]
    del seperate[-1]
    return "".join(seperate)
    '''
    #Method 2:
    '''
    seperate = list(s)
    return "".join(seperate[1:-1])
    '''
    #Method 3:
    return s[1:-1]