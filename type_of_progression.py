""" Write a Python program to find the type of the progression (arithmetic progression/geometric progression) and
    the next successive member of a given three successive members of a sequence.
"""
def identify_progression(a, b, c):
    if b - a == c - b:
        return "Arithmetic Progression", c + (c - b)
    elif b / a == c / b:
        return "Geometric Progression", c * (c / b)
    else:
        return "Not a recognized progression", None

# Input three successive members of the sequence
a = float(input("Enter the first term (a): "))
b = float(input("Enter the second term (b): "))
c = float(input("Enter the third term (c): "))

# Identify the progression and calculate the next successive member
progression_type, next_term = identify_progression(a, b, c)

# Display the results
print(f"The sequence is a {progression_type}.")
if next_term is not None:
    print(f"The next successive member in the sequence is: {next_term}")

