import heapq
from collections import Counter

def main():
    leftHeap = []
    rightHeap = []

    with open("input.txt") as file:
        for line in file:
            l, r = line.split("   ")
            heapq.heappush(leftHeap, int(l))
            heapq.heappush(rightHeap, int(r))

    counter = Counter(rightHeap)

    distance = 0
    similarity = 0
    while leftHeap:
        left = heapq.heappop(leftHeap)
        distance += abs(left - heapq.heappop(rightHeap))
        similarity += left * counter[left]


    print("Part 1 Answer:")
    print(distance)

    print("Part 2 Answer:")
    print(similarity)


if __name__ == "__main__":
    main()

