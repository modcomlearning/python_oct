a = 300
b = -222

if b > a:
    print("B is bigger ")   # condition 1

elif a > b:
    print("A is bigger")   # condition 2

elif a == b:
    print("A and B are equal") # condition 3

else:
    print("Invalid") #  last option - assume

    # it is advisable to use elif to test possible conditions
    # Above example works when two variables are involved