"""
Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. Print "Yes"
if the given sides form a right triangle otherwise print "No".
Input:
Integers separated by a single space. 1 = length of the side = 1,000
Input three integers(sides of a triangle)
8 6 7
No
"""

def right_triangle(a,b,c):
    sides = sorted([a,b,c])

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return "Yes, right triangle"
    else:
        return "NO!.."


tri_sides = input("Enter 3 Integers: ").split(" ")

s1, s2, s3 = map(int,tri_sides)

result = right_triangle(s1,s2,s3)
print(result)

