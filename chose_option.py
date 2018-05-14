#! /usr/bin/python3

import time
from google import search

#from BeautifulSoup import BeautifulSoup
## library to query a website ##
import urllib2
print ("Press1 : {Enter anything to get related website}")
print ("Press2 : {Enter anything to get related images}")
print ("Press3 : {Enter anything to get related URL of webpages}")
print ("Press4 : {to get current date and time}")
print ("Press5 : {to open default WebBrowser}")
print ("Press6 : {to check current connected IPs}")
print ("Press7 : {Enter domain and get owner's name and contact}")


option = int(raw_input())

if option == 1:
	print ("option 1 choosen,corresponding output is:")
	print ("Enter the string")
	str = raw_input()
	list = str.split()



elif option == 2:
	print ("option 2 choosen,corresponding output is:")
	print ("Enter the string")
	str = raw_input()
	list = str.split()

elif option == 3:
	print ("option 3 choosen,corresponding output is:")
	print ("Enter the string")
	str = raw_input()
	list = str.split()

	for i in range(0,len(list)):
		for url in search(list[i], stop=15):
			## stop = is used for controlling no of output URLs ##
    			print(url)

		## for getting titles and links of webpages using beautifulsoup and urllib lib ##
		'''	findPatTitle = re.findall(patFinderTitle,webpage)

			findPatLink = re.findall(patFinderLink,webpage)	
			print findPatLink	
		'''

elif option == 4:
	print ("option 4 choosen,corresponding output is:")
	
	current_time = time.ctime()
	print (current_time)

elif option == 5:
	print ("option 5 choosen,corresponding output is:")

elif option == 6:
	print ("option 6 choosen,corresponding output is:")


elif option == 7:
	print ("option 7 choosen,corresponding output is:")
	print ("Enter the string")
	str = raw_input()
	list = str.split()

else:
	print ("Choose a valid option")

