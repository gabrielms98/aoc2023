import re
import difflib

INPUTS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

regex = re.compile(r"one|two|three|four|five|six|seven|eight|nine")


def solve():
    with open("input.sol", "r") as f:
        sum = 0
        line = f.readline()
        count = 0
        while line:
            line = line.strip()
            for key, value in INPUTS.items():
                line = line.replace(key, f"{key[0]}{value}{key}")

            numbers = "".join(re.compile(r"\d").findall(line))
            sum += int(f"{numbers[0]}{numbers[-1]}")

            line = f.readline()
            count += 1

        return sum


if __name__ == "__main__":
    print(solve())
