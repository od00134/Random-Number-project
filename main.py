import time
M = 2 ** 16 + 1
A = 75
C = 74


def lcg(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed


if __name__ == '__main__':
    # start = input("Please enter beginig of interval:\n")
    # start = int(start)
    #
    # end = input("Please enter end of interval:\n")
    # end = int(end)
    #
    seed = int(time.time())
    seed = int(seed)
    #
    # print(f"start {start}")
    # print(f"end {end}")
    # print(f"seed {seed}")
    generator = lcg(M, C, A, seed)
    for i in range(5):
        print(next(generator))
