str_list = ["Имеется", "список", "строк", "разной", "длины.", "Необходимо", "составить", "новый"]
n = len(max(str_list, key=lambda x: len(x)))
str_list = list(map(lambda x: x.rjust(n, "_"), str_list))
print(str_list)