def make_lines(num_of_elements: int) -> str:
    '''Добавляем в консоль строку для визуального разделения блоков'''
    line = '*' * num_of_elements
    print(line)


def set_user_name() -> str:
    '''Запаршивае имя пользователя'''
    new_name = input('Как тебя зовут? ')
    return new_name
