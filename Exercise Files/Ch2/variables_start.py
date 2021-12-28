# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)


# re-declaring the variable works
#f="abc"
#print (f)


# ERROR: variables of different types cannot be combined
#print("this is a string " + str(123))


# Global vs. local variables in functions
def someFunction():
    global f #This is declaring that the f variable is global and changes will be made globally
    f= "def"
    print (f)

someFunction()
print(f)

del (f) #this delets all assignments of variable f
#print (f)