#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while x < 20:
    print (x)
    x = x + 1

  # define a for loop
  for x in range (5 , 11):
    print (x)

  # use a for loop over a collection
  days = ["mon", "tue", "wed" , "thur" , "fri" , "sat", "sun"]
  for x in days:
    print (x)
  
  # use the break and continue statements
  for x in range(5,100):
    if (x == 7): break
    #if x divided by 2 and the remainder is = 0 then skip and proceed to the next one with a remainder thats != 0
    if (x % 2 == 0): continue
    print (x)

  for y in range(10 , 20):
    if (y == 19) :
      break
    if (x <= 20 ):
      continue

  #using the enumerate() function to get index 
  days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
  for i, x in enumerate(days):
    print(i, x)

if __name__ == "__main__":
  main()
