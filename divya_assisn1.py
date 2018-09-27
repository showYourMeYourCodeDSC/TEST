#ques1
r=[]
for i in range(2000,3201):
    if (i%7==0 and i%5!=0):
         r.append(i)
print(r)

#ques2
result=dict()
n=int(input("Enter number"))
for i in range(1,n+1):
    result.update({i:i*i})
print(result)

#ques3
num=int(input("enter number"))
fact=1
for i in range(n):
    fact=fact*(i+1)
print("factorial of number is",fact)

#ques4
#(i)
a=[5,7,9,3,2,1,4,2,6,3,0,9,8]
for i in a:
    if(a[i]<5):
     print(a[i])

#(ii)
b=[]       
for j in a:
    if(a[j]<5):
      b.append(a[j])
print(b)
#(iv)
no=input("enter number")
if no in a:
   print("element is present in list")
else:
   print("element not in list")

#ques 5
line=input("enter line")
print(line.upper())

#ques7
string=input("enter string")
string=string.split(" ")
revstring=string[: :-1]
print(revstring)

#ques8
for i in range(1,5):
    print(end="\n")
    for k in range(1,2*i):
          if(k>=i):
              print(k,end=' ')
#ques9
class Circle:
      def __init__(self,radius):
          self.radius=radius
      def area(self):
          self.area=(3.14*(self.radius)**2)
          print(self.area)
y=int(input("enter radius"))
ob=Circle(y)
ob.area()

      
      
      


 

        


    
 
