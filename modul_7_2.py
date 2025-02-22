def custom_write(file_name: str, strings: list):
    strings_positions = {}
    file = open(file_name, 'r+', encoding='utf-8')
    line_number = 1
    for i in strings:
        strings_positions[line_number, file.tell()] = i
        file.write(f'{i}\n')
        line_number += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


