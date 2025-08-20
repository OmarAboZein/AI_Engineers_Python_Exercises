print("Enter a number to check if it's even or odd and if divisble by 4:")
number = int(input())
if number % 2 == 0:
    if number % 4 == 0:
        print("The number is even and divisible by 4.")
    else:
        print("The number is even.")
else:
    print("The number is odd.")

print("Now enter two numbers to check if the first is divisible by the second:")
num = int(input("Enter the first number: "))
check = int(input("Enter the second number: "))
if num % check == 0:
    print(f"{num} is divisible by {check}.")
else:
    print(f"{num} is not divisible by {check}.")        
