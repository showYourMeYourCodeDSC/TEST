#Ques1

L=[]
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
       L.append(i)
print(L)



#Ques2
x= int(input("Enter Number"))
Lone={i:i*i for i in range(1,n+1)}
print(Lone)


#Ques3
x= int(input("Enter Number"))
f=1
while x>0 :
      f= f*x
      x= x-1
print(f)


#Ques4
a= [5,7,9,3,2,1,4,2,6,3,0,9,8]

#parta
for i in a:
    if a[i]<5:
print(a[i])

#partb
b=[]
for i in a:
    if a[i]<5:
       b.append(a[i])
    
print(b)

#partc
c=[a[i] for i in a if a[i]<5]
print(c)


#partd
d= int(input("Enter Number"))
if d==a[i] for i in a:
   print("Number Present")
   else:
       print("Number Not Present")
       

#Ques5
x= int(input("Enter string")
print(x.upper())


#Ques7

St= ("Rinkiya Ke papa")
St1 =St.split()

St2= []
x = len(St1) - 1
while x >= 0:
    St2.append(St1[x])
    x = x-1

result=" ".join(St2)
print (result) 
    


#Ques6
def decimalToBinary(num):
    if num > 1:
       decimalToBinary(num // 2)
       print(num % 2, end='')
number = int(input("Enter any decimal number: "))  
decimalToBinary(number)









#Ques11
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
return counts
print(word_count(str))

