# BOJ 18406

# Q:
# 123402
# A:
# LUCKY

# Q:
# 7755
# A:
# READY

import sys

input = sys.stdin.readline

numbers = list(map(int, input().rstrip()))

if sum(numbers[:len(numbers) // 2]) == sum(numbers[len(numbers) // 2:]) :
	print("LUCKY")
else :
	print("READY")