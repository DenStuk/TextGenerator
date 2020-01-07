import random
import sys
import os
import re
import handling

def learning():
    # Открытие файла
    file = open("Data.txt", 'r')

    # Создание списка - обработка по словам
    spisok = list()

    for line in file:
        x = line.split()
        spisok = spisok + x

    # Создание словаря
    global vocabulary 
    vocabulary = dict()

    # Создание модели словаря
    for i in range(len(spisok)):
        a = spisok[i]
        b = list()
        vocabulary[a] = b

    # Заполнение словаря            
    for i in range(len(spisok)-1):
        a = spisok[i]
        b = spisok[i+1]
        x = vocabulary[a]
        x.append(b)
        vocabulary[a] = x
    
    return vocabulary

def generation(text_len):
    global vocabulary
    result = ''

    data = vocabulary

    now = random.choice(list(data.keys()))

    j = 0 # Счётчик слов

    while j < int(text_len):
        length = len(data[now])
        if length > 1:
            rnd = random.randint(0,length - 1)
            value = data[now]
            nxt = value[rnd]
            result += nxt
            result += ' '
            now = nxt
        elif length == 1:
            value = data[now]
            nxt = value[0]
            result += nxt
            result += ' '
            now = nxt
        else:
            break
        j += 1

    return result

def preparation(text):
    # Все буквы в строчные
    text = text.lower()
    
    # Первая буква заглавная
    fword = ''
    for let in text:
        if let == " ":
            break
        else:
            fword += let
    title = fword.title()
    text = text.replace(fword, title, 1)


    # Точка в конце текста
    text = text[:len(text)-1]
    text = text + '.'
    
    # Расстановка запятых
    text = text.replace(' а ', ' ,а ')
    text = text.replace(' но ', ' ,но ')

    # Расстановка дефисов
    text = text.replace('какнибудь','как-нибудь')
    text = text.replace('чтонибудь','что-нибудь')
    text = text.replace('когданибудь','когда-нибудь')
    text = text.replace('чтото','что-то')

    return text

if __name__ == '__main__':
    arguments = len(sys.argv) - 1
    if arguments == 1:
        if sys.argv[1] == '/?':
            print("Text Generator")
            print("This program generates random text based on any other text.")
            print("Instruction: python(python3 for MacOS) [File name] [Length of the text]")
            print("Also you can use test text: python Test.txt [Length of the text]")
        if sys.argv[1] != '/?':
            print("Error: You entered the wrong number of arguments.")
            print("Enter: \"python main.py [file] [length]\" or use command \"main.py /?\"")
    elif arguments == 2:
        text_name = sys.argv[1] # Используемый текст
        text_len = sys.argv[2] # Длина выходного текста
        if os.path.exists(text_name) == False:
            print("Error: File doesn't exist")
            sys.exit()
        if text_len.isdigit() == False:
            print("Error: Second argument is not a number")
            sys.exit()

        # Выполнение основной программы
        handling.redactor(text_name) # Подготовка текста
        learning() # Создание словаря
        text = generation(text_len) # Генерация случайного текста
        target = preparation(text) # Редактирование текста
        print(target) # Вывод текста

    else:
        print("Error: You entered the wrong number of arguments.")
        print("Enter: \"python main.py [file] [length]\" or use command \"main.py /?\"")

