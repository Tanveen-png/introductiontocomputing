
#Question 1

a=int(input("enter the number: "))
for i in range(a//2):
    rem=a%2
    a=a//2
    print(rem, end="")


#Question 2

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return(x/y)
print("\nselect operation")
print("1.Add")
print("2.subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice= input("Enter the choice(1/2/3/4)")
    if choice in ('1','2','3','4'):
        n1=float(input("Enter first number:"))
        n2=float(input("Enter the second number:"))

        if choice=='1':
            print(n1,"+",n2,"=",add(n1,n2))
        elif choice=='2':
            print(n1,"-",n2,"=",subtract(n1,n2))
        elif choice=='3':
            print(n1,"*",n2,"=",multiply(n1,n2))
        elif choice=='4':
            print(n1,"/",n2,"=",divide(n1,n2))
        nxt_cal=input("Next Calculation (Y/N):")
        if nxt_cal=="N":
            break
    else:
        ("Invalid Input")

#Question 3

from math import sin
from math import cos
a=(3+4)*(5)
print('\na',a)
n=int(input("Enter the number:"))
b=n*(n-1)/2
print('b',b)
r=int(input("Enter the number:"))
pi=3.41
c=4*pi*r**2
print('c',c)
a=int(input("enter angle"))
b=int(input("enter angle"))
d=(r*(cos(a)**2)+r*sin(b)**2)**(1/2)
print('d',d)
x1=int(input("enter number"))
y1=int(input("enter number"))
x2=int(input("enter number"))
y2=int(input("enter number"))
e=(y2-y1)/(x2-x1)
print('e',e)


# Question 4

print('\na)')
for i in range(5):
    print(i)
print('b)')
for i in range(3,10):
    print(i)
print('c)')
for i in range(4,13,3):
    print(i)
print('d)')
for i in range(15,5,-2):
    print(i)
print('e)')
for i in range(5,3):
    print(i)

# Question 5

h=int(input("\nEnter the no of hydrogen atom: "))
c=int(input("Enter the no of carbohydrate atom: "))
o=int(input("Enter the no of oxygen atom: "))
m= h*1.00794+ c*12.0107 + o*15.9994
print("Molecular Weight: ",m)






        
