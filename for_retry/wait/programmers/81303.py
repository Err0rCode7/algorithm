from collections import deque

def solution(n, k, cmd):
	table = [[True, True] for _ in range(n)]
	dead = deque()
	for c in cmd:
		ec, count = 0, 0
		if len(c) >= 3:
			ec, count = c[0], int(c[2:])
			if ec == 'D':
				move = 0
				while move < count:
					k += 1
					if table[k][0] == True:
						move +=1
			else :
				move = 0
				while move < count:
					k -= 1
					if table[k][0] == True:
						move +=1
		else :
			ec = c[0]
			if ec == 'C':
				table[k][0] = False
				dead.append(k)
				met = False
				# 아래로 탐색
				move = 1
				while move + k < n:
					if table[move + k][0] == True:
						met = True
						break
					move += 1
				if met :
					k = move + k
				else :
					move = -1
					# 위로 탐색
					met = False
					while move + k >= 0:
						if table[move + k][0] == True:
							met = True
							break
						move -= 1
					k = move + k

			else : # ec == 'Z'
				reindex = dead.pop()
				table[reindex][0] = True
	answer = ""
	for i in range(n):
		if table[i][0]:
			answer += 'O'
		else:
			answer += 'X'
	return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))