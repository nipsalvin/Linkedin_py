#
# Example file for working with timedelta objects
#

from datetime import date, timedelta
from datetime import time
from datetime import datetime



# construct a basic timedelta and print it
print (timedelta(days=365, hours=10, minutes=5))

# print today's date
now = datetime.now()
print("today is: " + str(now))

# print today's date one year from now
print("One year from now it will be: "+ str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print ("in 2 days it will be:" + str(now + timedelta(days=2)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
print ("! week ago was date: ", t)
s = t.strftime("%A, %B, %d, %Y")
print (s)
### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1) #This gets afd (ApriL Fools Day)
print (afd)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print ("April Fool's went by %d days ago" %((today-afd).days))
    afd = afd.replace(year=today.year + 1)
    print (afd) #Next afd

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print("It's ", time_to_afd.days, " days until next AFD")
