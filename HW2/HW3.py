# Напишите приложение, которое будет запрашивать у пользователя следующие данные в произвольном порядке,
# разделенные пробелом:
# Фамилия Имя Отчество датарождения номертелефона пол
import datetime
import re

class WrongData(Exception):
    def __init__(self, expressison, message):
        self.expression = expressison
        self.message = message

    def print(self):
        print(self.expression)
        print(self.message)

class StringLengthError(WrongData):
    pass


class AllNamesError(WrongData):
    pass


class DateError(WrongData):
    pass


class PhoneError(WrongData):
    pass


class GenderError(WrongData):
    pass


def valid_info():
    while True:
        try:
            info = input('''Введите следующие данные через пробел:
Фамилия Имя Отчество Дата Рождения Номер телефона Пол\n''').split(' ')
            if len(info) < 6:
                raise StringLengthError(f'Количество значащих элементов: {len(info)}',
                                      'Строка слишком короткая, пропущен пробел, повторите ввод')
            elif len(info) > 6:
                raise StringLengthError(f'Количество значащих элементов: {len(info)}',
                                         'Строка слишком длинная, поставлен лишний пробел, повторите ввод')
            else:
                break
        except StringLengthError as e:
            e.print()
    return info


def valid_name(info):
    dct = {0: "Фамилию", 1: "Имя", 2: "Отчество"}
    for i in range(3):
        while True:
            try:
                if any(mark in '{}[],./?><=-_+:;|!@#$%^&*()' for mark in info[i]):
                    raise AllNamesError(f'Введено: {info[i]}',
                                        'Данные не могут содержать знаки')
                elif any(mark.isdigit() for mark in info[i]):
                    raise AllNamesError(f'Введено {info[i]}',
                                        'Данные не могут содержать цифры')
                else:
                    break
            except AllNamesError as e:
                e.print()
                newinfo = input(f'Введите {dct[i]} снова\n')
                info[i] = newinfo


def valid_date(info):
    form = '%d.%m.%Y'
    while True:
        try:
            if info[3].count('.') < 2 and len(info[3]) != 10:
                raise DateError(f'Введено: {info[3]}\n',
                                'Введен неверный формат даты')
            data = datetime.datetime.strptime(info[3], form).date()
            break
        except ValueError:
            print('Введён неверный формат даты\n')
            newdata = input('Введите дату снова\n')
            info[3] = newdata
        except DateError as e:
            e.print()
            newdata = input('Введите дату снова\n')
            info[3] = newdata


def valid_phone(info):
    while True:
        try:
            data = re.sub('\D', '', info[4])
            if data != info[4]:
                raise PhoneError(f'Введено {info[4]}\n',
                          'Телефон вводится без знака и форматирования\n')
            else:
                break
        except PhoneError as e:
            e.print()
            newdata = input('Введите телефон снова\n')
            info[4] = newdata

def valid_gender(info):
    while True:
        try:
            if info[5] not in 'fm':
                raise GenderError(f'Введено: {info[5]}\n',
                                  "There's no place for atack helicopter")
            else:

                break
        except GenderError as e:
            e.print()
            newdata = input('Введите пол снова\n')
            info[5] = newdata

def take_info():
    info = valid_info()
    valid_name(info)
    valid_date(info)
    valid_phone(info)
    valid_gender(info)
    return info


def put_info(info):
    filename = f'{info[0]}.txt'
    with open(filename, 'a') as f:
        f.write(' '.join(info) + '\n')
        f.close()


def main():
    while True:
        try:
            inp = input('Введите 1, чтобы внести данные\n'
                        'Введите 2, чтобы выйти из приложения\n')
            if int(inp) == 1:
                info = take_info()
                put_info(info)
                continue
            if int(inp) == 2:
                break
            else:
                raise WrongData(f'Введено {inp}', 'Неверный ввод')
        except ValueError or NameError:
            print('Неверный ввод')
        except WrongData as e:
            e.print()


main()