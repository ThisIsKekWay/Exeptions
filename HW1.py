# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения
#
# Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?
#
# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке. Если длины массивов не равны,
# необходимо как-то оповестить пользователя.
#
# * Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке. Если длины массивов не равны,
# необходимо как-то оповестить пользователя.
#
# Важно: При выполнении метода единственное исключение, которое пользователь может увидеть - RuntimeException, т.е. ваше.


import random
def div(num1, num2):
    while True:
        try:
            print(num1 / num2)
            break
        except ZeroDivisionError:
            print('Деление на ноль недопустимо')
            while True:
                try:
                    num2 = int(input('Введите новое число '))
                    break
                except ValueError:
                    print('Вводить можно только числа')
                except NameError:
                    print('Введите число и только число')


def list_pointer(lst, num):
    print(*lst)
    while True:
        try:
            print(lst[num])
            break
        except IndexError:
            print('Этот массив не содержит столько элементов')
            try:
                num = int(input('Введите индекс снова '))
            except ValueError or NameError:
                print('Введите число и только число')
                continue



def dic_pointer(dct, key):
    while True:
        try:
            print(dct[key])
            break
        except KeyError:
            print('Словарь не содержит такого ключа')
            print(f'Список доступных для обращения ключей: {dct.keys()}')
            key = input('Введите ключ ')


def array_diff(lst1, lst2):
    print(f'Первый массив {lst1}')
    print(f'Второй массив {lst2}')
    if len(lst1) != len(lst2):
        print('ВНИМАНИЕ! Длины массивов не равны, корректное завершение операции не гарантируется')
    new_lst = list()
    try:
        for i in range(len(lst1)):
            new_lst.append(lst1[i] - lst2[i])
        print(f'Результат вычислений: {new_lst}')
    except IndexError:
        print(f'''Достигнута точка разницы массивов
                  Промежуточный результат: {new_lst}
Выполнение остановлено''')


def array_div(lst1, lst2):
    print(f'Первый массив {lst1}')
    print(f'Второй массив {lst2}')
    if len(lst1) != len(lst2):
        print('ВНИМАНИЕ! Длины массивов не равны, корректное завершение операции не гарантируется')
    new_lst = list()
    try:
        for i in range(len(lst1)):
            new_lst.append(round(lst1[i] / lst2[i], 2))
    except IndexError:
        print(f'''Достигнута точка разницы массивов
                  Промежуточный результат: {new_lst}
Выполнение остановлено''')


while True:
    try:
        chose = int(input('''Введите цифру для выбора функции:
                             1) Проверка исключения "Деление на ноль"
                             2) Проверка исключения "Индекс за пределами массива"
                             3) Проверка исключения "Ошибка ключа словаря"
                             4) Проверка разности элементов двух разноразмерных массивов
                             5) Проверка частного элементов двух разноразмерных массивов
                             
                             Для выхода введите 0\n'''))
        if chose == 0:
            break

        if chose == 1:
            while True:
                try:
                    num1 = int(input('Введите первое число '))
                    num2 = int(input('Введите второе число '))
                    div(num1, num2)
                    break
                except ValueError:
                    print('Введите число и только число')
                    continue
                except NameError:
                    print('Введите число и только число')
                    continue


        if chose == 2:
            lst = list(random.randint(0, 10) for _ in range(random.randint(5, 11)))
            try:
                num = int(input('Введите индекс массива '))
                list_pointer(lst, num)
            except ValueError:
                print('Введите число и только число')
            except NameError:
                print('Введите число и только число')



        if chose == 3:
            dct = {'green': 'go', 'yellow': 'warning', 'red': 'stop'}
            key = input('Введите ключ словаря ')
            dic_pointer(dct, key)

        if chose == 4:
            lst1 = list(random.randint(0, 51) for _ in range(random.randint(5, 11)))
            lst2 = list(random.randint(0, 51) for _ in range(random.randint(3, 6)))
            array_diff(lst1,lst2)

        if chose == 5:
            lst1 = list(random.randint(0, 51) for _ in range(random.randint(5, 11)))
            lst2 = list(random.randint(0, 51) for _ in range(random.randint(3, 6)))
            array_div(lst1, lst2)

        if chose < 0 or chose > 5:
            print('Команда не распознана, повторите ввод')

    except ValueError:
        print('Введите цифру и только цифру')



