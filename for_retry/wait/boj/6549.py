from collections import deque
import sys

input = sys.stdin.readline

while True:
	heights = list(map(int, input().rstrip().split()))
	n = heights.pop(0)
	if n == 0:
		break
	result = 0
	q = deque()

	for i in range(n):
		if len(q) == 0:
			if heights[i] > 0:
				q.append((heights[i], i))
			continue
		if heights[i] > q[-1][0]:
			q.append((heights[i], i))
			result = max(result, heights[i])
		elif heights[i] < q[-1][0]:
			while q and heights[i] < q[-1][0]:
				cur_value, cur_index = q.pop()
				result = max(result, cur_value * (i - cur_index))
				pre_index = cur_index
			if q and q[-1][0] == heights[i]:
				continue
			if heights[i] > 0:
				q.append((heights[i], cur_index))
		else :
			continue
	while q:
		cur_value, cur_index = q.pop()
		result = max(result, cur_value * (n - cur_index))
	print(result)
