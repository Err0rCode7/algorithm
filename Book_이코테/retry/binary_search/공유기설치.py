# BOJ 2110

import sys

input = sys.stdin.readline

N, C = map(int, input().rstrip().split())

array = []
for i in range(N):
	array.append(int(input().rstrip()))

array.sort()

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0
while start <= end:

	mid = (end + start) // 2
	value = array[0]
	count = 1
	for i in range(1, N):
		if array[i] >= value + mid:
			count += 1
			value = array[i]
	if count >= C:
		start = mid + 1
		result = mid
	else :
		end = mid - 1

print(result)
