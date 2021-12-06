from advent_of_code_2021.day6.School import School
from advent_of_code_2021.day6.get_input import get_input


def solve(filename: str) -> None:
    initial_state = [val for val in get_input(filename)]
    school = School(initial_state)

    print(f'Initial State: {school}')
    for i in range(80):
        school.tick()
        print(f'After {i + 1} days {school.count_fish()} fish')


if __name__ == '__main__':
    solve('example.txt')
    solve('input.txt')
