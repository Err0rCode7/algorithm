import heapq

class Node :
	def __init__(self, index, value):
		self.left = None
		self.right = None
		self.index = index
		self.value = value


def solution(stones, k):
	# 연결리스으 NlogN + N
	n = len(stones)
	listArray = [0] * n
	pre = None
	head = None
	heap = []
	for i in range(n):
		node = Node(i, stones[i])
		if head == None:
			head = node
		if pre != None:
			node.left = pre
			pre.right = node
		pre = node
		listArray[i] = node
		heapq.heappush(heap, (stones[i], i))


	time = 0

	while heap:
		stone, index = heapq.heappop(heap)
		node = listArray[index]
		left = node.left
		right = node.right
		time = stone
		if left != None and right != None:
			if right.index - left.index > k:
				break
			left.right = right
			right.left = left
		elif left == None and right != None:
			if right.index >= k :
				break
			right.left = None
		elif left != None and right == None:
			if n - left.index > k :
				break
			left.right = None

	return time

def solution2(stones, k):
	# 이분탐색 풀이
	# NlogM
	
	s = 1
	e = max(stones)
	answer = 1
	while s <= e:
		mid = (e + s) // 2
		count = 0
		possible = True
		for stone in stones:
			# 이미 모두 밟아서 못건너는 스톤일때
			if stone < mid :
				count += 1
				# 못밟는 스톤이 연속해서 k개 있으면 인원 수를 줄임
				if count == k :
					e = mid - 1
					possible = False
					break
			else :
				count = 0
		
		if possible :
			# 현재 인원 수에서 가능하므로 인원 수를 더 올려본다.
			answer = max(answer, mid)
			s = mid + 1
	return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution2([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))