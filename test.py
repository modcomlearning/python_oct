# means all functions in lesson 3a can be accessed here
from Lesson3a import *

# this function returns netpay
netpay = payroll(basic=40000, house_allowance=2500,
               transport_allowance=1000, nhif=300)

print("Netpay is ", netpay)

# the answer is being by the function, not this file
# this file does have access to answers
# Now this file has access to netpay

bmi = body_mass_index(weight=50.9, height=1.5)
print("BMI is ", bmi)

area = traingle_area(base=45, height=1.5)
print(area)

from  math import *
square = sqrt(25)
print(square)






