import math

def circual(x):
    return math.sqrt(1 - x ** 2)

def integral(f, a, b, n):
    s = 0
    dx = (b - a) / n
    for i in range(1, n+1):
        s += dx *(f(a + i * dx))
    return 4 * s

def main():
    a = 0
    b = 1
    n = 23000
    f = circual
    t = 1
    p = integral(f, a, b, n)
    while p != t:
        t = p
        n += 1
        if n % 1000 == 0:
            print(n, "----->", p)
        p = integral(f, a, b, n)
    print(n, "--->", p)


main()
