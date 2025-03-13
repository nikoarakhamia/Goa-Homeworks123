# Work 1

# Answer: 4

nums = [2,4,8,9,5] # მოცემულია სია რიცხვითი მნშვნელობებით.

nums.insert(1, 3) # გამოყენებულია insert ფუნქცია, რომლის დახმარებით სიაში ვამატებთ პირველ ინდექსად მდგარ მნიშვნელობას რიცხვითი მნშვნელობა სამით.

nums.remove(9) # გამოყენებილია remove ფუნქცია, რომელიც შლის სიიდან კონკრეტულ რიცხვით მნშვნელობას, ამ შემთხვევაში ცხრას.

nums.insert(0, nums.count(8)) # გამოყენებულია insert ფუნქცია, რომლის დახმარებით სიაში ვამატებთ ნულ ინდექსად მდგარ მნიშვნელობას რიცხვითი მნიშვნელბით, რომელიც მოცემულია count სიის ფუნქციით.

print(nums[3]) # პრინტავს, ანუ გამოაქვს სიაშ მესამე ინდექსად მდგარ მნიშვნელობას (ანუ 4).




# Work 2

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("List of fruits is: " + str(fruits))

print(fruits[0])

print(fruits[4])

fruits.append("fig")

fruits.remove("banana")

fruits.insert(1,"blueberry")

print("Updated list of fruits is: " + str(fruits))

print(len(fruits))



# Work 3

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

numbers.append(100)

numbers.insert(0,5)
