import datetime

def log_to_console_and_file(file_name = 'log.txt'):
    def decorator(func):
        def wrapper(*args, **kwargs):

            name = func.__name__
            start = datetime.datetime.now()

            with open(file_name, mode='a', encoding="utf-8") as f:
                f.write(f"{start}: Старт функции {name}.\n")

            result = func(*args, **kwargs)
            end = datetime.datetime.now()

            with open(file_name, mode='a', encoding="utf-8") as f:
                f.write(f"{end}: Функция {name} завершена.\n")
                # print(f"Время выполнения функции {name}: {end - start}")

            return result
        return wrapper
    return decorator

# @log_to_console_and_file('log.txt')
# def pow(x, y):
#     return x ** y

#print(pow(2, 10))