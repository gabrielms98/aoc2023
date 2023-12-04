import re


def part1():
    with open("input.sol", "r") as f:
        line = f.readline()
        sum = 0
        while line:
            numbers = "".join(re.compile(r"\d").findall(line))
            sum += int(f"{numbers[0]}{numbers[-1]}")

            line = f.readline()

        print(sum)


if __name__ == "__main__":
    part1()
