# Задача 1
# Напишите функцию read_entire_file, которая целиком считает текст из файла и напечатает
# его

def read_entire_file(path2file):
    with open(path2file, 'r', encoding='utf-8') as f:
        text = f.read()
    print(text)
    return 0

print('*'*10, 'Задача 1', '*'*10)
read_entire_file('sample.txt')

# Задача 2
# Напишите функцию read_first_n_lines, которая напечатает первые n строк текстового
# файла

def read_first_n_lines(path2file, n):
    with open(path2file, 'r', encoding='utf-8') as f:
        for i, j in enumerate(f):
            if (i+1) <= n:
                print(j.rstrip())
            else: break
    return 0

print('*'*10, 'Задача 2', '*'*10)
read_first_n_lines('sample.txt', 2)


# Задача 3
# Напишите функцию add_end_to_file, которая добавит к файлу строку, которая будет
# содержать фразу END OF FILE воспользовашись методом write

def add_end_to_file(path2file):
    with open(path2file, 'a', encoding='utf-8') as f:
        f.write('\nEND OF FILE\n')
    return 0

print('*'*10, 'Задача 3', '*'*10)
add_end_to_file('sample.txt')


# Задача 4
# Напишите функцию text2list, которая запишет текст в список построчно (каждый элемент
# списка - строка в исходном файле)

def text2list(path2file):
    with open(path2file, 'r', encoding='utf-8') as f:
        lines = [item.rstrip() for item in f.readlines()]
    return lines

print('*'*10, 'Задача 4', '*'*10)
text = text2list('sample.txt')
print(text)

# Задача 5
# Напишите функцию longest_line, которая вернет самую длинную строку (длина строки -
# количество символов в ней)

def longest_line(path2file):
    with open(path2file, 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            if len(line) > i:
                i = len(line)
                result = line
        return result

print('*'*10, 'Задача 5', '*'*10)
result = longest_line('sample.txt')
print(result)


# Задача 6
# Напишите функцию add_info_to_file, которая посчитает число слов и число различных слов
# в текстовом файле и допишет после текста пустую строку, строку, которая будет содержать
# фразу "Количество слов в тексте: n", где n - результат подсчета числа слов и строку, которая
# будет содержать фразу "Количество различных слов в тексте: k" (k - число различных слов)

# основная функция
def add_info_to_file(path2file):
    file = open(path2file, 'r+', encoding='utf-8')
    text = file.read().replace('\n', ' ').rstrip()
    words = tokenize(text) # получаем список слов
    words_count = len(words)
    different_count = len(set(words))
    file = write_to_file(file, 'Количество слов в тексте: {n}\n'.format(n = words_count))
    file = write_to_file(file, 'Количество различных слов в тексте: {k}\n'.format(k = different_count))
    file.close()
    return 0

def tokenize(text):
    words = [word.rstrip(',.') for word in text.split(' ')]
    return words

# записывает аргумент в файл на новой строке
def write_to_file(file, info):
    file.write(info)
    return file

print('*'*10, 'Задача 6', '*'*10)
add_info_to_file('sample.txt')

# Задача 7
# Напишите функцию get_names_from_json, которая вернет список имен из sample.json
# Подсказка: изучите файл перед выполнением задания и не забудьте импортировать библиотеку
# json

# При использовании на sample.json:
# Ivan Elena Leonid Mihail Maxim

import json

def get_names_from_json(path2file):
    with open(path2file, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    names = [name for name in data] # записываем в переменную список имен из json
    return names

print('*'*10, 'Задача 7', '*'*10)
result = get_names_from_json('sample.json')
print(result)

# Задача 8
# Напишите функцию convert_marks, которая прочитает sample.json из переведет оценки из
# букв в цифры (A соответствует 5, B - 4, C - 3, D - 2) и запишет в новый json под названием
# digit_marks.json

def convert_marks(path2file):
    with open(path2file, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    marks_dict = {'A': '5', 'B': '4', 'C': '3', 'D': '2'}
    data = json.dumps({i:marks_dict[data[i]] for i in data})
    with open('digit_marks.json', 'w', encoding='utf-8') as result:
        result.write(data)
    return 0

print('*'*10, 'Задача 8', '*'*10)
convert_marks('sample.json')