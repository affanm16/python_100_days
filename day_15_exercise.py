#time module
import time
# timestamp = time.strftime('%H:%M:%S')#strftime is a func which gives hours and minutes
# print(timestamp)
# timestamp=int(time.strftime('%H'))
# print(timestamp)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)
hourshand = int(time.strftime('%H'))

# minuteshand=int(time.strftime('%M'))

# secondshand=int(time.strftime('%S'))
timestamp=time.strftime('%H:%M:%S')
print(timestamp)

#morning 6:0:0 to 11:59:59
if(hourshand>=6 and hourshand <12):
    print("good morning")
elif(hourshand>11 and hourshand <17):
    print("good afternoon")
elif(hourshand>16 and hourshand <23):
    print("good evening")
else:
    print("good night")

