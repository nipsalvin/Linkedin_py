#
# Example file for working with functions
#

# define a basic function
def func1():
    print ("I am function 1")

# function that takes 2 arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x = 1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args): # the * character means you can pas a variable number of arguments
    result = 0
    for x in args:
        result = result + x
    return result

func1()
print(func1()) #Takes self arg
print (func1) 

func2(10, 20)
print(func2(10, 20))
print(cube(3)) #asssigns 3 to arg x 
print (power(2)) #arg num is assigned 2 without power 'x'
print (power(2, 3)) #arg num is assigned 2 and x is assigned 3
print (power (x=3, num=2))
print (multi_add(2, 3, 10, 15, 70))