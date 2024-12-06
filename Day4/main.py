def part_one():
    str_matrix = []
    with open("input.txt", "r") as file:
        for line in file:
            str_matrix.append(line.rstrip())

    m = len(str_matrix)
    n = len(str_matrix[0])

    xmas = 0

    def is_xmas(x0, y0, x1, y1, x2, y2):
        if min(x0, y0, x1, y1, x2, y2) < 0:
            return False

        if max(x0, x1, x2) >= m:
            return False

        if max(y0, y1, y2) >= n:
            return False

        return (
            str_matrix[x0][y0] == "X" and
            str_matrix[x1][y1] == "A" and
            str_matrix[x2][y2] == "S"
        )

    def get_occurrence(x, y):
        occurrences = 0

        horizontal_edge = (x == 0 or x == m-1)
        vertical_edge = (y == 0 or y == n-1)

        # Horizontal
        if not horizontal_edge:
            if (
                is_xmas(x-1, y, x+1, y, x+2, y) or
                is_xmas(x+1, y, x-1, y, x-2, y)
            ):
                occurrences += 1

        # Vertical
        if not vertical_edge:
            if (
                is_xmas(x, y+1, x, y-1, x, y-2) or
                is_xmas(x, y-1, x, y+1, x, y+2)
            ):
                occurrences += 1

        # Diagonals
        if not horizontal_edge and not vertical_edge:
            # /
            if (
                is_xmas(x-1, y-1, x+1, y+1, x+2, y+2) or
                is_xmas(x+1, y+1, x-1, y-1, x-2, y-2)
            ):
                occurrences += 1

            # \
            if (
                is_xmas(x-1, y+1, x+1, y-1, x+2, y-2) or
                is_xmas(x+1, y-1, x-1, y+1, x-2, y+2)
            ):
                occurrences += 1

        return occurrences


    for x in range(m):
        for y in range(n):
            if str_matrix[x][y] == "M":
                xmas += get_occurrence(x, y)

    return xmas



if __name__=="__main__":
    print("Part one answer:")
    print(part_one())
