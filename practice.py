# import requests
# urk="http://saral.navgurukul.org/api/courses"
# url=requests.get(urk)
# print(url)


# 5O0BA



# s = "abcabcbb"
# i=0
# j=""
# while i<len(s):
#     if s[i] not in j:
#         j+=s[i]
#     i+=1
# print(j,len(j))



# arr=[1,3,5,7,9]
# i=0
# j=arr[0]
# while i<len(arr):
#     if j>arr[i]:
#         j=arr[i]
#     i+=1
# print(j)

# *********************************************************
# aList = ["PYnative", [4, 8, 12, 16]]
# print(aList[0][1])    
# print(aList[1][3])


# var = "James" * 2  * 3
# print(var)

# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)

# calculate(5, 6)



# for i in range(10, 15, 2):
#   print( i, end=', ')

# for i in range(15, 1, -2):
#   print( i, end=', ')

# a="567"
# print(float(a))

# list=[[1,4,5],[1,3,4],[2,6],[7,6,5]]

# i=0
# a=[]
# while i<len(list):
#     j=0
#     while j<(3):
#             a.append(list[i][j])
#             j=j+3
#     i=i+1
# print(a)





 
import datetime

import os

import time

import random

import webbrowser

# If video URL file does not exist, create one

if not os.path.isfile("youtube_alarm_videos.txt"):

print('Creating "youtube_alarm_videos.txt"...')

with open("youtube_alarm_videos.txt", "w") as alarm_file:

alarm_file.write("https://www.youtube.com/watch?v=anM6uIZvx74")

def check_alarm_input(alarm_time):

"""Checks to see if the user has entered in a valid alarm time"""

if len(alarm_time) == 1: # [Hour] Format

if alarm_time[0] < 24 and alarm_time[0] >= 0:

return True

if len(alarm_time) == 2: # [Hour:Minute] Format

if alarm_time[0] < 24 and alarm_time[0] >= 0 and \

alarm_time[1] < 60 and alarm_time[1] >= 0:

return True

elif len(alarm_time) == 3: # [Hour:Minute:Second] Format

if alarm_time[0] < 24 and alarm_time[0] >= 0 and \

alarm_time[1] < 60 and alarm_time[1] >= 0 and \

alarm_time[2] < 60 and alarm_time[2] >= 0:

return True

return False

# Get user input for the alarm time

print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")

while True:

alarm_input = input(">> ")

try:

alarm_time = [int(n) for n in alarm_input.split(":")]

if check_alarm_input(alarm_time):

break

else:

raise ValueError

except ValueError:

print("ERROR: Enter time in HH:MM or HH:MM:SS format")

# Convert the alarm time from [H:M] or [H:M:S] to seconds

seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second

alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# Get the current time of day in seconds

now = datetime.datetime.now()

current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

# Calculate the number of seconds until alarm goes off

time_diff_seconds = alarm_seconds - current_time_seconds

# If time difference is negative, set alarm for next day

if time_diff_seconds < 0:

time_diff_seconds += 86400 # number of seconds in a day

# Display the amount of time until the alarm goes off

print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

# Sleep until the alarm goes off

time.sleep(time_diff_seconds)

# Time for the alarm to go off

print("Wake Up!")

# Load list of possible video URLs

with open("youtube_alarm_videos.txt", "r") as alarm_file:

videos = alarm_file.readlines()

# Open a random video from the list

webbrowser.open(random.choice(videos))
