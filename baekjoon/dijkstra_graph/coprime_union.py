import sys

# 서로소 합집합 그래프
# parent 리스트에 자기 자신으로 초기화를 해놓은 상태로 시작한다.
# 두 개의 노드를 서로소 형태로 합할때 두개의 부모 노드를 찾아서 한쪽이 다른 한쪽에 종속되도록 연결한다.
# 연결하기위해 부모 노드를 탐색할 때 자기 자신의 값과 일치하지 않으면 부모 값이 다른 노드를 참조하는 것이므로
# 자기 자신의 부모의 값을 찾고 연결한다. (최대 depth까지 탐색하는 것)

def find_parent(parent, x) :
	if parent[x] != x :
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b) :
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if (a < b) :
		parent[b] = a
	else :
		parent[a] = b

input = sys.stdin.readline
v, e = map(int, input().rstrip().split())
parent = [0] * (v + 1)

for i in range(1, v + 1) :
	parent[i] = i

for i in range(e) :
	a, b = map (int, input().rstrip().split())
	union_parent(parent, a, b)

print('각 원소가 속한 집합:', end='')
for i in range(1, v + 1):
	print(find_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end='')
for i in range(1, v + 1):
	print(parent[i], end=' ')
