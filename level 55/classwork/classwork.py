# 1 codewras

def small_enough(array, limit):
    return max(array) <= limit


# 2 codewars


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# 3 codewars

def is_square(n):    
    if n>=0:
        print(str(math.sqrt(n)))
        print(str(math.sqrt(n))[-2::])
    if n>= 0 and str(math.sqrt(n))[-2::] == '.0':
        return True
    else: return False