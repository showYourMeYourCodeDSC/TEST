#question 1
a=[]
for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        a.append(i)
    else:
        continue
print(a)

#question 2
n=int(input("enter any number:"))
b={i:i*i for i in range(1,n+1)}
print(b)

#question 3
num=int(input("enter the number whose factorial is to be calculated:"))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print(fact)

#question 4
#part a
b=[]
a=[5,7,9,3,2,1,4,2,6,3,0,9,8]
for i in a:
    if(a[i]<5):
       print(a[i])
#part b
for i in a:
    if(a[i]<5):
        b.append(a[i])
print(b)
#part c
c=[]
c=[a[i]for i in a if(a[i]<5)]
print(c)
#part d
n=input("enter the number to check:")
if(a[i]==n for i in a):
    print("yes,the number is present")
else:
    print("the number you entered is not present")
#question 5
str=input("enter the required string")
print(str.upper())

#question 6
a=[]
y=int(input("enter the integer:"))
while(1):
    quo=y//2
    rem=y%2
    a.append(rem)
    y=quo
    if(y==0):
        break
a.sort(reverse=True)
print(a)

#question 7
x=input("enter any string:")
x=x.split(" ")
print(x[::-1])

#question 8
for i in range(1,5):
    print(end="\n")
    for j in range(1,2*i):
        if(j>=i):
            print(j,end=' ')

#question 9
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        self.area=3.14*pow(self.radius,2)
        print(self.area)
p1=Circle(25)
p1.area()

#question 10
class string:
    def getstring(self):
        self.s=input("enter any string:")
    def printstring(self):
        print(self.s)
p2=string
p2.getstring()
p2.printstring()

#question 11
count=0
w={}
s={}
y=input("enter any statement:")
z=y.split(" ")
for i in z:
    for j in z:
        if(i==j):
            count+=1
    w.update({i:count})
    count=0
for j in sorted(w):
    s.update({j:w[j]})
print(s)

#takeabreak
import webbrowser
import time
for i in range(0,3):
    webbrowser.open(r"https://github.com/showYourMeYourCodeDSC/TEST/commit/7d1a261fa44b0a07034c42dfdfa74f2cd2c03fe4,new=0,autoraise=true")
    time.sleep(10)
