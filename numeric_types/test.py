name = 'world'
first = 'Reuven'
last = 'Lerner'
number = 2048

# print(f'Hello {first:#<10} {last:#>10}')
# print(f'Hello {last:#<10} {name:#>10}')
# print(f'{name = }' )
# print(f'{number:#0x}')
# print(f'{name:=>12}')

# # assigning strings to the variables
# left_alignment = "Left Text"
# center_alignment = "Centered Text"
# right_alignment = "Right Text"

# # printing out aligned text
# print(f"|{left_alignment :=<20}{center_alignment :*^15}{right_alignment :$>20}|")

# print(f'Number\t\t\tSquare\t\t\tCube')
# for x in range(1, 11):
#  print(f'{x:2d}\t\t\t{x*x:3d}\t\t\t{x*x*x:4d}'
from decimal import *

getcontext().prec = 2

print(Decimal(3.14))

print(Decimal('3.14'))

print(Decimal((0, (3, 1, 4), -2)))

print(Decimal('NaN'))

print(Decimal(0.1) + Decimal(0.2))


