a=float(input("Enter the first number"))
b=float(input("Enter the Third number"))
c=float(input("Enter the Third number"))

if(a>=b) and (a>=c):
    largest=a
if(b>=a)and(b>=c):
    largest=b
if(c>=a)and(c>=b):
    largest=c

    print("Largest number among a b And c are=",largest) 