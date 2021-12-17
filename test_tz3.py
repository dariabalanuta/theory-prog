import timeit
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
    assert min_number([1, -1, -2]) == -2

def load(number):
    def sum_number(number):
        suma = 0
        for x in number:
            suma = suma + x
        return suma
    sum_number(number)

    def mult_number(number):
        mult = 1
        for x in number:
            mult = mult * x
        return mult
    mult_number(number)

    def max_number(number):
        maximum = max(number)
        return maximum
    max_number(number)

    def min_number(number):
        minimum = min(number)
        return minimum
    min_number(number)

    print("Сумма:", sum_number(number))
    print("Произведение:", mult_number(number))
    print("Максимальное:", max_number(number))
    print("Минимальное", min_number(number))
    print('Время работы:', timeit.timeit())
    return

#Проверка работы программы при количестве элементов в массиве
def test_load_f(): #элементы в диапазоне от 1 до 100 и количество = 100 и без нуля
    import random
    number = [random.randint(1, 100) for i in range(100)]
    assert (load(number)) == (False, None)

def test_load_s(): #элементы в диапазоне от 1 до 100 и количество = 1000 и без нуля
    import random
    number = [random.randint(1, 100) for i in range(10000)]
    assert (load(number)) == (False, None)

#без нуля так как он сокращает работу из-за умножения


















