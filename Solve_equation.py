"""
Write a Python program which solve the equation:
ax+by=c dx+ey=f
Print the values of x, y where a, b, c, d, e and f are given.
Input:
a,b,c,d,e,f separated by a single space.
(-1,000 = a,b,c,d,e,f = 1,000) Input the value of a, b, c, d, e, f:
5	8 6 7 9 4
Values of x and y: -2.000 2.000
"""
a, b, c, d, e, f = map(float, input("Enter values of a, b, c, d, e, f separated by a single space: ").split())

# Check if the denominator is zero to avoid division by zero
if a * e - b * d == 0:
    print("The system of equations has no unique solution.")
else:
    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)

    print("Values of x and y: {:.3f} {:.3f}".format(x, y))
