def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.

    Параметры:
        - text (str): строка;
        - shift (int): свдиг.
    Результат:
        str: измененная строка."""
    # Набор кириллических букв
    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    new_text = ''
    for i in text:
        # if i.lower() not in letters:
        #     new_text += i
        #     continue
        try:
            j = letters.index(i.lower()) + shift
            while j > len(letters):
                j -= len(letters)
            char = letters[j]
            if not i.islower():
                char = char.capitalize()
            new_text += char

        except ValueError:
            new_text += i

    return new_text

try:
    text = input()
    shift = int(input())
    encoded = ceasar(text, shift)
    decoded = ceasar(encoded, -shift)
    print("Зашифрованная строка:", encoded)
    print("Расшифрованная строка:", decoded)
except ValueError:
    print("Сдвиг должен быть целым числом!")