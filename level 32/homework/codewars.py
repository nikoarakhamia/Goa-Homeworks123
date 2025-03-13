# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

def between(a,b):
    list = []
    for i in range(a,b + 1):
        list.append(i)
    return list

# Complete the solution so that it reverses the string passed into it.

def solution(string):
    return string[::-1]

# Implement a function which convert the given boolean value into its string representation. Note: Only valid inputs will be given.

def boolean_to_string(b):
    return str(b)

# Unfinished Loop - Bug Fixing #1. Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res +=[i]
        i = i + 1
    return res

# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number. For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

def quarter_of(month):
    if month < 4:
        return 1
    elif 3 < month < 7:
        return 2
    elif 6 < month < 10:
        return 3
    else:
        return 4