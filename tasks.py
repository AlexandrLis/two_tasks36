# Задача Винни пух
def song():
    count = 0
    letters = []
    alphabet = 'аеёиоуыиэюя'
    sing = input('Введите стих: ')
    my_sing = sing.split()
    while(count < len(my_sing)):
        for word in my_sing:
            symbol = 0
            for letter in word:
                if letter in alphabet:
                    symbol += 1
            letters.append(symbol)
            count += 1
    letters.sort()
    if letters[0] == letters[len(letters) - 1]:
        print('Парам пам-пам')
    else:
        print('Пам парам')
song()

#задача 36
def print_operation_table(operation, row, col):
    for i in range(1, row+1):
        for j in range(1, col+1):
            print(operation(i, j), end = '\t')
        print()

def resultat():
    row = int(input('Введите номер строки: '))
    col = int(input('Введите номер столбца: '))
    print_operation_table(lambda i, j: i*j, row, col)

resultat()