from collections import deque
import sys


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
