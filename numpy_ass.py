#!/usr/bin/python3

##run this file as python3 file_name

import numpy as np

count = 0	#for counting no of inputs
valid_input = 1		#for getting inputs until q is reached
print("enter the values and press q: to stop as any further input")

user_input = input()

t=()
t = t+tuple(user_input)

## to check return type of input() function whether it is also string ##

#print(type(user_input))

## to compare strings in python function used is str1.equals(str2)  ##

while valid_input != 0:
	if user_input != "q":
		user_input = input()
		if user_input != "q":
			t = t+tuple(user_input)		
		count+=1

	else:
		break

print("tuple formed==>"+str(t))
print("count==>"+str(count))

count_no=count
 
for i in range(2,count_no//2+1):
	if count%i==0:
		print ("matrix can be formed from them")
		break
			
	else:
		print("enter one more number")
		user_input = input()
		t = t+tuple(user_input)
		count+=1
		break
print(" you have entered "+str(count)+" elements ")
print ("enter the prefered size of the matrix you want from the input")
row = int(input())
column = int(input())
if (row*column == count and (row!=1 or column!=1) and (row!=0 or column!=0)):	
	print ("matrix can be formed with this size")
else:
	print("sorry not a valid size for forming the matrix with the given input of size count")



## printing  the desired array of choosen size with the given inputs ##

tp = np.full([row,column],0)


## below for loop will parallely run condition of for loop on 3 variables i,j,k ##
#for i,j,k in zip(range(0,len(t)),range(0,row),range(0,column)):	
#	tp[j][k] = t[i]



## copy content of t in t1 ##
t1=t
no_of_elements_count=0 ## for keeping count in tuple on reading elements ##
m=0  ##initialising row value to be fixed for each row
i=0
k=0
n=0  ##for setting pointer to first element of tuple##
def array(i1,k1):
	global no_of_elements_count,m,n,i,k,n		## declaring these all as global variables ##
	i=i1
	k=k1
	no_of_elements_count+=1
	tp[m][k]=t[i]

	if(k==column-1 and m!=row-1 and n!=len(t)):	
		m+=1				##for next row##
		#n=len(t)-no_of_elements_count	##remove added elements from the tuple to add remaining##
		n+=1
		k=0
		arr=array(n,k)
		arr

	elif(k==column-1 or m==row-1 or n==len(t)-1):
		print("resultant desired array is==>>"+str(tp))
		print("the final output is as above")
	else:
		
		n+=1
		k+=1	
		arr=array(n,k)
		arr
		


## to call definition of function ##
arr=array(0,0)
arr
