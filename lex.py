import pandas as pd

LEXER_TABLE = pd.DataFrame(columns=['TOKEN', 'IDENTITY'])

def lexer():
    with open('input1.txt', 'r') as myfile:
        string = myfile.read().replace('\n', '')

    SYMBOLS = ['(', ')', ';', ',', ':', '\'']
    SYMBOLS_1 = [' (', ')', ';', ',', ':', '\'', '+', '-']
    SYMBOLS_1_DUP = [['Open bracket', '('], ['Close bracket', ')'], ['Semicolon', ';'],
                     ['Comma', ','], ['Colon', ':'], ['single quote', ''], ['plus', '+'], ['minus', '-']]

    keywords = ['int', 'main', 'char', 'switch', 'begin', 'case', 'printf', 'break', 'end', 'return', ' ', '\n']
    keywords_def = [['t', 'int'], ['m', 'main'], ['t', 'char'], ['w', 'switch'], ['b', 'begin'], ['c', 'case'],
                    ['p', 'printf'], ['k', 'break'], ['d', 'end'], ['r', 'return'], ['s', ' '], ['o', '+'],
                    ['o', '-'], ['n', '\n'], ['d', 'end']]
    KEYWORDS = SYMBOLS_1 + keywords

    white_space = ' '
    lexeme = ''
    mylist = []
    string = string.replace('\t', '')
    # print(string)
    for i, char in enumerate(string):
        if char != white_space:
            lexeme += char
        if (i + 1 < len(string)):
            if string[i + 1] == white_space or string[i + 1] in KEYWORDS or lexeme in KEYWORDS:
                if lexeme != '':
                    mylist.append(lexeme.replace('\n', '<newline>'))
                    # print(mylist)
                    lexeme = ''
    mylist.append(lexeme.replace('\n', '<newline>'))

    s = ''
    j = 0

    try:
        while True:
            mylist.remove('')
    except ValueError:
        pass

    for item in mylist:
        for i in keywords_def:
            if i[1] == item:
                s = s + i[0]
        if item in SYMBOLS:
            s = s + item
        elif item.isdigit():
            s = s + 'a'
        elif item not in KEYWORDS:
            s = s + 'v'

    for i in mylist:
        for k in SYMBOLS_1_DUP:
            if i == k[1]:
                LEXER_TABLE.at[j, 'TOKEN'] = i
                LEXER_TABLE.at[j, 'IDENTITY'] = k[0]
                j = j + 1
                break
        if i in keywords:
            LEXER_TABLE.at[j, 'TOKEN'] = i
            LEXER_TABLE.at[j, 'IDENTITY'] = 'Keyword'
            j = j + 1
            continue
        if i.isdigit():
            LEXER_TABLE.at[j, 'TOKEN'] = i
            LEXER_TABLE.at[j, 'IDENTITY'] = i
            j += 1
            continue
        elif i not in KEYWORDS:
            LEXER_TABLE.at[j, 'TOKEN'] = i
            LEXER_TABLE.at[j, 'IDENTITY'] = 'identifier'
            j += 1

    return s

result = lexer()
print(result)
LEXER_TABLE.to_csv('lex.csv', index=False)
