'''
Write a Python program to find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9.
The number that can be rearranged shall start with 0 as in 00135668. 
Input: 
Input an integer created by 8 numbers from 0 to 9.: 
2345 
Difference between the largest and the smallest integer from the given integer: 3087
'''

from itertools import permutations

def find_difference(input_number):
    # Convert the input number to a list of digits
    digits = list(map(int, str(input_number)))

    # Generate all permutations of the digits
    permutations_list = list(permutations(digits))

    # Convert each permutation to an integer and filter out those starting with 0
    valid_permutations = [int(''.join(map(str, perm))) for perm in permutations_list if perm[0] != 0]

    # Find the largest and smallest integers
    largest_integer = max(valid_permutations)
    smallest_integer = min(valid_permutations)

    # Calculate the difference
    difference = largest_integer - smallest_integer

    return difference

# Input from the user
input_number = int(input("Input an integer created by 8 numbers from 0 to 9: "))

# Calculate and display the difference
result = find_difference(input_number)
print(f"Difference between the largest and smallest integer from the given integer: {result}")
