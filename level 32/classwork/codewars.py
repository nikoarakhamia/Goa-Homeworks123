# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

def make_negative( number ):
    if number >= 0:
        return(0 - number)
    else:
        return number


# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

def say_hello(name):
    return f'Hello, {name}'


# When provided with a number between 0-9, return it in words. Note that the input is guaranteed to be within the range of 0-9.

def switch_it_up(number):
    if number == 0:
        return "Zero"
    elif number == 1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"
    
# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

def between(a,b):
    list = []
    for i in range(a,b + 1):
        list.append(i)
    return list
