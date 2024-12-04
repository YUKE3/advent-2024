def part_one():
    safe = 0

    with open("input.txt", "r") as file:
        for line in file:
            levels = line.split(" ")

            diff = None
            val = int(levels.pop())
            while levels:
                next = int(levels.pop())
                new_diff = val - next
                if diff != None and new_diff ^ diff < 0:
                    break # different sign
                if abs(new_diff) > 3 or abs(new_diff) < 1:
                    break # out of range
                diff = new_diff
                val = next
            else:
                safe += 1

    return safe


def part_two():
    safe = 0

    with open("input.txt", "r") as file:
        for line in file:
            levels = list(map(int, line.split(" ")))

            diffs = []
            for i in range(1, len(levels)):
                diffs.append(levels[i] - levels[i-1])

            if check_diff_sequence(diffs, dampener=True):
                safe += 1

    return safe

def check_valid(diff, prev=None):
    if (
        abs(diff) < 1 or
        abs(diff) > 3 or
        (prev != None and prev ^ diff < 0)
    ):
        return False
    else:
        return True


def check_diff_sequence(seq, dampener=False):
    for i in range(len(seq)):
        prev = None if i == 0 else seq[i-1]
        if not check_valid(seq[i], prev):
            if not dampener:
                return False

            sequences = []

            if i == 0 or i == 1: # Remove leftmost
                sequences.append(seq[1:])

            if i != 0: # Combine with left
                left = seq.copy()
                left[i-1:i+1] = [seq[i-1] + seq[i]]
                sequences.append(left)

            if i != len(seq)-1: # Combine with right
                right = seq.copy()
                right[i:i+2] = [seq[i] + seq[i+1]]
                sequences.append(right)

            else: # Remove rightmost
                sequences.append(seq[:-1])


            for possible_seq in sequences:
                if check_diff_sequence(possible_seq):
                    return True

            # Can't be dampened
            return False

    return True


if __name__=="__main__":
    print("Part 1 answer:")
    print(part_one())

    print("Part 2 answer:")
    print(part_two())
