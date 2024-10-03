from datetime import date , time , datetime 

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("\n current Date and time is", now)

print(f"\nDate components {today.year}/{today.month}/{today.day}")