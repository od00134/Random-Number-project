import time

M = 2 ** 16 + 1
A = 75
C = 74


def lcg(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed


def cut_to_range(start, end, generator, m):
   return round((end - start) * (next(generator) / m) + start)


if __name__ == '__main__':
    start = input("Please enter beginig of interval:\n")
    start = int(start)

    end = input("Please enter end of interval:\n")
    end = int(end)

    count = input("Please enter count of interval:\n")
    count = int(count)

    seed = int(time.time())
    seed = int(seed)

    generator = lcg(M, C, A, seed)

    for i in range(count):
        print(cut_to_range(start, end, generator, M))
