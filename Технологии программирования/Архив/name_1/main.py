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
# Нужно: прочитать оба файла, собрать единый поток реплик с указанием говорящего
# и склеить соседние фрагменты одного говорящего в полноценные предложения. Результат сохранить в файл result.json


from typing import Dict, List, Union
import json
from itertools import zip_longest
import sys
from logger.logger import log_to_console_and_file


PUNCTUATION_MARKS = (".", "!", "?")
LOG_FILE = "name_1\\log.txt"

@log_to_console_and_file(LOG_FILE)
def combine_calls(first_call: List[Dict[str, Union[str, int]]],
                  second_call: List[Dict[str, Union[str, int]]]) -> List[Dict[str, str]]:
    """
    Объединения каналов транскрибации звонков
    :param first_call: левый канал (оператор)
    :param second_call: правый канал (клиент)
    :return: итоговая транскрибация диалога
    """

    result = []
    first_sentence = {}
    second_sentence = {}
    for first_word, second_word in zip_longest(first_call, second_call, fillvalue=None):
        first_flag = True
        second_flag = True
        if not first_sentence and (not first_word is None):
            first_sentence = first_word
            first_sentence["text"] = "ОПЕРАТОР: " + first_sentence["text"]
            first_flag = False
        if not second_sentence and (not second_word is None):
            second_sentence = second_word
            second_sentence["text"] = "КЛИЕНТ: " + second_sentence["text"]
            second_flag = False
        if (not first_word is None) and first_flag:
            if first_word["text"][0] != "-":
                first_sentence["text"] += " " + first_word["text"]
            else:
                first_sentence["text"] += first_word["text"]
            first_sentence["end"] = first_word["end"]
            if first_word["text"][-1] in PUNCTUATION_MARKS:
                result.append(first_sentence)
                first_sentence = {}
        if (not second_word is None) and second_flag:
            if second_word["text"][0] != "-":
                second_sentence["text"] += " " + second_word["text"]
            else:
                second_sentence["text"] += second_word["text"]
            second_sentence["end"] = second_word["end"]
            if second_word["text"][-1] in PUNCTUATION_MARKS:
                result.append(second_sentence)
                second_sentence = {}
    result.sort(key=lambda i: i["end"])
    result_text = '\n'.join(i["text"] for i in result)
    return result_text


@log_to_console_and_file(LOG_FILE)
def get_calls(path: str = r"./f1.json") -> List[Dict[str, Union[str, int]]]:
    """
    Получение транскрибации разговора из файла
    :param path: путь к файлу
    :return: диалог участника
    """
    import os
    print(os.getcwd())
    print(path)
    with open(path, mode="r", encoding="utf-8") as f:
        text_of_call = json.load(f)
    return text_of_call


@log_to_console_and_file(LOG_FILE)
def save_result(text: str, path: str = r"./result.json") -> None:
    """
    Сохранение результатов в файл
    :param path:
    :param text: итоговая транскрибация диалога
    :return:
    """
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(text)


@log_to_console_and_file(LOG_FILE)
def main():
    """
    Основная функция
    :return: None
    """
    # Тут писать код <-
    first_call = get_calls("name_1\\f1.json")
    second_call = get_calls("name_1\\f2.json")
    result = combine_calls(first_call, second_call)
    save_result(result, "name_1\\result.json")


if __name__ == '__main__':
    main()