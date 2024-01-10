# Write a Python program to find common divisors between two numbers in a given pair


def find_divisor(num1,num2):
    common_divisor = []
    min_num = min(num1,num2)

    for i in range(1,min_num+1):
        if num1%i==0 and num2%i==0:
            common_divisor.append(i)

    return common_divisor

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

result = find_divisor(num1,num2)
print(f"The common divisors between {num1} and {num2} are: {result}")

