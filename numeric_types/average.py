import summing_numbers


def average(*numbers):
    lng = len(numbers)
    sum = summing_numbers.mysum(*numbers)
    avg = sum / lng
    return f'{avg:.1f}'


# print(average(10,20,30,40,50,50,90,120,12,78,1000))