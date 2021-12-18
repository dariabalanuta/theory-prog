import timeit
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
        maximum = number[0]
        for x in number:
            if maximum < x:
                maximum = x
        return maximum
    max_number(number)

    def min_number(number):
        minimum = number[0]
        for x in number:
            if minimum > x:
                minimum = x
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