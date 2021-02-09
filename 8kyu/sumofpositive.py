#Instructions: You get an array of numbers, return the sum of all of the positives ones.
 def positive_sum(arr):
    #looking at each number
    #if the number is greater than 0
    #append that to a list that only has positive numbers
    #then add everything within that list
    #return the sum 
    positives = []
    for x in arr: 
        if x > 0:
            positives.append(x)
    return sum(positives)