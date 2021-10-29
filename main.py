def lcg(modulus: int, a: int, c: int, seed: int) :
    while True:
        seed = (a * seed + c) % modulus
        yield seed


if __name__ == '__main__':
    start = input("Please enter beginig of interval:\n")
    start = int(start)

    end = input("Please enter end of interval:\n")
    end = int(end)

    seed = input("Please enter seed of interval:\n")
    seed = int(seed)

    print(f"start {start}")
    print(f"end {end}")
    print(f"seed {seed}")
