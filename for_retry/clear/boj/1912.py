import sys

input = sys.stdin.readline

n = int(input())
_sum = [0] * n
numbers = list(map(int, input().rstrip().split()))

total = 0
for i in range(n):
	total += numbers[i]
	_sum[i] = total

min_left = 0
_max = _sum[0]
for i in range(1, n):
	min_left = min(min_left, _sum[i - 1])
	_max = max(_max, _sum[i] - min_left)

print(_max)