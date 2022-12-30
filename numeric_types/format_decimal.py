from decimal import *
import math

def format_decimal(numberf,before, after):

    try:
        number_string = str(numberf)[before:]
        decimals = number_string.split('.')[1][:after]
        number_decimal = math.trunc(numberf)
        print(f'{number_decimal}.{decimals}')

    except InvalidOperation as e:
        print('Valor incorrecto')

format_decimal(1234.5678, 2, 3)