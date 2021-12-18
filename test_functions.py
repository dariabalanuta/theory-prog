#Сумма чисел
def sum_number(number):
    suma = 0
    for x in number:
        suma = suma + x
    return suma

def test_sum_number():
    number = ([1, 2, 4])
    assert sum_number(number) == 7
    assert sum_number([1, -1, 1]) == 1


#Произведение чисел
def mult_number(number):
    mult = 1
    for x in number:
        mult = mult * x
    return mult

def test_mult_number():
    number = ([1, 2, 4])
    assert mult_number(number) == 8
    assert mult_number([1, -1, 1]) == -1


#Максимум чисел
def max_number(number):
    maximum = max(number)
    return maximum

def test_max_number():
    number = ([1, 2, 4])
    assert max_number(number) == 4
    assert max_number([1, -1, 2]) == 2


#Минимум чисел
def min_number(number):
    minimum = min(number)
    return minimum

def test_min_number():
    number = ([1, 2, 4])
    assert min_number(number) == 1
    assert min_number([1, -1, -2]) == -3


















