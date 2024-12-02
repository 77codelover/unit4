a = int(input("Enter the 1st value: "))
b = int(input("Enter the 2nd value: "))
 
try:
    Ans = a/b
except ZeroDivisionError:
    print("Second value is not zero...")
else:
    print("Answer = ",a/b)