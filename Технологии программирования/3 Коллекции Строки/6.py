text = """"В тексте определить 3 наиболее часто встречаемых символа. 
Пробелы нужно игнорировать (не учитывать при подсчете). 
Итог работы программы представить в виде строки: 
«символ – количество раз, символ – количество раз…».""".lower()
text = text.replace(" ", '')
max_count = [0, 0, 0]
chars = [0, 0, 0]
for i in text:
    a = text.count(i)
    if a > max_count[0] and i not in chars:
        max_count[0] = a
        chars[0] = i
    elif a > max_count[1] and i not in chars:
        max_count[1] = a
        chars[1] = i
    elif a > max_count[2] and i not in chars:
        max_count[2] = a
        chars[2] = i

print(max_count)
print(chars)