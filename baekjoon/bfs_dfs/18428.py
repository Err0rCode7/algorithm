import sys

# 완전 탐색 문제 (dx, dy 활용)
# 3개의 벽을 이용하여 선생님의 시야에 학생들이 있지 않는 방법이 존재하는지 판단하는 문제
# 'T'는 teacher 'S'는 student 'X'는 벽을 놓을 수 있는 빈 공간 'O'는 벽

# 선생님 리스트와 빈 공간 리스트를 각각 만들고
# 빈 공간 리스트에 3가지 경우의 수를 완전 탐색하여 대입해본다.
# 각각의 경우의 수 마다 선생님에게 걸리지 않는지 탐색하여 걸리지 않는 방법이 있다면 Yes,
# 전부 탐색하여 걸리지 않는 방법이 없다면 No를 출력한다.

def is_valid_graph(graph, t_list) :
	for t in range(len(t_list)) :
		x, y = t_list[t]
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			while dx[i] != 0 and nx < n and nx >= 0 :
				if graph[y][nx] == 'O':
					break
				if graph[y][nx] == 'S':
					return False
				nx += dx[i]
			while dy[i] != 0 and ny < n and ny >= 0 :
				if graph[ny][x] == 'O':
					break
				if graph[ny][x] == 'S':
					return False
				ny += dy[i]
	return True

def check_graph(graph) :
	t_list = []
	x_list = []

	for y in range (n) :
		for x in range (n) :
			if (graph[y][x] == 'T') :
				t_list.append((x, y))
			if (graph[y][x] == 'X') :
				x_list.append((x, y))

	for i in range(len(x_list)) :
		i_x, i_y = x_list[i]
		graph[i_y][i_x] = 'O'
		for j in range(i + 1, len(x_list)) :
			j_x, j_y = x_list[j]
			graph[j_y][j_x] = 'O'
			for k in range(j + 1, len(x_list)) :
				k_x, k_y = x_list[k]
				graph[k_y][k_x] = 'O'
				if is_valid_graph(graph, t_list) :
					return True
				graph[k_y][k_x] = 'X'
			graph[j_y][j_x] = 'X'
		graph[i_y][i_x] = 'X'
	return False


n = int(sys.stdin.readline().rstrip())
graph = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n) :
	graph.append(sys.stdin.readline().rstrip().split())

if (check_graph(graph) == True) :
	print("YES")
else :
	print("NO")
