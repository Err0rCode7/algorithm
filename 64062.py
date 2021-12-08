import heapq

class Node :
	def __init__(self, index, value):
		self.left = None
		self.right = None
		self.index = index
		self.value = value


def solution(stones, k):
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
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))