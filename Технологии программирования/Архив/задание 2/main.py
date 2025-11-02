# ЗАДАНИЕ
#
# У вас есть результат распознавания речи телефонного разговора, где каналы разделены:
#   • Левый канал — оператор (файл f1.json),
#   • Правый канал — клиент (файл f2.json).
#
# Каждый канал лежит в отдельном JSON-файле со списком фрагментов:
# [
#   { "start": 2.03, "end": 2.63, "text": "Алло," },
#   { "start": 2.63, "end": 3.03, "text": "Елен," },
#   { "start": 3.17, "end": 3.67, "text": "здравствуйте." }
# ]
#
# Нужно написать программу, которая проверяет, что:
# 1) Нет ненормативной лексики
# 2) Есть благодарность
# 3) Приветствие
# 4) Сотрудник говорил более чем 1 мин
# 5) Сотрудник предложил купить посуду
#
# Результат вывести на экран.
# Пример: Правило 1: OK/Нарушение (обоснование нарушения)
import json
from itertools import zip_longest
import sys
sys.path.insert(0, '../logger')
from logger import log_to_console_and_file


BAN_WORDS = ("козел", "пидор", "мудак", "сука", "дурак")                    #ненормативная лексика
THANKS = ("спасибо", "блогадорю")                                           #благодарность
GREETINGS = ("привет", "здравствуйте")                                      #приветствие
DISHES = ("чашки", "тарелки", "посуду", "посуда", "ложки", "вилки")         #посуда
OFFERS = ("купить", "приобрести", "закупить", "заказать", "рассмотреть")    #предложение купить
LOG_FILE = "log.txt"


@log_to_console_and_file(LOG_FILE)
def check_ban_words(current_word):                      #Поиск ненормативной лексики
    current_word_text = current_word["text"].lower()
    for ban_word in BAN_WORDS:
        if ban_word in current_word_text:
            return current_word


@log_to_console_and_file(LOG_FILE)
def check_thanks(current_word):                         #Поиск благодарности
    current_word_text = current_word["text"].lower()
    for thank in THANKS:
        if thank in current_word_text:
            return current_word


@log_to_console_and_file(LOG_FILE)
def check_greetings(current_word):                      #Поиск приветствия
    current_word_text = current_word["text"].lower()
    for greeting in GREETINGS:
        if greeting in current_word_text:
            return current_word


@log_to_console_and_file(LOG_FILE)
def time_counting(word):                                #Подсчет времени
    return word["end"] - word["start"]


@log_to_console_and_file(LOG_FILE)
def check_buy_dishes(word1, word2):                     #Поиск предложения купить посуду
    flag_offer = False
    flag_dish = False
    if word2["start"] - word1["start"] <= 1:
        for offer, dish in zip_longest(DISHES, OFFERS, fillvalue=None):
            if not (offer is None) and (offer in word1["text"].lower() or offer in word2["text"].lower()):
                flag_offer = True
            if not (dish is None) and (dish in word1["text"].lower() or offer in word2["text"].lower()):
                flag_dish = True
            if flag_offer and flag_dish:
                return {"start": word1["start"], "end": word2["end"], "text": word1["text"] + word2["text"]}


with open("f1.json", mode="r", encoding="utf-8") as f1: #Открываем файл
    text_of_call = json.load(f1)

#Списки нарушений
rule_ban_words = []
rule_thanks = []
rule_greetings = []
rule_buy_dished = []
time = 0

#Выполнение программы
for i in range(len(text_of_call)):
    current_word = text_of_call[i]
    try:
        next_word = text_of_call[i + 1]
    except Exception:
        next_word = None

    #Вызов функций, заполнение списков нарушений
    result = check_ban_words(current_word)
    if not result is None:
        rule_ban_words.append(result)

    result = check_thanks(current_word)
    if not result is None:
        rule_thanks.append(result)

    result = check_greetings(current_word)
    if not result is None:
        rule_greetings.append(result)

    time += time_counting(current_word)

    if not next_word is None:
        result = check_buy_dishes(current_word, next_word)
        if not result is None:
            rule_buy_dished.append(result)

#Вывод результатов
if not rule_ban_words:
    print("Правило 1: ОК, нет ненормативной лексики")
else:
    print(f"Правило 1: Нарушение! Ненормативная лексика: {rule_ban_words}")
if not rule_thanks:
    print("Правило 2: Нарушение! Нет благодарности!")
else:
    print(f"Правило 2: ОК, есть благодарность: {rule_thanks}")
if not rule_greetings:
    print("Правило 3: Нарушение! Нет приветствия!")
else:
    print(f"Правило 3: ОК, есть приветствие: {rule_greetings}")
if time >= 60:
    print(f"Правило 4: ОК, время разговора {time} больше минуты")
else:
    print(f"Правило 4: Нарушение, время разговора {time} меньше минуты")
if not rule_buy_dished:
    print("Правило 5: Нарушение! Не предложил купить посуду!")
else:
    print(f"Правило 5: ОК, предложил купить посуду: {rule_buy_dished}")