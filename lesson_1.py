'''def strcount(string): # сложность O(n**2)
    for symbol in string:
        counter = 0
        for sub_symbol in string:
            if symbol == sub_symbol:
                counter += 1
        print(symbol, counter)

strcount('aaaaabbbbbccdeee')'''


'''def strcount(string): # сложность O(n * m)
    for symbol in set(string):
        counter = 0
        for sub_symbol in string:
            if symbol == sub_symbol:
                counter += 1
        print(symbol, counter)


strcount('aaaaabbbbbccdeee')'''

'''def strcount(string): # сложность O(n)
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
    print(syms_counter)
strcount('aaaaabbbbbccdeee')'''

#GIT
# ls - просмотр всех файлов в папке
# git status - отслеживание статуса
# git init - инециализация
# git add . - добавить изменение
# git commit -m "initial commit" - сохранение изменений