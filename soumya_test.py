#python 2.7.6

# Q1 .multiples of 7 & not 5
mul=[]
for I in range(2000,3201):
  if (I%7==0) and (I%5!=0):
     mul.append(I)
print (mul)

    
# Q2.dictionary
dictionary={}
x=int(input("enter the number of elements :\n"))
for I in range(1,x+1)
   b=I*I
   dictionary[I]=b

print(dictionary)



# Q3.factorial

y=int(input("enter the number :\n"))
c=1
if y<0:
 print("factorial not possible")
else :
 {
	
   for I in range(1,y+1):
    c=c*I 
 }
print(c)



# Q4.less than 5 digits

a = [5,7,9,3,2,1,4,2,6,3,0,9,8]
z=[]
for n in a:
  if n<5:
    z.append(n)
    
print (z)  
x=input("element to be searched")
 
if x in a:
  print("element is present")
else:
  print("not found")  
  
  
  
  
  # Q5.upper case string
a=raw_input("enter the string")
print(a.upper())
    


#Q6.binary conversion
b=[]
a=int(input("enter the no"))
while a>1:
  {
  	    c=a%2
  	    b.append(c)
  	    a = a//2 
  }	    
d=len(b)-1
e=[]
while d>=0:
{
	e.append(b[d])
	d=d-1
}

 print( ' '.join(e))

  
#Q7.string reversal
a=raw_input("enter the string")
b=a.split()
c=[]
f=len(b)-1
while f>=0:
{
	c.append(b[f])
	f=f-1
}
print( ' '.join(c))

	
#Q8.pattern
a=input("enter no of rows")
for b in range(1,n+1):
 {
	for c in range(1,b+1):
	  {
  		
  	print(c)
  	}
  	print('\n')
 }
  