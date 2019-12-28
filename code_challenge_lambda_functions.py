# this is a code challenge about basic lambda functions that i've done
# during my data science path on Codecademy

# Create a lambda function named contains_a that takes an input word and returns
# True if the input contains the letter 'a'. Otherwise, return False.
contains_a = lambda input: 'a' in input

print(contains_a("banana")) 
print(contains_a("apple")) 
print(contains_a("cherry")) 

# Create a lambda function named long_string that takes an input str and returns
# True if the string has over 12 characters in it. Otherwise, return False.
long_string = lambda str: True if len(str) > 12 else False
print(long_string("short")) 
print(long_string("photosynthesis")) 

# Create a lambda function named ends_in_a that takes an input str and returns True
# if the last character in the string is an a. Otherwise, return False.
ends_in_a = lambda str: True if str[-1] is 'a' else False
print(ends_in_a("data"))
print(ends_in_a("aardvark")) 

# Create a lambda function named double_or_zero that takes an integer named num. 
# If num is greater than 10, return double num. Otherwise, return 0.
double_or_zero = lambda num: num*2 if num > 10 else 0
print(double_or_zero(15)) 
print(double_or_zero(5)) 

# Create a lambda function named even_or_odd that takes an integer named num.
#  If num is even, return "even". If num is odd, return "odd".
even_or_odd = lambda num: 'even' if num%2 == 0 else 'odd'
print(even_or_odd(10)) 
print(even_or_odd(5)) 

# Create a lambda function named multiple_of_three that takes an integer named num. 
# If num is a multiple of three, return "multiple of three". Otherwise, return "not a multiple".
multiple_of_three = lambda num: 'multiple of three' if num%3 == 0 else 'not a multiple'
print multiple_of_three(9)
print multiple_of_three(10)

# Create a lambda function named rate_movie that takes a number named rating.
# If rating is greater than 8.5, return "I liked this movie". Otherwise return "This movie was not very good".
rate_movie = lambda rating: 'I liked this movie' if rating > 8.5 else 'This movie was not very good'
print rate_movie(9.2)
print rate_movie(7.2)

# Create a lambda function named ones_place that returns the ones’ place of the input num.
ones_place = lambda num: num%10
print ones_place(123)
print ones_place(4)

# Create a lambda function named double_square that takes an input named num. The function 
# should return twice the square of num.
double_square = lambda num: 2 * num**2

print double_square(5)
print double_square(3)

# Create a lambda function named add_random that takes an input named num. The function should
# return num plus a random integer number between 1 and 10 (inclusive).
import random
add_random = lambda num: num + random.randint(1,10)
print add_random(5)
print add_random(100)
