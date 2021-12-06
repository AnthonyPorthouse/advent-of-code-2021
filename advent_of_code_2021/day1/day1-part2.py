def solve():
    data = []

    increases = 0
    decreases = 0
    same = 0

    previous = None

    for value in get_set():
        if previous:
            sumval = sum(value)
            sumprev = sum(previous)

            if sumval > sumprev:
                print(f"{sumval} - increase")
                increases += 1
            elif sumval < sumprev:
                print(f"{sumval} - decrease")
                decreases += 1
            else:
                print(f"{sumval} - no change")
                same += 1
        previous = value

    print(f"inc: {increases} dec: {decreases} same: {same}")


def get_set():
    a = None
    b = None
    c = None

    with open('input.txt') as input:
        for value in input:
            [a, b, c] = [b, c, int(value.strip())]

            if a is None:
                continue

            yield a, b, c


if __name__ == '__main__':
    solve()
