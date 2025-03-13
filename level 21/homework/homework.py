fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("List of fruits is: " + str(fruits))

print(fruits[0])

print(fruits[4])

fruits.append("fig")

fruits.remove("banana")

fruits.insert(1,"blueberry")

print("Updated list of fruits is: " + str(fruits))

print(len(fruits))
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

numbers.append(100)

numbers.insert(0,5)

numbers.remove(30)

numbers.reverse()

numbers.index(50)

print(numbers.count(20))

print(numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_half = numbers[0:5]

seconf_half = numbers[5:10]

squares = [numbers ** 2 for numbers in numbers]

print(first_half)
print(seconf_half)
print(squares)
temperatures = [72, 68, 75, 70, 78, 74, 71]

print(max(temperatures))

print(min(temperatures))

print(sum(temperatures) // len(temperatures))

above_70 = [temp for temp in temperatures if temp > 70]

print(above_70)