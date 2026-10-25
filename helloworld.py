"""print("Hello, World!")
print(1,2,3)
print(1,2,3,sep="---")
print(1,2,3,sep="---",end="***")"""

# Redirecting print output to a file
"""f = open("a.txt", "a")
print("This is redirected to a.txt", file=f)
f.close()"""

# Flushing the output buffer
"""import time
for i in range(1,6):
    print(i, end=" ", flush=True)
    time.sleep(1)

for i in range(1,6):
    print(i, end=" ", flush=False)
    time.sleep(1)"""

"""a=input("Enter a number: ")
print("You entered:", a, type(a))"""

"""a=int(input("Enter a number a: "))
b=int(input("Enter a number b: "))
#print("You entered:", a, b, type(a), type(b))
print("Sum of a and b is:", a+b)

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")"""

a=int(input("Enter a number a: "))
b=int(input("Enter a number b: "))
c=int(input("Enter a number c: "))
if a>b and a>c:
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
else:
    print("c is the greatest")

