import re


def part1():
    with open("input.sol", "r") as f:
        data = f.read().splitlines()
        sum = 0
        for line in data:
            numbers = "".join(re.compile(r"\d").findall(line))
            sum += int(f"{numbers[0]}{numbers[-1]}")

        print(sum)


if __name__ == "__main__":
    part1()
