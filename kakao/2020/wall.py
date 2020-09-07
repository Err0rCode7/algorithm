# 원의 형태로 된 (머리와 꼬리가 연결된 형태) 형태에서 취약점을 고치기위한 agent의 최소 수를 구하는 문제이다.
# 각 agent별로 주어진 시간에 움직일 수 있는 거리가 다르다.
# 이 문제는 처음 접해본 유형으로 잘못된 방향으로 삽질을 한 문제이다.
# 문제의 키 포인트는 원의 형태인 것과 완전 탐색이다.
# 완전 탐색을 하기 위해 원의 형태를 연결된 형태로 나타내서 풀 수 있다.
# 예를 들어 길이가 12이고 취약점이 1, 5, 6, 10일 때를 보면,
# agent가 취약점을 고치기 위해서는 연속된 방향으로 이동을 해야한다.
# 하나의 agent가 취약점을 고칠 수 있는 경우의 수를 보기 위해서는 1에서 시계방향으로 시작하거나 반시계방향으로 시작하는 두개의 수 그리고
# 계속해서 5, 6, 10도 같은 방식으로 해보는 경우의 수가 있다 즉, 8개의 경우의 수가 있다.
# 여기서 1에서 시계방향으로 도는 것은 이 agent가 1에서 시작해서 도착하는 지점을 k라고 했을때 k를 출발점으로 하여 반 시계 방향으로 도는 것과 같은 방법이다.
# 따라서 한 방향만 고려하여 풀면 된다.
# 또한 한 방향으로만 생각을 하고 원의 형태(선형 형태로) 탐색하기 위해서는 10에서 출발하여 1에 도착한다고 했을 때를 10에서 1 + 12(전체 길이)라고 생각 하고 13에 방문 했을 때
# 1에 방문한 것과 같은 맥락으로 보면 되는 것이다.
# 즉, 1, 5, 6, 10 의 취약점을 늘려서 1, 5, 6, 10, 13, 17, 18, 22로 볼 수 있는 것이다.

# 위의 개념을 활용하여 문제를 해결하는 방법이 여러가지가 있다.
# 내가 알아본 방법으로는 dp와 완전탐색이 있다.
# dp의 경우는 위의 개념을 활용하여 agent가 이동거리가 큰 것부터 하여 한 명일때 두 명일때를 알아가는 방법이다.
# 첫 번째는 agent가 한명일 때의 모든 경우에 수를 해보고 취약점이 남아 있을 때를 저장하여 두 명일때 세 명일때를 해보는 방식이다.
# 만약 취약점이 없는 경우가 생긴다면, 그때의 agent 수를 구하여 답을 맞추는 방식이다.
# 완전 탐색은 permutation을 이용하여 모든 경우의 수를 따지는 방식이다.
# 취약점을 한번에 많이 해결하는 경우의 수를 따져서 문제를 해결하면 좋겠지만은 어려움이 있다.
# 따라서 각각의 agent가 배치되는 순서에 해당하는 경우의 수를 permutation으로 모두 해보는 방식이다.
# 모든 경우의 수로 완전 탐색을 하기 때문에 agent가 투입되는 최소의 수를 찾을 수 있다.

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

