import time

from advent_of_code_2021.day6.School import School
from advent_of_code_2021.day6.get_input import get_input


def solve(filename: str) -> None:
    initial_state = [val for val in get_input(filename)]
    school = School(initial_state)

    print(f'Initial State: {school}')
    for i in range(256):
        print(f"Day {i+1}")
        school.tick()

    print(f'After {256} days {school.count_fish()} fish')


if __name__ == '__main__':
    start_time = time.perf_counter()
    solve('example.txt')
    result = time.perf_counter() - start_time

    print(f'Time taken: {result * 1000}ms')
    start_time = time.perf_counter()
    solve('input.txt')
    result = time.perf_counter() - start_time

    print(f'Time taken: {result * 1000}ms')
