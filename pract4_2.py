try:
    a = int(input("Enter the 1st value: "))
    b = int(input("Enter the 2nd value: "))
    Ans = a/b
except (ZeroDivisionError,TypeError,SyntaxError):
    print("Error...")
else:
    print("Answer = ",a/b)