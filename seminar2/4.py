# 4) Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

txt = input("введите слова")
txt = txt.split(" ")
for ind, el in enumerate(txt):
    print(ind + 1, el[0:10])
