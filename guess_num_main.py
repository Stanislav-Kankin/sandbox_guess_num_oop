from random import randint


class GuessNum:
    def __init__(self, user_try=5,
                 start_num=0, end_num=50,
                 user_name = 'User') -> None:
        self.user_try = user_try
        self.start_num = start_num
        self.end_num = end_num
        self.user_name = user_name

    def set_random_num(self) -> int:
        print(
            '*************************************************\n'
            'Привет, это игра угадай число))\n'
            'введи пожалуйста диапазон для загадывания числа!\n'
            '*************************************************'
        )
        self.start_num = int(
            input('Введите начальное число: ')
        )
        self.end_num = int(
            input(
                'Введи число конца диапазона: \n'
            )
        )
        return randint(self.start_num, self.end_num)

    def set_try(self) -> int:
        self.set_try = int(
            input(
                '_______________________\n'
                'Введите число попыток: '
            )
        )
        return self.set_try

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