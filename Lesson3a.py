
# function is a blcok of code that performs a task
def payroll(basic, house_allowance, transport_allowance, nhif):
    # basic = 15000
    # house_allowance = 2500
    # transport_allowance = 3000
    # nhif = 500
    tax = basic*0.05
    gross = basic + transport_allowance + house_allowance
    print("Your Gross is ", gross)

    netpay = gross - (nhif + tax)
    return netpay  # netpay is returned


# create a function to find SI
# PRT/100
def simple_interest():
    p = 50000
    r = 11.4
    t = 14
    interest = p * r * t/100
    print("ANswer is ", interest)

# create a function to convert from  KES to USD, EURO, YEN

# create to find bmi
def body_mass_index(weight, height):
    bmi = weight/(height ** 2)
    return bmi


# Task1 : create to find area of triangle
# 1/bh
# Your function should have parameters , and return
def traingle_area(base, height):
    area = 1/2 * base * height
    return area



def leap(year):
    if year%4 ==0:
        return "Leap"
    else:
        return "Not Leap"

status = leap(year=2000)
print(status)
# =========
def leap2():
    year = 2024






# advantages
# 1. They allow code reuse
# 2. Split a bigger program to smaller chunks/parts
# 3. Functions are used in OOP
