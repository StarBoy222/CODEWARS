def is_divide_by(number, a, b):
    x = abs(number)
    y = abs(a)
    z = abs(b)
    if (x % y == 0) and (x % z == 0):
        Lucky = True
    else:
        Lucky = False
    return Lucky