import numpy as np
import matplotlib.pyplot as plt


def main():
    x = list(np.arange(-6, 8, 1))
    # fig, ax = plt.subplots(1, 1)
    y = spec(x)
    makep(x, y)
    plt.show()
    y = spec([i - 3 for i in x])
    makep(x, y)
    plt.show()
    y = spec([i + 2 for i in x])
    makep(x, y)
    plt.show()
    y = spec([-i for i in x])
    makep(x, y)
    plt.show()
    y = spec([-i + 1 for i in x])
    makep(x, y)
    plt.show()
    y = spec([-i - 2 for i in x])
    makep(x, y)
    plt.show()


def spec(r):
    return ramp([i + 4 for i in r]) - ramp([i - 4 for i in r]) - 8 * step([i - 4 for i in r]) - impulse([i + 3 for i in r])


def makep(x, y):
    plt.plot(x, y, 'o')
    plt.xlabel('n')
    plt.ylabel('y[n]')
    for i, j in zip(x, y):
        plt.vlines(i, 0, j, color='gray', linestyle='--')


def impulse(n: list):
    y = np.zeros(len(n))
    for i, j in enumerate(n):
        if j == 0:
            y[i] = 1
            break
    return y


def step(n: list):
    y = np.zeros(len(n))
    for i, j in enumerate(n):
        if j >= 0:
            y[i] = 1
    return y


def ramp(n: list):
    y = np.zeros(len(n))
    for i, j in enumerate(n):
        if j >= 0:
            y[i] = j
    return y


if __name__ == '__main__':
    main()
