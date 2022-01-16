from collections import deque
from copy import deepcopy
from itertools import combinations

n, k = input().rstrip().split()
k = int(k)

index = [i for i in range(len(n))]
index_comb = list(combinations(index, 2))
result = [c for c in n]

# def dfs(size):
# 	global answer
# 	if size == k :
# 		answer = max(answer, int(''.join(result)))
# 		return
# 	temp = set()
# 	for a, b in index_comb:
# 		result[a], result[b] = result[b], result[a]
# 		snapshot = ''.join(result)
# 		if snapshot not in temp:
# 			temp.add(snapshot)
# 			if (snapshot[0] != '0'):
# 				dfs(size + 1)
# 		result[a], result[b] = result[b], result[a]

def bfs(q):
	dup_check = set()
	count = len(q)
	for i in range(count):
		number_list = q.popleft()
		for a, b in index_comb:
			number_list[a], number_list[b] = number_list[b], number_list[a]
			new_tuple = tuple(number_list)
			if new_tuple not in dup_check and new_tuple[0] != '0':
				new = deepcopy(number_list)
				dup_check.add(new_tuple)
				q.append(new)
			number_list[a], number_list[b] = number_list[b], number_list[a]

que = deque()
que.append(result)

for i in range(k):
	bfs(que)
answer = -1
while que:
	numbers = que.popleft()
	answer = max(answer, int(''.join(numbers)))
print(answer)