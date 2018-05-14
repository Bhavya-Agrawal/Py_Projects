#! /usr/bin/python

import time

print "Press1 : {Enter anything to get related website}"
print "Press2 : {Enter anything to get related images}"
print "Press3 : {Enter anything to get related URL of webpages}"
print "Press4 : {to get current date and time}"
print "Press5 : {to open default WebBrowser}"
print "Press6 : {to check current connected IPs}"
print "Press7 : {Enter domain and get owner's name and contact}"


option = int(raw_input())

if option == 1:
	print "option 1 choosen,corresponding output is:"


elif option == 2:
	print "option 2 choosen,corresponding output is:"


elif option == 3:
	print "option 3 choosen,corresponding output is:"


elif option == 4:
	print "option 4 choosen,corresponding output is:"
	
	current_time = time.ctime()
	print current_time

elif option == 5:
	print "option 5 choosen,corresponding output is:"

elif option == 6:
	print "option 6 choosen,corresponding output is:"


elif option == 7:
	print "option 7 choosen,corresponding output is:"


else:
	print "Choose a valid option"

