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


def display_menu():
    return int(input(
        '1- repeat with same argument\n' +
        '2- repeat with different arguments\n'
        '3- read inputs from file (start,end,count,seed) each separated by new line\n'
        '4- exit\n'))


def first_time_display_menu():
    return int(input(
        '2- type arguments\n'
        '3- read inputs from file (start,end,count,seed) each separated by new line\n'
        '4- exit\n'))


if __name__ == '__main__':
    print("Welcome to Random number generator using [Linear congruential generator] Omar Ahmed Aly ID:200134")
    option = first_time_display_menu()
    start, end, count = 0, 100, 10
    seed_from_file = False
    while True:
        if option == 2:
            start = input("Please enter beginning of interval:\n")
            start = int(start)

            end = input("Please enter end of interval:\n")
            end = int(end)

            count = input("Please enter count of interval:\n")
            count = int(count)
        elif option == 3:
            seed_from_file = True
            with open('input', 'r') as f:
                start = int(f.readline())
                end = int(f.readline())
                count = int(f.readline())
                seed = int(f.readline())

        if not seed_from_file:
            seed = get_seed_from_time()

        generator = lcg(M, C, A, seed)
        random_list = []
        print(f'arguments = start: {start}, end: {end},count: {count},seed: {seed}')
        for i in range(count):
            random_list.append(cut_to_range(start, end, generator, M))

        print(f'list={random_list}')

        input_option = display_menu()

        option = 1  # initializing default value
        if input_option:
            option = int(input_option)

        if option == 4:
            exit()

