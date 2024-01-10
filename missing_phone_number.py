# Write a Python program to find the digits which are absent in a given mobile number.

no = [0,1,2,3,4,5,6,7,8,9]
phone_no = int(input("Enter a phone number: "))
for i in len(phone_no):
    if i not in no:
        print(f"the number {i} is not in mobile nuber.")
    else:
        print("all numbers are in phone number.")


