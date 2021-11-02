import time

# lcg constants
M = 2 ** 31
A = 1103515245
C = 12345


def lcg(modulus, a, c, seed):
    # https://en.wikipedia.org/wiki/Linear_congruential_generator
    while True:
        seed = (a * seed + c) % modulus
        yield seed


def cut_to_range(start, end, generator, m):
    return round((end - start) * (next(generator) / m) + start)


def get_seed_from_time():
    # effective way to seed from time https://stackoverflow.com/a/45573061
    t = int(time.time() * 1000.0)
    return ((t & 0xff000000) >> 24) + \
           ((t & 0x00ff0000) >> 8) + \
           ((t & 0x0000ff00) << 8) + \
           ((t & 0x000000ff) << 24)


if __name__ == '__main__':
    print("Welcome to Random number generator using [Linear congruential generator]")
    option = 2
    start, end, count = 0, 100, 10
    while True:
        if option == 2:
            start = input("Please enter beginning of interval:\n")
            start = int(start)

            end = input("Please enter end of interval:\n")
            end = int(end)

            count = input("Please enter count of interval:\n")
            count = int(count)

        generator = lcg(M, C, A, get_seed_from_time())
        random_list = []
        for i in range(count):
            random_list.append(cut_to_range(start, end, generator, M))

        print(f'list={random_list}')

        option = 1
        input_option = input(
            '1- repeat with same argument\n'
            '2- repeat with different arguments\n'
            '3- exit\n')
        if input_option:
            option = int(input_option)

        if option == 3:
            exit()
