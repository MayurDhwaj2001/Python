x = 5
y = 0

try:
    print("Resource Opend")
    print(x / y)

except ZeroDivisionError as e:
    print("Hey! not possible,", e)

except Exception:  # For Unknown Error
    print("Something went wrong")

finally:  # This will run if there is error or not
    print("Resource Closed")
