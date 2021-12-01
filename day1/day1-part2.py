def solve():
    data = []

    increases = 0
    decreases = 0
    same = 0

    previous = None

    with open('input.txt') as input:
        for value in input:
            data.append(int(value.strip()))

    for i in range(0, len(data) - 2):
        value = (data[i:i+3])

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


if __name__ == '__main__':
    solve()
