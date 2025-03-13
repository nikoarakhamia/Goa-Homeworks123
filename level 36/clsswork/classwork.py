def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
[11:41 PM]
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result
