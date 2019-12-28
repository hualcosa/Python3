#1 Create a new list named double_nums by multiplying each number in nums by two.
nums = [4, 8, 15, 16, 23, 42]
double_nums = [num*2 for num in nums]
print(double_nums)

#2 You’ve been given a list of the numbers between 0 and 10. We created this list using the range function!
# Create a new list named squares that contains the square of every number in this list.
nums = range(11)
squares = [number**2 for number in nums]
print(nums, squares)

#3 Create a new list named add_ten that adds ten to every element in the list nums.
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num + 10 for num in nums]
print(nums)
print(add_ten)

#4 Create a new list named divide_by_two that contains half of every element in the list nums.
nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [el/2 for el in nums]
print(nums)
print(divide_by_two)

#5 Create a new list named parity that contains a 1 or a 0 for each element of nums. For each element,
# if that element was even, the new list should contain a 0. If the element was odd, the new list should contain a 1.
nums = [4, 8, 15, 16, 23, 42]
parity = [el % 2 for el in nums]
print(nums)
print(parity)

#6 Create a new list named greetings that adds "Hello, " in front of each name in the list names.
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + name for name in names]
print(names)
print(greetings)

#7 Create a new list named first_character that contains the first character from every name in the list names
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]
print(names)
print(first_character)

#8 Create a new list named lengths that contains the size of each name in the list of names
names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]
print(names)
print(lengths)

#9 Create a new list named opposite that contains the opposite boolean for each element in the list booleans.
booleans = [True, False, True]
opposite = [not el for el in booleans]
print(booleans)
print(opposite)

#10 Create a new list called is_Jerry, in which an entry at position i is True if the entry in names
# at position i equals "Jerry". The entry should be False otherwise
names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name == "Jerry" for name in names]
print(names)
print(is_Jerry)

#11 Create a new list called greater_than_two, in which an entry at position i is True
# if the entry in nums at position i is greater than 2.
nums = [5, -10, 40, 20, 0]
greater_than_two = [num > 2 for num in nums]
print(nums)
print(greater_than_two)

#12 Create a new list named product that contains the product of each sub-list of nested_lists.
nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [item1 * item2 for (item1, item2) in nested_lists]
print(nested_lists)
print(product)

#13 Create a new list named greater_than that contains True if the first number in
# the sub-list is greater than the second number in the sub-list, and False otherwise.
nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than =[item1 > item2 for (item1, item2) in nested_lists]
print(nested_lists)
print(greater_than)

#14 Create a new list named first_only that contains the first element in each sub-list of nested_lists.
nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [item1 for (item1, item2) in nested_lists]
print(nested_lists)
print(first_only)

#15 Use list comprehension and the zip function to create a new list
#  named sums that sums corresponding items in lists a and b
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [e1 + e2 for (e1, e2) in zip(a, b)]
print(sums)

# 16 Use list comprehension and the zip function to create a new list named quotients
# that divides the elements in list b by those in list a
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [e1/e2 for (e1, e2) in zip(b, a)]
print(quotients)

# 17 You’ve been given two lists: a list of capitals and a list of countries. Create a new list
# named locations that contains the string "capital, country" for each item in the original lists.
capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = [capital + ", " + country for (capital, country) in zip(capitals, countries)]
print(locations)

# 18 You’ve been given two lists: a list of names and a list of ages. Create a new list named users that contains the string
# "Name: name, Age: age" for each pair of elements in the original lists. For example, if the 5th item in the names list is "John"
# and the 5th item in ages is 42, then the 5th item in the new list should be "Name: John, Age: 42".
names = ["Jon", "Arya", "Ned"]
ages = [14, 9, 35]
users = ["Name: " + name + ", Age: " + str(age) for (name, age) in zip(names, ages)]
print(users)

# 19 Create a new list named greater_than that contains True or False depending on whether
# the corresponding item in list a is greater than the one in list b.
a = [30, 42, 10]
b = [15, 16, 17]
greater_than = [i1 > i2 for (i1, i2) in zip(a, b)]
print(greater_than)
