def solve():
    increases = 0
    decreases = 0
    same = 0

    previous = None

    with open('input.txt') as input:
        for value in input:
            value = int(value.strip())
            if not value:
                continue

            if previous:
                if value > previous:
                    print(f"{value} - increase")
                    increases += 1
                elif value < previous:
                    print(f"{value} - decrease")
                    decreases += 1
                else:
                    print(f"{value} - no change")
                    same += 1

            previous = value

    print(f"inc: {increases} dec: {decreases} same: {same}")


if __name__ == '__main__':
    solve()
