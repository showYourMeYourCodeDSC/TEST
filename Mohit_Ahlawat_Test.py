
Jupyter Notebook

#find the no. divisible by 7 in range 2000 to 3201, and not be a multiple of 5.

x=[]

for i in range(2000,3201):

    if(i%7==0 and i%5!=0):

        x.append(i)

        

print(x)        

[2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199]

#Question 2

x=int(input())

d={}

a=[]

b=[]

for i in range(x+1):

    a.append(i)

    c=i*i

    b.append(c)

    d[a[i]]=b[i]

    

print(d)    

9     #INPUT
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} #OUTPUT

#Question 3

def factorial(n):

    x=1

    i=1

    while i<=n:

        x=x*i

        i+=1

    print(x)

x=int(input())    

result=factorial(x)

result

        

        

10       #INPUT
3628800  #OUTPUT

#Question 4 part(a)

l=[5,7,9,3,2,1,4,2,6,3,0,9,8]

for i in l:

    if i<5:

        print(i)

    else:

        continue

        
#OUTPUT
3
2
1
4
2
3
0

#part b

l=[5,7,9,3,2,1,4,2,6,3,0,9,8]

new=[]

for i in l:

    if i<5:

        new.append(i)

        pass

    

print(new)    

[3, 2, 1, 4, 2, 3, 0]

#take a no. from the user part(c)

n=int(input())

if n in l:

    print("number is present in list!")

else:

    print("no such number in list!")

6
number is present in list!

#Question 5

string=input()

print(string.upper())

hello world this is python
HELLO WORLD THIS IS PYTHON

#Question 6

x=int(input())

i=x

z=''

while i>=1:

    d= i%2

    z+=str(d)

    i=i//2

print(z[::-1])    

    

11 #INPUT
1011 #OUTPUT

#Question 7 string reverse

str1=input()

str_1=str1.split( )

str_2=str_1[::-1]

print(" ".join(str_2))

 
python is really a cool language!! #INPUT
language!! cool a really is python #OUTPUT

#Question 8
un=4

count=0

for i in range(0,n):

    if i<=1:

        for j in range(0,i+1):

            count+=1

            print(count,end='')


    else:

        count=i+1

        for j in range(0,i+1):

            print(count,end='')

            count++1

    

    print("\r")

#output

1
23
345
4567

#Question 9
class Circle():

    

    def __init__(self,radius,):

        

        self.radius=radius

    def area(self):

        print(3.147*pow(self.radius,2))

        

        

obj=Circle(4)

obj.area()

50.352

#Question10
class MultipleMethods():

    def __init__(self):

        pass

    def getString(self):

        print("please enter a string:")

        self.q=input()

    def printString(self):

        print(self.q)

obj1=MultipleMethods()

obj1.getString()

obj1.printString()

    

please enter a string:
hello bro!!!
hello bro!!!

#Question 11
str2=input()

str3=str2.split( )


for i in str3:

    count=0

    for j in str3[1:]:

        if(i==j):

            count+=1

    print("{}:{}".format(i,count))    

    

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3 #INPUT
#OUTPUT
New:0
to:1
Python:5
or:2
choosing:1
between:1
Python:5
2:2
and:1
Python:5
3?:1
Read:1
Python:5

#################################################################################end.
2:2
or:2
Python:5
3:1

