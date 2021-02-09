#Instructions: Write a function called repeat_str which repeats the given 
# string src exactly count times.

#Method One:

def repeat_str(repeat, string):
    repeated = ""
    for i in range(repeat):
        repeated += string
    return repeated


#Method Two:

def repeat_str(repeat, string):
    return string*repeat
