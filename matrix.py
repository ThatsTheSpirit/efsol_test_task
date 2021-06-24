from random import randint


m, n = int(input('Введите M: ')), int(input('Введите N: '))
matrix = [[randint(1, 10) for _ in range(n)] for _ in range(m)]

ans = input('Записать в файл?(да/нет): ')
if ans.lower() == 'да':
    filename = input('Имя файла для сохранения матрицы: ')

    if not filename.endswith('.csv'):
        filename = filename + '.csv'

    with open(filename, 'w') as csvfile:
        for row in matrix:
            line = map(str, row)
            line = ','.join(line) + '\n'
            csvfile.write(line)
elif ans.lower() == 'нет':
    for row in matrix:
        print(*row, sep=' ')
else:
    print('Ошибка')
