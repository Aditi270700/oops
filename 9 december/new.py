import my_calculator_python as m 
print(m.x)
print(m.y)

from my_calculator_python import sub_calculator as b
print(b(50,25))

from my_calculator_python import add_calculator as bcd
data=bcd(10,10)
print(data)
bcd(10,10)