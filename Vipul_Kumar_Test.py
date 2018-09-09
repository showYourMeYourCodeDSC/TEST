# Question 1
# Write a program which will find all such numbers which are divisible by 7 but are not
# a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints: Consider use range(#begin, #end) method in range ""

# Solution 1
for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        print(str(i),end =",")


# QUESTION 2:
# With a given integral number n, write a program to generate a dictionary that contains
# (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Solution2
n = int(input("Enter the integer range"))
thedist = {}
for i in range (1,n+1):
    thedist.update([(i,i*i)])
print(thedist)


# Question 3
# factorial
factIn = int(input("Enter a the number to find its factorial "))
a = 1
for i in range(1, factIn + 1):
    a = a * i
print(a)



# Question 4
a = [5, 7, 9, 3, 2, 1, 4, 2, 6, 3, 0, 9, 8]
b = list()
for i in range(len(a)):
    if a[i] < 5:
        b.append(a[i])
print(a+[b])
Check=int(input("Enter number to be find into the list"))
for i in range(len(a)):
    if a[i] == Check:
        print("Number present at postion "+str(i))



# Question 5
b = []
while True:
    a = input("Press Enter after you have written the Stings\n")
    if a:
        b.append(a.upper())
    else:
        break;

for a in b:
    print(a)


#Question 6
# Integer to Binary
def intToBinary(n):
    k = ""
    while n > 0:
        k = k+str(n%2)
        n = int(n/2)
    return k
def reverse(a):
  str = ""
  for i in a:
    str = i + str
  return str
inp=int(input("Enter the number to be Converted into Binary"))
s = intToBinary(inp)
print(reverse(s))




# Question 7
def reverseWords(inp):
    inputWords = inp.split(" ")

    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output

if __name__ == "__main__":
    inp = 'Rinkiya ke papa'
    print (reverseWords(inp))




# Question 8
# 1
# 23
# 345
# 4567
def patt(n):
    num = 1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print("\r")
n = 4
patt(n)




# QUESTION 9:
# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.
# Hints: Use def methodName(self) to define a method.

class Circle:
    def Area(self,r):
        A=2*3.174*r*r
        return A
r=int(input("Enter the radius"))
obj = Circle()
print("Enter a Area",round(obj.Area(r)))


