import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

result = []
sequence = []
numbers = deque()

for i in range(n):
	numbers.append(int(input().rstrip()))

i = 0
while True :
	# print(sequence, numbers, i)
	if sequence and sequence[-1] == numbers[0]:
		numbers.popleft()
		result.append("-")
		sequence.pop()
		continue
	i += 1
	if i == n + 1:
		break
	result.append("+")
	sequence.append(i)

if numbers :
	print("NO")
else :
	for c in result:
		print(c)
