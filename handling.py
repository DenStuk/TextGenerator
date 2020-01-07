def redactor(fileName):
    file = open(fileName, "r")

    string = ''

    for line in file:
        string += line

    length = len(string)
    i = 0

    while i < length:
        if string[i] == '.':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == ',':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '!':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '?':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '-':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == ':':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == ';':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '"':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == "'":
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '(':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == ')':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '-':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '—':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '«':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '»':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '.':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '„':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        elif string[i] == '“':
            string = string[:i] + string[i+1:]
            length -= 1
            i -= 2
        i += 1

    f = open("Data.txt", 'w')

    for j in string:
        f.write(j)

