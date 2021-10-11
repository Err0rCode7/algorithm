# test case

# Q:
# 5 3
# 1 3 2 3 2

# A:
# 8

# Q:
# 8 5
# 1 5 4 3 2 4 5 2

# A:
# 25

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
balls = list(map(int, input().rstrip().split()))

balls.sort()

counts = [0 for _ in range(0, m + 1)]

for ball in balls:
	counts[ball] += 1

result = 0

# case 1
# 이 내용을 아래와 같이 수정하여 효율을 올림
# for score in range(1, m) :
# 	result += counts[score] * sum(counts[score + 1:])

# case 2
# 효율 상승
for score in range(1, m) :
	n -= counts[score]
	result += counts[score] * n

print(result)