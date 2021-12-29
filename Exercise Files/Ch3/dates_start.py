#
# Example file for working with date information
#
from datetime import date, timedelta
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print ("Today is", today)
  tomorrow=date(today.year,today.month,today.day+1)
  print(tomorrow)
  # print out the date's individual components
  print("Date components", today.day, today.month, today.year )
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday number is", today.weekday())
  days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
  print("The day today is:", days[today.weekday()])
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print (today)
  
  # Get the current time
  t = datetime.time(datetime.now())
  print (t)

  today=date.today()
  days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  print("Tomorrow will be "+days[(today.weekday()+1)%7])

  
if __name__ == "__main__":
  main();
  