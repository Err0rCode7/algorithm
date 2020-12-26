import sys

input = sys.stdin.readline

N = int(input().rstrip())

house = list(map(int, input().rstrip().split()))

house.sort()

print(house[(N - 1) // 2])
