from collections import deque

n = int(input())

numbers = list(map(int, input().rstrip().split()))

stack = deque()
results = []
for i in range(n - 1, -1, -1):
	while stack and stack[-1] <= numbers[i]:
		stack.pop()
	result = -1
	if stack :
		result = stack[-1]
	stack.append(numbers[i])
	results.append(result)

for number in results[::-1]:
	print(number, end=' ')
print()
