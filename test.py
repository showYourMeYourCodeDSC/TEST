print("Nos. divisible by 7 but are not multiple of 5")
nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))

#Print factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factorial : "))
print(factorial(n))

#Hello world
def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


# decimal number
number = int(input("Enter any decimal number: "))

decimalToBinary(number)

#circle
import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
 
r=int(input("Enter radius of circle: "))
obj=circle(r)
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),2))
