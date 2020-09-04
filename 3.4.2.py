def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


print(my_func(5, -2))
