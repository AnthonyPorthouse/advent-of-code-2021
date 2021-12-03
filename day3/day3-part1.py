from typing import List, Tuple

from day3.get_input import get_input


def solve(filename: str) -> None:
    high_totals = None
    low_totals = None

    for values in get_input(filename):
        if high_totals is None:
            high_totals = [0 for i in range(len(values))]
            low_totals = [0 for i in range(len(values))]
        for key, value in enumerate(values):
            if value is True:
                high_totals[key] += 1
            else:
                low_totals[key] += 1

    print(f"high_totals: {high_totals} low_totals: {low_totals}")

    gamma, epsilon = calculate_gamma_epsilon(high_totals, low_totals)

    print(f"gamma: {gamma} epsilon: {epsilon}")

    power_consumption = gamma * epsilon

    print(f"Power Consumption: {power_consumption}")


def calculate_gamma_epsilon(high_totals: List[int], low_totals: List[int]) -> Tuple[int, int]:
    gamma = epsilon = ''
    for k, v in enumerate(high_totals):
        v2 = low_totals[k]

        if v > v2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2), int(epsilon, 2)



if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
