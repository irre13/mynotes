import datetime
import controller as controller

commands = [
    'Создать заметку',
    'Показать все заметки',
    'Удалить заметку',
    'Изменить заметку',
    'Выбрать заметки по дате',
    'Выход из программы'
]


def main_menu() -> int:
    print('\nГлавное меню:')
    for i, line in enumerate(commands, 1):
        print(f'\t{i}. {line}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 7:
                return choice
            else:
                print('\nТакого пункта нет. Попытайтесь еще раз.')
        except ValueError:
            print('\nВведено неверное значение. Попробуйте еще раз. ')


def show_notes(note_list):
    print('\nЗаметки:')
    if len(note_list) == 0:
        print('\tПока нет ни одной заметки')
    else:
        for note in note_list:
            print('\nID: ' + str(note['id']) + '\n' + 'Заголовок: ' + note['header'] + '\n' + 'Содержание: ' +
                  note['content'] + '\n' + 'Дата создания/изменения: ' + note['data_of_create_or_change'])


def create_new_note(new_id: int):
    date_note = datetime.datetime.now().strftime("%d.%m.%Y : %H.%M.%S")
    d = {'id': new_id, 'header': input('Заголовок заметки: '), 'content': input('Содержание заметки: '),
         'data_of_create_or_change': date_note}
    return d


def show_new_note(note: dict):
    print('\nНовая заметка:')
    print('ID: ' + str(note['id']) + '\n' + 'Заголовок: ' + note['header'] + '\n' + 'Содержание: ' +
          note['content'] + '\n' + 'Дата создания/изменения: ' + note['data_of_create_or_change'])


def select_del_note() -> int:
    while True:
        try:
            id_note_for_delete = int(input('\nВыберите id заметки, которую хотите удалить: '))
            return id_note_for_delete
        except ValueError:
            print('\nЧислом, пожалуйста. Попробуйте еще раз. ')


def del_confirm(header: str):
    result = input(f'Вы действительно хотите удалить заметку "{header}"? (y/n): ').lower()
    if result == 'y':
        return True
    else:
        return False


def view_changes():
    print('\nИзменения внесены.')


def undo_changes():
    print('\nИзменения отменены. Возвращаемся в главное меню')


def find_note():
    find = input('\nУкажите, от какого числа ищем заметки в формате ДД.ММ.ГГГГ: ')
    return find


def search_error():
    print('\nЗаметок нет. Возможно был неверно указан формат даты, или нет заметок с указанной датой.')


def input_error():
    print('\nОшибка ввода. Нет заметки с таким ID.')


def exit_prog():
    print('\nПрограмма завершена. До свидания!')
