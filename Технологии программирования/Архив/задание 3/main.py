#  ЗАДАНИЕ
#
#  Вы аналитик внутри компании в отделе продаж. Вам нужно написать программу, которая принимаем данные о продажах за месяц (функция get_data) и формирует отчет, состоящий из:
#  1) total — общая выручка
#  2) most_expensive — самый дорогой товар по price
#  3) most_profitable — товар с максимальной выручкой, по сумме всех его строк
#  4) most_sold — товар с наибольшим суммарным quantity (с учётом дублей)
#  5) revenue_by_category — словарь: категория -> выручка, кол-во продаж
#  6) top_category — категория с максимальной выручкой
#
#  Отчет сохранить в файл (тип файла и вид отчета на ваш выбор)

from typing import List, Dict, Union
import sys
sys.path.insert(0, '../logger')
from logger import log_to_console_and_file


LOG_FILE = "log.txt"


@log_to_console_and_file(LOG_FILE)
def get_data() -> List[Dict[str, Union[str, int]]]:
    """Получение данных"""
    return [
        {"item": "Телефон X",   "category": "Электроника", "price": 25000, "quantity": 2},
        {"item": "Ноутбук Z",   "category": "Электроника", "price": 70000, "quantity": 1},
        {"item": "Планшет M",   "category": "Электроника", "price": 40000, "quantity": 3},
        {"item": "Наушники S",  "category": "Аксессуары",  "price": 3000,  "quantity": 5},
        {"item": "Чехол T",     "category": "Аксессуары",  "price": 500,   "quantity": 10},
        {"item": "Клавиатура K","category": "Периферия",   "price": 2000,  "quantity": 4},
        {"item": "Мышь L",      "category": "Периферия",   "price": 1500,  "quantity": 6},
        {"item": "Чехол T",     "category": "Аксессуары",  "price": 500,   "quantity": 7},
        {"item": "Наушники S",  "category": "Аксессуары",  "price": 3000,  "quantity": 2},
    ]


@log_to_console_and_file(LOG_FILE)
def generation_report(data: List[Dict[str, Union[str, int]]]) -> str:
    """
    Формирование текстового отчета
    :param data: статистика продаж
    :return: отчет в текстовой форме
    """
    report = ''

    @log_to_console_and_file(LOG_FILE)
    def universal_sum(func_sum, key_filter, new_key_name) -> list:
        """"
        Универсальный сумматор
        :param func_sum: функция суммирования
        :param key_filter: ключ, по которому производиться сумма
        :param new_key_name: имя нового ключа (значение - сумма)
        :return: список словарей
        """
        res = []
        for item in data:
            res.append({key_filter: item[key_filter],
                        new_key_name: sum([func_sum(i) for i in data if i[key_filter] == item[key_filter]])})
        return res

    # 1) общая выручка
    total = sum([i["price"] * i["quantity"] for i in data])
    report += f"1) общая выручка: {total}\n"

    # 2) самый дорогой товар по price
    most_expensive = max(data, key=lambda i: i["price"])
    most_expensive = {"item": most_expensive['item'], "price": most_expensive['price']}
    report += f"2) самый дорогой товар по price: {most_expensive}\n"

    # 3) товар с максимальной выручкой, по сумме всех его строк
    most_profitable = max(universal_sum(lambda i: i["price"] * i["quantity"], "item", "revenue"),
                          key=lambda i: i["revenue"])
    report += f"3) товар с максимальной выручкой, по сумме всех его строк: {most_profitable}\n"

    # 4) товар с наибольшим суммарным quantity (с учётом дублей)
    most_sold = max(universal_sum(lambda i: i["quantity"], "item", "quantity"),
                    key=lambda i: i["quantity"])
    report += f"4) товар с наибольшим суммарным quantity (с учётом дублей): {most_sold}\n"

    revenue_list = universal_sum(lambda i: i["price"] * i["quantity"], "category", "revenue")
    quantity_list = universal_sum(lambda i: i["quantity"], "category", "quantity")

    # 5) словарь: категория -> выручка, кол-во продаж
    revenue_by_category = [x | y for x, y in zip(revenue_list, quantity_list)]
    report += f"5) словарь: категория -> выручка, кол-во продаж: {revenue_by_category}\n"

    # 6) категория с максимальной выручкой
    top_category = max(revenue_list, key=lambda i: i["revenue"])
    report += f"6) категория с максимальной выручкой: {top_category}\n"

    return report


@log_to_console_and_file(LOG_FILE)
def save_report(data: str, path: str = r"./result.txt") -> None:
    """
    Сохранение отчета в файле
    :param data: отчет
    :param path: путь к файлу
    :return: None
    """
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(data)


@log_to_console_and_file(LOG_FILE)
def main():
    data = get_data()
    result = generation_report(data)
    save_report(result, "result.txt")


if __name__ == "__main__":
    main()