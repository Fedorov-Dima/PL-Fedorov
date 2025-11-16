def isvowels(word):
    vowels = 'аоуыэяёюие'
    if word[0].lower() in vowels:
        return True
    return False

def isconsonants(word):
    consonants = 'йцкнгшщзхъфвпрлджчсмтб'
    if word[0].lower() in consonants:
        return True
    return False

with open("poem.txt", 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)
    words = text.split()

vowels_count = 0
consonants_count = 0

for word in words:

    if isvowels(word):
        vowels_count += 1

    elif isconsonants(word):
        consonants_count += 1

if vowels_count > consonants_count:
    print('гласные')
elif consonants_count > vowels_count:
    print('согласные')
else:
    print('одинаково')