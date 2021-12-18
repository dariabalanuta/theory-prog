import timeit
print("Program started")
try:
    print("Opening file...")
    with open('1.txt', 'r') as file:
        lines = file.read()
        number = []
        number = [int(x) for x in lines.split()]

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

    load(number)

except FileNotFoundError:
    print("File not found!")
except Exception:
    print("Something gone wrong!")
print("Program finished")
