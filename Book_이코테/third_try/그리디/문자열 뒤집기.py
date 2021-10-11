# BOJ 1439

# test case

# Q:
# 0001100
# A:
# 1

import sys

input = sys.stdin.readline

string = input().rstrip()

target = string[0]
result = 0

for i in range(1, len(string)):
	if target != string[i] and string[i] != string[i - 1]:
		result += 1

print(result)