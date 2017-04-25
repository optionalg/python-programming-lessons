#Wendy's update

import datetime

now = datetime.datetime.now()
name = input("What's your name? ")
age = int(input("What's your age by the end of this year? "))
year = now.year + (100 - age)
print ("Hi ",name," you will turn 100 in.....","\n","calculating.....","\n","calculating.....","\n","the year ",year)
