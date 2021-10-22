# nested statements
x = 25
if x > 10:
    print("X is more than 10")
    if x > 20:
        print("X is still more than 20")
    else:
        print("X is less than 20")
else:
    print("X is less or equal to 10")