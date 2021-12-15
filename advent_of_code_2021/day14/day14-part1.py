import math

from advent_of_code_2021.day14.get_input import get_input, get_rules


def solve(filename: str) -> None:
    polymer = get_input(filename)

    rules = get_rules(filename)

    for _ in range(10):
        next_polymer = ''
        for i in range(len(polymer)):
            chunk = polymer[i:i + 2]

            if chunk in rules:
                rule = rules[chunk]
                next_polymer += rule.new_value[:-1]
            else:
                next_polymer += polymer[i]

        polymer = next_polymer

    print(f'polymer length: {len(polymer)}')
    totals = {}
    for element in polymer:
        if element not in totals:
            totals[element] = 0

        totals[element] += 1

    most = 0
    least = math.inf
    for el, count in totals.items():
        most = max(most, count)
        least = min(least, count)

    print(f'score: {most - least}')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
