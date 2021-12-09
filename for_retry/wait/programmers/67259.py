from collections import deque
import sys
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS
def bfs(board, visited, x, y, vector, cost):
	global dx, dy
	n = len(board)
	q = deque()
	q.append((x, y, vector, cost))
	while q :
		x, y, vector, cost = q.popleft()
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 0:
				n_cost = 100
				if not (x == 0 and y == 0) and i != vector and abs(vector - i) != 2:
					n_cost += 500
				if visited[ny][nx][i] > cost + n_cost:
					visited[ny][nx][i] = cost + n_cost
					q.append((nx, ny, i, cost + n_cost))

def solution_bfs(board):
	global _min

	n = len(board)
	visited = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]
	visited[0][0] = [0, 0, 0, 0]
	bfs(board, visited, 0, 0, 0, 0)
	return min(visited[n - 1][n - 1])

# 백준 배달문제랑 비슷 -> 배달문제 풀어봐야겠다..
# bfs를 고려해야함 -> 최소 금액을 찾아야하고 DP로 메모리제이션을 해서 가지치기를 뎁스가 낮을 때 빨리 하는 것이 좋음

# DFS
sys.setrecursionlimit(10000)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(board, visited, x, y, vector, cost):
	global dx, dy
	n = len(board)

	if not (x == 0 and y == 0) and visited[y][x][vector] <= cost:
		return
	visited[y][x][vector] = cost
	if x == n - 1 and y == n - 1:
		return
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 0:
			n_cost = 100
			if not (x == 0 and y == 0) and i != vector and abs(vector - i) != 2:
				n_cost += 500
			
			dfs(board, visited, nx, ny, i, cost+n_cost)

def solution_dfs(board):
	global _min
	n = len(board)
	visited = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]
	visited[0][0] = [0, 0, 0, 0]
	dfs(board, visited, 0, 0, 0, 0)
	return min(visited[n - 1][n - 1])


# dp solution
# 방향에 맞추어 현재를 기준으로 상하좌우의 dp를 저장
# n, n에 있는 좌표까지의 dp를 계산해야하므로 N*N번 반복
def solution_dp(board):
	N = len(board)
	#each block contains cost coming from up, down, left, right blocks
	map = [[[N*N*500+1 for i in range(4)] for j in range(N)] for k in range(N)]
	map[0][0] = [0, 0, 0, 0]
	for i in range(N * N):
		for r in range(N):
			for c in range(N):
				if r-1>-1 and board[r-1][c]==0:
					map[r-1][c][1] = min(map[r-1][c][1], map[r][c][0]+600, map[r][c][1]+100, map[r][c][2]+600, map[r][c][3]+600)
				if r+1<N and board[r+1][c]==0: 
					map[r+1][c][0] = min(map[r+1][c][0], map[r][c][0]+100, map[r][c][1]+600, map[r][c][2]+600, map[r][c][3]+600)
				if c-1>-1 and board[r][c-1]==0:
					map[r][c-1][3] = min(map[r][c-1][3], map[r][c][0]+600, map[r][c][1]+600, map[r][c][2]+600, map[r][c][3]+100)
				if c+1<N and board[r][c+1]==0:
					map[r][c+1][2] = min(map[r][c+1][2], map[r][c][0]+600, map[r][c][1]+600, map[r][c][2]+100, map[r][c][3]+600)
	return min(map[N-1][N-1])

print(solution_dp([[0,0,0],[0,0,0],[0,0,0]]))
print(solution_dp([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	))
print(solution_dp([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	))
print(solution_dp([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	))