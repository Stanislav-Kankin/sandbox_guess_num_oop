from random import randint
from utils import make_lines
from score_db import session


class GuessNum:
    def __init__(self, user_try=5,
                 start_num=0, end_num=50,
                 user_name='User') -> None:
        self.user_try = user_try
        self.start_num = start_num
        self.end_num = end_num
        self.user_name = user_name

    def set_random_num(self) -> int:
        self.set_user_name()
        make_lines(40)
        print(
            f'Привет, {self.user_name}, это игра угадай число))\n'
            'введи пожалуйста диапазон для загадывания числа: '
        )
        self.start_num = int(
            input('Введите начальное число: ')
        )
        self.end_num = int(
            input(
                'Введи число конца диапазона: \n'
            )
        )
        make_lines(40)
        return randint(self.start_num, self.end_num)

    def set_try(self) -> int:
        make_lines(40)
        self.set_try = int(
            input(
                'Введите число попыток: '
            )
        )
        make_lines(40)
        return self.set_try

    def set_user_name(self) -> None:
        new_name = input('Как тебя зовут? ')
        self.user_name = new_name
        return self.user_name

    def main(self) -> None:
        count_of_try = 0
        try:
            rand_num = self.set_random_num()
            option_user_try = self.set_try()
        except ValueError:
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
                print()
                print('Загаданное число меньше...')
                print()
            elif user_int < rand_num:
                option_user_try -= 1
                count_of_try += 1
                print()
                print('Загаданное число больше...')
                print()


if __name__ == '__main__':
    player = GuessNum()
    try:
        player.main()
    except KeyboardInterrupt:
        print('Программа завершена пользователем.')
