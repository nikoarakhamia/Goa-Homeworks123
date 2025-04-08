# 1 codewars

def open_or_senior(data):
    categorization = []
    for prospective_member in data:
        if prospective_member[0] >= 55 and prospective_member[1] > 7:
            categorization.append("Senior")
        else:
            categorization.append("Open")
    return categorization
        

# 2 codewars

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    root = sq ** 0.5
    return (root + 1) ** 2 if root.is_integer() == True else - 1






# 3 codewars

def row_sum_odd_numbers(n):
    sum_of_odd_integers = []
    for layer in range(1,n+1):
        sum_of_odd_integers.append(layer * layer**2)
    return max(sum_of_odd_integers)







# 4 codewars

def nb_year(p0, percent, aug, p):
    ipop = p0
    years = 0
    while ipop < p:
        ipop = int(ipop + (ipop * (precent * .01)) + aug)
        years += 1
    return years



# 5 codewars

def printer_error(s):
    errors = sum(char>"m" for char in s)
    total = len(s)
    return f"{errors}/{total}"