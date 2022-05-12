#Q1
num_1=int(input("Enter the number to be converted to binary: "))
print(bin(num_1))



#Q2
exp = input("Enter the expression ")
print(eval(exp))




#Q3
import math as mth

n=int(input("Ënter the number n: "))
r=int(input("Enter the radius r: "))
a=int(input("Enter the angle a: "))
b=int(input("Enter the angle b: "))
x1=int(input("Enter the number x1: "))
x2=int(input("Enter the number x2: "))
y1=int(input("Enter the number y1: "))
y2=int(input("Enter the number y2: "))
print ("print (3+4)(5)=",(3+4)*5)
print("print n(n-1)/2=",(n*(n-1))/2)
print("print 4πr^2=",4*mth.pi*(r**2))
print("sqrt(r(cos a)^2 + r(sin b)^2)=",(r*mth.cos(a)**2+r*mth.sin(b)**2)**0.5)
if(x2==x1):
    print("NOT DEFINED")
else:
    print("y2-y1/x2-x1=",(y2-y1)/(x2-x1))    


#Q4

print("In the range(5)")
for i in range (5):
    print(i)

print("In the range(3, 10)")
for i in range(3, 10):
    print(i) 

print("In the range(4 ,13, 3)")
for i in range(4 ,13, 3):
    print(i) 

print("In the range(15, 5, -2)")
for i in range(15, 5, -2):
    print(i) 

print("In the range(5, 3)")
for i in range(5, 3):
    print(i)


#Q5
h2=int(input("Ënter the number of hydrogen atoms:"))
o2=int(input("Enter the number of oxygen atoms:"))
c=int(input("Enter the number of carbon atoms:"))

wt1=h2*1.00794
wt2=o2*15.9994
wt3=c*12.0107

print("The molecular mass of the carbohydrate is:",wt1+wt2+wt3)

