from guess_num import GuessNum

if __name__ == '__main__':
    player = GuessNum()
    try:
        player.main()
    except KeyboardInterrupt:
        print('Программа завершена пользователем.')
