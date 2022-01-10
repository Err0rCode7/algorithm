import sys, heapq

input = sys.stdin.readline

t = int(input())

for i in range(t):
	k = int(input())
	file_size = list(map(int, input().rstrip().split()))
	heapq.heapify(file_size)
	result = 0
	while file_size:
		if len(file_size) == 1:
			break

		a, b = heapq.heappop(file_size), heapq.heappop(file_size)
		print(a, b)
		new = a + b
		result += new
		print(new)
		heapq.heappush(file_size, new)
	print(result)


