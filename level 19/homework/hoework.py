umber1 = int(input("Enter number #1 : "))
number2 = int(input("Enter number #2 : "))
number3 = int(input("Enter number #3 : "))
number4 = int(input("Enter number #4 : "))
number5 = int(input("Enter number #5 : "))
number6 = int(input("Enter number #6 : "))
number7 = int(input("Enter number #7 : "))
number8 = int(input("Enter number #8 : "))
number9 = int(input("Enter number #9 : "))
number10 = int(input("Enter number #10 : "))

number = []

number += [number]
number += [number2]
number += [number3]
number += [number4]
number += [number5]
number += [number6]
number += [number7]
number += [number8]
number += [number9]
number += [number10]

print("Your entered numbers are: " + str(number))
number1 = int(input("Enter number #1: "))
number2 = int(input("Enter number #2 : "))
number3 = int(input("Enter number #3 : "))
number4 = int(input("Enter number #4 : "))
number5 = int(input("Enter number #5 : "))
print("Yout entered numbers list is: " + str(list))

search_number = int(5)

if search_number in list:
    print(str(search_number) + " is in list")
else:
    print("There is no number in list you entered.")
    list = input("Enter numbers list: ")

print("Your entered numbers list is: " + str(list))