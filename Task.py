import random

def learning():
    # Открытие файла
    file = open('Training.txt', 'r')

    # Создание списка - обработка по словам
    spisok = list()

    for line in file:
        x = line.split()
        spisok = spisok + x

    # Создание словаря
    vocabulary = dict()

    for i in range(len(spisok)):
        a = spisok[i]
        b = list()
        vocabulary[a] = b
                
    for i in range(len(spisok)-1):
        a = spisok[i]
        b = spisok[i+1]


        x = vocabulary[a]
        x.append(b)
        vocabulary[a] = x
    
    return vocabulary

def generation():
    global vocabulary
    result = ''

    data = vocabulary

    now = random.choice(list(data.keys()))

    j = 0
    while j < 30:
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



if __name__ == '__main__':
    vocabulary = learning()
    print(vocabulary)

    text = generation()

    print(text)