# 
# Example file for retrieving data from the internet
#

import urllib.request  #This has classes needed for http requests

def main(): #defining main function
  webUrl = urllib.request.urlopen("http://google.com") #variable called webUrl 
  print("result code: " + str(webUrl.getcode())) #response from the server is obtained by calling the getcode function (E.g 200, 404)
  data = webUrl.read() #calling read function on the response
  print (data)

if __name__ == "__main__":
  main()
