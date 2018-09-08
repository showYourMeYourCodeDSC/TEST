#Q1:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.


a=[]

for i in range(2000,3001):
    if(i%7==0):
        if(i%5!=0):
            a.append(i)

        else:
            continue
    else:
        continue
b=','.join(str(i) for i in a)
print(b)


#Q2:
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


sqr=dict()
n=int(input("Enter the number:"))
for i in range(1,n+1):
    sqr.update({i:i**2})
print(sqr)


#Q3:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320


n=int(input("ENTER NUMBER: "))
f=1
for i in range(n):
    f=f*(i+1)

print("Factorial of",n,"is",f)


#Q4:

a = [5,7,9,3,2,1,4,2,6,3,0,9,8]

#(i) Write a program that prints out all the elements of the list that are less than 5.
for i in a:
    if(i<5):
        print(i)

#(ii) Make a new list that consists of numbers less than 5 from this list in it and print out this new list.


b=[i for  i in a if i<5]
print(b)

#(iv) Ask a number from the user and check whether the number is present in the list or not.

n=int(input("Enter Number:"))

if n in a:
    print("Element",n,"is present in list")
else:
    print("Element",n,"is not present in list")


#Q5:
#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect

#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT


lines = []
n=int(input("Enter number of lines:"))
for i in range(n):

    s =input("Enter the string  ")
    if s:
        lines.append(s)
        b='\n'.join(i.upper() for i in lines)

    else:
        break;



print(b)


#Q6:
#Given a decimal number (integer N), convert it into binary and print.
#HINT: Print output as a string



x=[]
re=[]
y=int(input("Enter the Integer:"))
while(1):
    q=y//2
    r=y%2
    x.append(r)
    y=q
    if(y==0):
        break

i=len(x)-1
while(i>=0):
    re.append(x[i])
    i=i-1

b=''.join(str(j) for j in re)
print(b)


#Q7:
#Reverse the given string word wise. That is, the last word in given string should come at 1st place, last second word at 2nd place and so on. Individual words should remain as it is.
#For Example Rinkiya ke papa should become papa ke Rinkiya


l=[]
re=[]
st=input("Enter string:")
l=st.split(" ")
i=len(l)-1
while(i>=0):
    re.append(l[i])
    i=i-1

b=' '.join(str(j) for j in re)

print(b)


#Q8:
#Print the following pattern
#Pattern for N = 4
#1
#23
#345
#4567


n=int(input("Enter number of lines:"))

for i in range(1,n+1):
    print("\n")
    count=i
    for j in range(i):
        print(count,end='')
        count=count+1

#Q9:
#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
#Hints: Use def methodName(self) to define a method.

class Circle:

    def __init__(self,radius):

        self.radius = radius

    def area(self):

        print("Area of circle:",3.14*((self.radius)**2))




r=int(input("Enter radius:"))
ob=Circle(r)
ob.area()


#Q10:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.
#Hints:
#Use __init__ method to construct some parameters


class String_2:

    def __init__(self,s1,us1):

        self.s1 = s1
        self.us1= us1

    def getString(self):

        print(self.s1)

    def printString(self):

        print(self.us1)




s1=input("Enter string:")
us1=s1.upper()
ob=String_2(s1,us1)
ob.getString()
ob.printString()


#Q11:
#Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

#Suppose the following input is supplied to the program:

#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

n=input()
counts=dict()
words=n.split()
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key,":", counts[key])


#Finish
