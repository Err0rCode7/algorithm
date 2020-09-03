testcase = []
testcase.append((12, [1, 5, 6, 10], [1, 2, 3, 4]))
testcase.append((12, [1, 3, 4, 9, 10], [3, 5, 7]))

def get_clock_dist(a, b, n) :
	value = 0
	if a > b :
		value = a - b
	else :
		value = b - a
	return n - value if n - value < value else value

def solution(n, weak, dist):
	answer = 0
	node_list = [[] for _ in range(len(weak))]
	for i in range(len(weak)) :
		left = i - 1
		right = i + 1
		if left < 0 :
			left = len(weak) - 1
		if right == len(weak) :
			right = 0
		node_list[i].append((get_clock_dist(weak[i], weak[left], n), left))
		node_list[i].append((get_clock_dist(weak[i], weak[right], n), right))

	dist.reverse()
	visited = []
	left = node_list[0][0]
	right = node_list[0][1]
	right_v = right[0]
	left_v = left[0]
	visited.append(0)
	sum = 0
	for i in range(len(dist)) :
		while len(visited) != len(node_list) :
			print("left: ",left)
			print("right: ",right)
			if left_v <= right_v and dist[i] + rest >= sum + left_v:
				sum += left_v
				visited.append(left[1])
				left = node_list[left[1]][0]
				left_v = left[0]
				print("dist[i]: ", dist[i])
				print("sum: ", sum)
				print("visited: ", visited)
			elif left_v > right_v and dist[i] >= sum + right_v:
				sum += right_v
				visited.append(right[1])
				right = node_list[right[1]][1]
				right_v = right_v
				print(visited)
			else :
				sum = 0
				break
		if len(visited) == len(node_list) :
			answer = i + 1
			break
	return answer

for a, b, c in testcase :
	print("answer: ", solution(a, b, c))

