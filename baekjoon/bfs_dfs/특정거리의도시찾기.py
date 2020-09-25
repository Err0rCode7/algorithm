from collections import deque
n, m, k, x = map(int, input().split())

city = [[] for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]
for i in range(m) :
	a, b = map(int, input().split())
	city[a].append(b)

queue = deque()
queue.append(x)
while queue :
	x = queue.popleft()
	for node in city[x] :
		if distance[node] == 0 or distance[node] > distance[x] + 1:
			distance[node] = distance[x] + 1
			queue.append(node)
flag = True
for index, value in enumerate(distance) :
	if value == k :
		flag = False
		print(index)
if flag :
	print(-1)
