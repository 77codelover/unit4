import datetime
year = int (input("Enter your birth year: "))
month = int (input("Enter your birth month: "))
day = int (input("Enter your birth day: "))
birthday = datetime.datetime(year, month, day)
now = datetime.datetime.now()
Difference = now - birthday
print("Difference is ",Difference.days," days ")