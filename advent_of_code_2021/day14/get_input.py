from typing import Dict

from advent_of_code_2021.day14.Pair import Pair
from advent_of_code_2021.day14.Rule import Rule


def get_input(filename: str) -> str:
    with open(filename) as file:
        return next(file).strip()


def get_input_as_pairs(filename: str) -> Dict[Pair, int]:
    with open(filename) as file:
        polymer = next(file).strip()
        pairs = {}
        for i in range(len(polymer) - 1):
            if not polymer[i + 1]:
                break
            pair = Pair(polymer[i], polymer[i + 1])

            if pair not in pairs:
                pairs[pair] = 1
            else:
                pairs[pair] += 1

        return pairs


def get_rules(filename: str) -> Dict[str, Rule]:
    with open(filename) as file:
        next(file)
        next(file)

        rules = {}
        for line in file:
            data = line.strip().split(' -> ')
            rules[data[0]] = Rule(data[0], data[1])

        return rules
