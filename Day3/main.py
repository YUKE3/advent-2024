

def part_one():
    total = 0

    with open("input.txt", "r") as file:
        for line in file:
            idx = 0
            while idx < len(line):
                idx = line.find("mul(", idx)
                if idx == -1:
                    break

                idx += 4
                i = idx

                # Get first number
                while i < len(line) and line[i].isnumeric():
                    i += 1
                if i == len(line) or i == idx or line[i] != ",":
                    continue
                x = int(line[idx:i])

                i += 1 # increment past ","
                idx = i

                # Get second number
                while i < len(line) and line[i].isnumeric():
                    i += 1
                if i == len(line) or i == idx or line[i] != ")":
                    continue
                y = int(line[idx:i])

                total += x * y
                idx = i

    return total

if __name__=="__main__":
    print("Part 1 answer:")
    print(part_one())
