import math

from advent_of_code_2021.day14.get_input import get_rules, get_input_as_pairs, get_input


def solve(filename: str) -> None:
    input = get_input(filename)
    pairs = get_input_as_pairs(filename)

    print(pairs)

    rules = get_rules(filename)

    totals = {}
    for i in input:
        if i not in totals:
            totals[i] = 0
        totals[i] += 1


    for i in range(40):
        next_pairs = pairs.copy()
        for pair in pairs.keys():

            if str(pair) not in rules:
                continue

            rule = rules[str(pair)]

            if rule.insert not in totals:
                totals[rule.insert] = 0

            a, b = rule.new_pairs
            if a not in next_pairs:
                next_pairs[a] = 0
            if b not in next_pairs:
                next_pairs[b] = 0

            amount = pairs[pair]
            next_pairs[pair] -= amount
            next_pairs[a] += amount
            next_pairs[b] += amount
            totals[rule.insert] += amount

        pairs = next_pairs

    print(pairs)
    print(totals)

    print(f'Score: {max(totals.values()) - min(totals.values())}')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
