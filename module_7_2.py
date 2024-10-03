import io

from pprint import pprint

strings_positions = {}


def custom_write(file_name, strings):
    count = 0
    file = open(file_name, 'w', encoding='utf-8')

    for i in strings:
        x = file.tell()
        file.write(i + '\n')
        count += 1
        strings_positions[(count, x)] = i
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('../test.txt', info)
for elem in result.items():
    print(elem)
