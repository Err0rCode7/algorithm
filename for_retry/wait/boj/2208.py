import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
gems = [0] * n
accumulated = [0] * n

total = 0
for i in range(n):
	gems[i] = int(input().rstrip())
	total += gems[i]
	accumulated[i] = total

min_left = 0
answer = 0
for i in range(m - 1, n):
	if i == m - 1:
		min_left = 0
	else :
		min_left = min(min_left, accumulated[i - m])
	answer = max(answer, accumulated[i] - min_left)

print(answer)