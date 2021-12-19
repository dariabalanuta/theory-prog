import string
import timeit

print("Program started")
try:
    print("Opening file...")
    with open('1.txt', 'r') as file:
        number = []
        lines = file.readlines()
        lines = [x.strip() for x in lines]

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
                    print("Произведение:", mult_number(number))
                    print("Максимальное:", max_number(number))
                    print("Минимальное", min_number(number))
                    print('Время работы:', timeit.timeit())
                    return
                load(lines)
                return

    onlynumb(lines)

except FileNotFoundError:
    print("File not found!")
except Exception:
    print("Something gone wrong!")
print("Program finished")
