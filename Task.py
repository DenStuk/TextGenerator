import random
import sys
import handling
import re

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
    

    # Расстановка дефисов
    text = text.replace('какнибудь','как-нибудь')
    text = text.replace('чтонибудь','что-нибудь')
    text = text.replace('когданибудь','когда-нибудь')
    text = text.replace('чтото','что-то')

    return text

if __name__ == '__main__':
    text_name = sys.argv[1] # Используемый текст
    text_len = sys.argv[2] # Длина выходного текста
    handling.redactor(text_name) # Подготовка текста
    learning() # Создание словаря
    text = generation(text_len) # Генерация случайного текста
    target = preparation(text)
    print(target) # Вывод текста

