try:
    with open("1_1.txt", "r") as f:
        numbers = [float(i) for i in f.read().split()]

    sum_numbers = sum(numbers)
    max_numbers = max(numbers)

    with open("1_1.txt", "a") as f:
        f.write('\n' + str(sum_numbers))
        f.write('\n' + str(max_numbers))

except FileNotFoundError as error:
    print(error)
