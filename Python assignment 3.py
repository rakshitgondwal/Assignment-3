

#Question1
n=int(input("Enter Number:"))
a=bin(n)
print(a)





#Question2
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choice = input("Enter choice(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))


        next_cal = input("Let's do next calculation? (yes/no): ")
        if next_cal == "no":
          break

    else:
        print("Invalid Input")







#Question3
import math
print(int(3+4)*5)
n=int(input("Enter Value of n:"))
print(n*(n-1)/2)
r=int(input("Enter value of r:"))
print(4*3.14*r**2)
a=int(input("Eter value of a:"))
b=int(input("Enter value of b:"))
print(((r*(math.cos(a)**2)) + (r*(math.sin(b)**2)))**0.5)
y2=int(input("Eter value of y2:"))
y1=int(input("Enter value of y1:"))
x2=int(input("Eter value of x1:"))
x1=int(input("Enter value of x2:"))
print((y2-y1)/(x2-x1) )








#Question4
print("a part")
for a in range(5):
    print(a)
print("b part")
for b in range(3,10):
    print(b)
print("c part")
for c in range(4,13,3):
    print(c)
print("d part")
for d in range(15,5,-2):
    print(d)
print("e part")
for e in range(5,3):
    print(e)






#Question5
h=int(input("Enter Number of Hydrogen atoms"))
c=int(input("Enter Number of Carbon atoms"))
o=int(input("Enter Number of Oxygen atoms"))
total=int(h*1.00794+c*12.0107+o*15.9994)
print("The total combined molecular weight in grams per mole is",total)

