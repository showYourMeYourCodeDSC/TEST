# Q1
seq = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        seq.append(i)

print(seq)

# Q2
n = int(input("Enter the number:"))
dict = {}
for i in range(1, n+1):
    dict[i] = i**2

print(dict)


# Q3

while True:
    print("Options:")
    print("Enter 1 to print Factorial")
    print("Enter 2 to quit")
    user_input = input(': ')

    if user_input == '2':
        break
    elif user_input == '1':
        x = int(input("Enter the Number:"))
        f = x
        fact = 1
        for i in range(x):
            fact = fact*f
            f -= 1
         print(fact)
# Q4

a = [5, 7, 9, 3, 2, 1, 4, 2, 6, 3, 0, 9, 8]  # original list

for i in range(len(a)):
    if a[i] < 5:
        print(a[i])
# part b
x = []
for i in range(len(a)):
    if a[i] < 5:
        x.append(a[i])
print(x)
# part c
y = [a[i] for i in range(len(a)) if a[i] < 5]
print(y)
#part d
n=int(input("Enter the number to check:"))
for i in range(len(a)):
    if(a[i]==n):
        print("Number is present")
    else:
        print("Number is not present")
# Q5

string=input("Enter the string:  ")
print(string.upper())

# Q6
digit = int(input("Enter the Digit:"))
binary = 0
i = 0
while(1):
    rem = digit % 2
    quot = digit//2
    pot = 10**i
    i = i+1
    binary = rem*pot+binary
    digit = quot
    if(digit == 0):
        break
print("Binary:"+str(binary))

#Q7

n=input("Enter a string:")
n=n.split(" ")
print(n[::-1])

# Q8

for i in range(1, 5):
    print()
    for j in range(1, 2*i):
        if(j >= i):
            print(j, end=' ')

# Q9


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.area = 3.14*(self.radius**2)
        print(self.area)


a1 = Circle(10)
a1.area()

# Q11
k = 0
a = {}
b = {}
string = input("Enter the line:")
x = string.split(" ")
for i in x:
    for j in x:
        if(i == j):
            k += 1
    a.update({i: count})
    k = 0
for j in sorted(a):
    b.update({j: a[j]})
print(b)
