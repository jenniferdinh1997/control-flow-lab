# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
a = int(input('Enter the lengths of three sides of a triangle: a: '))
b = int(input('Enter the lengths of three sides of a triangle: b: '))
c = int(input('Enter the lengths of three sides of a triangle: c: '))
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
if a == b == c:
    print(f'A triangle with sides of {a}, {b}, and {c} is an equilateral triangle')
elif a != b != c:
    print(f'A triangle with sides of {a}, {b}, and {c} is a scalene triangle')
elif a == b or b == c or a == c:
    print(f'A triangle with sides of {a}, {b}, and {c} is an isosceles triangle')

