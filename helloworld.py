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

"""a=int(input("Enter a number a: "))
b=int(input("Enter a number b: "))
c=int(input("Enter a number c: "))
if a>b and a>c:
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
else:
    print("c is the greatest")"""

"""i = 0
while i < 5:
    print(i)
    i += 1"""

# Sum of N natural numbers
"""n = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print("Sum of first", n, "natural numbers is:", sum) """

# for <variable> in <iterable>:

"""for i in range(10):
    print(i)"""
"""
"""
# Build a calculator where 1 is addition, 2 is subtraction, 3 is multiplication, 4 is division and 5 is exit
"""while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice == 1:
        print("Sum is:", a + b)
    elif choice == 2:
        print("Difference is:", a - b)
    elif choice == 3:
        print("Product is:", a * b)
    elif choice == 4:
        # Check for division by zero
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Quotient is:", a / b)
    if choice < 1 or choice > 5:
        print("Invalid choice. Please try again.") 
"""

#print(__doc__)



# input two strings and check if they are anagrams or not
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Convert strings to lowercase and remove spaces
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check if the sorted characters of both strings are equal
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


"""s = "We love Python programming"
# Expected output is for every word in the string the first charactor should become the last character
words = s.split()
for word in words:
    print(word[-1] + word[1:-1] + word[0], end=" ")"""
