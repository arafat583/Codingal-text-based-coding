import time

print("Shutdown Verdicter opening...")
time.sleep(2)
print("loading....")
time.sleep(5)
times = str(input("what time is it? time + am/pm")).lower()
day = str(input("what day is it")).lower()

time.sleep(1)
print("checking the time...")
time.sleep(2)

if times <= "10" + "am":
    print("Work not started")
elif times >= "6" + "pm":
    print("Work time over")
else: 
    print("Work not ended")

time.sleep(1)
print("checking the day...")
time.sleep(2)

if day == "friday" or "saturday":
    print("No work today!")
else:
    print("It's a working day")             


