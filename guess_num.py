from random import randint
from utils import make_lines

from score_db import Score, session


class GuessNum:
    """
    Инициалзируем класс для игры
    """
    def __init__(self, user_try=5,
                 start_num=0, end_num=50) -> None:
        self.user_try = user_try
        self.start_num = start_num
        self.end_num = end_num
        self.name = None

    def set_random_num(self) -> int:
        """
        Метода для установки с помощью пользователя
        диапазона для загадывания числа
        """
        make_lines(40)
        self.set_user_name()
        print(
            f'Привет, {self.name}, это игра угадай число))\n'
            'введи пожалуйста диапазон для загадывания числа: '
        )
        self.start_num = int(
            input('Введите начальное число: ')  # Начало диапазона
        )
        self.end_num = int(
            input(
                'Введи число конца диапазона: \n'  # Конец диапазона
            )
        )
        make_lines(40)
        return randint(self.start_num, self.end_num)

    def set_user_name(self) -> str:
        """Запрашивает имя пользователя"""
        while True:
            try:
                new_name = input('Как тебя зовут? ')
                if new_name.strip():
                    self.name = new_name
                    return self.name
                else:
                    raise ValueError('Имя не может быть пустым.')
            except ValueError as e:
                print(e)
            except KeyboardInterrupt:
                print("\nВыход из программы.")
                break

    def set_try(self) -> int:
        """
        Просим пользователя поставить  количество попыток
        для отгадывания числа
        """
        make_lines(40)
        self.set_try = int(
            input(
                'Введите число попыток: '
            )
        )
        make_lines(40)
        return self.set_try

    def main(self) -> None:
        """
        Основная логика игры
        """
        count_of_try = 0  # Считаем за сколько пользователь угадает число
        try:
            rand_num = self.set_random_num()
            option_user_try = self.set_try()
        except ValueError:  # Проверяем что ввели именно число(целое)
            print('Ошибка, нужно ввести число!')
            return
        while True:
            print(
                f'Я загадал число от {self.start_num} до {self.end_num}\n'
                f'Осталось {option_user_try} попыток!')
            if option_user_try == 0:
                print(
                    'К сожалению ты не угадал, попытки кончились...\n'
                    'Не расстраивайся, попробуй ещё раз)\n'
                    f'Было загаданно число {rand_num}'
                    )
                break
            user_int = int(input(
                f'Количество попыток - {option_user_try}\n'
                'Введите число: '
            ))
            if user_int == rand_num:
                print(
                    'Число угаданно! Здорово!\n'
                    f'Ты справился за {count_of_try} попыток!'
                    )
                break
            elif user_int > rand_num:
                option_user_try -= 1
                count_of_try += 1
                print(
                    '\n'
                    'Загаданное число меньше...'
                    '\n')
            elif user_int < rand_num:
                option_user_try -= 1
                count_of_try += 1
                print(
                    '\n'
                    'Загаданное число больше...'
                    '\n')
                new_score = Score(
                    user_name=self.name, number_of_try=count_of_try
                    )
                session.add(new_score)
                session.commit()

        session.close()
