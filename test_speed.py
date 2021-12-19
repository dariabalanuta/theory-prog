import timeit
import random
import string


def onlynumb(lines):
    l = list(string.ascii_letters)

    for element in lines:
        if element in l:
            print('Mistake - there is a letter!')
            break
    else:
        def load(lines):
            number = [int(x) for x in lines]

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
            print('Время работы:', timeit.timeit())
            return

        load(lines)
        return

#Проверка работы программы при количестве элементов в массиве
def test_onlynumb_f(): #элементы в диапазоне от 1 до 1000 и количество = 10 и без нуля
    lines = [random.randint(1, 1000) for i in range(10)]
    onlynumb(lines)

def test_onlynumb_s(): #элементы в диапазоне от 1 до 1000 и количество = 10.000 и без нуля
    lines = [random.randint(1, 1000) for i in range(10000)]
    onlynumb(lines)
#без нуля так как он сокращает работу из-за умножения

print('#Проверка работы программы при количестве элементов в массиве  '
      '#без нуля так как он сокращает работу из-за умножения'  )
print()
test_onlynumb_f()
print('#элементы в диапазоне от 1 до 1000 и количество = 10 ')
print()
test_onlynumb_s()
print('#элементы в диапазоне от 1 до 1000 и количество = 10.000 ')
print()
print('#Сумма указана для подтверждения того, что числа разные')
