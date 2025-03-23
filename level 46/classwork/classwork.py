# 1 codewars

def repeats(arr):
    one_sum = []
    for i in arr:
        if arr.count(i) == 1:
            one_sum.append(i)
    return sum(one_sum)

# 2 codewars 

def litres(time):
    return time // 2

# 3 codewars

def cat_mouse(x):
    n = x.count(".")
    if n <= 3:
        return ("Caught!")
    if n > 3:
        return ("Escaped!")
    
