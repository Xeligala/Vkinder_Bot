import random


CALLBACK_TYPES = ('show_snackbar',
                  'open_link',
                  'open_app')

commands = {
    'search': {'in': ['search', 'поиск', 'искать', 'найти'],
              'out': ['Вот что я нашел'],
              'key': 'search',
              'keyboard': 'search'},
    'next': {'in': ['next', 'следующий'],
              'out': ['Следующий'],
              'key': 'next',
              'keyboard': 'search'},
    'previous': {'in': ['previous', 'предыдущий'],
             'out': ['Предыдущий'],
             'key': 'previous',
             'keyboard': 'search'},
    'settings': {'in': ['settings', 'настройки'],
                'out': ['Настройки'],
                 'key': 'settings',
                 'keyboard': 'settings'},
     'age_from': {'in': ['age_from', 'Возраст от'],
                  'out': ['Введите возраст от'],
                  'key': 'age_from',
                  'keyboard': 'settings'},
     'age_to': {'in': ['age_to', 'Возраст до'],
                  'out': ['Введите возраст до'],
                  'key': 'age_to',
                  'keyboard': 'settings'},
    'hello': { 'in': ['hello', 'привет', 'hello', 'hi', 'privet', 'hey'],
              'out': ['Приветствую', 'Здравствуйте', 'Привет!'],
              'key': 'hellow',
              'keyboard': 'menu' },
    'menu': { 'in': ['back', 'назад', 'меню'],
             'out': ['Назад' ],
              'key': 'back',
              'keyboard': 'back'},
    'back': {'in': ['назад'],
             'out': ['Назад'],
             'key': 'back',
             'keyboard': 'menu'},
    'black_list': {'in': ['black_list', 'черный список'],
             'out': ['Черный список'],
             'key': 'black_list',
             'keyboard': 'menu'},
    'favorites': {'in': ['favorites', 'фавориты', 'избранное'],
             'out': ['Фавориты'],
             'key': 'favorites',
             'keyboard': 'menu'},
    'none': {'in': [],
             'out': ['Я знаю команды:\n привет\n поиск\n следующий\n предыдущий\n избранное\n черный список\n настройки'],
             'key': 'none',
             'keyboard': 'menu'}
}


def get_answer(el):
    answer = f'{random.choice(el["out"])} {el.get("content")}'
    return answer
