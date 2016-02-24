from numpy import *

def CompSimp38(a, b, n):
    if n % 3 == 0:
        pass
    else:
        return print("Need a 'n' divisible by 3")

    x = linspace(a, b, n)
    y = 0
    fx = ones(len(x))
    h = (b - a) / n
    for i in range(len(x)):
        if x[i] > 2 or x[i] < -2:
            fx[i] = (x[i] / sqrt(x[i] ** 2 - 4))
        else:
            fx[i] = 0
    for i in range(len(x)):
        if i == 0 or i == n - 1:
            y += fx[i]
        elif i % 3 == 0:
            y += 2 * fx[i]
        else:
            y += 3 * fx[i]
    y = (y * 3 * h / 8)
    return y


print((CompSimp38(3, 4, 300)))

