try:
    a = input("Type a number:")
    b = input("Type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")
