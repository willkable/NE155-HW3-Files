from numpy import *
import matplotlib.pyplot as plt


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


ny = []
nx = []
sl = []
for h in range(3, 300, 3):
    ny.append(abs(CompSimp38(3, 4, h) - 1.228))  # 1.228 is the actual values of integral from 3 to 4#
    nx.append(1 / h)


plt.plot(nx, ny, "ro")
plt.xlabel('h values')
plt.ylabel('error')
plt.title('h vs. error in SimpComp3/8')
plt.show()

slope = ((ny[len(ny) - 1] - ny[0]) / (nx[len(ny) - 1] - nx[0]))
print("Slope:", slope)
print("CompSimp38:", (CompSimp38(3, 4, 30)))
