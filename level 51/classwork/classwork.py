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

def printer_error(s):
    errors = sum(char>"m" for char in s)
    total = len(s)
    return f"{errors}/{total}"