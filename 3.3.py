def my_func(x, y, z):
    if x >= y >= z:
        return x + y
    elif x >= y and z >= y:
        return x + z
    else:
        return y + z


print(my_func(10, 5, 6))
