import sys
input=sys.stdin.readline

class Node :

	def __init__(self, left, right, value) -> None:
		self.leftchild = left
		self.rightchild = right
		self.value = value

def init_tree(node, s, e, array):

	if s == e:
		node.value = array[s]
	mid = (s + e) // 2
	node.left = Node(s, mid, 0)
	node.right = Node(s, mid, 0)
	init_tree(node.left, s, mid, array)
	init_tree(node.right, mid + 1, e, array)

	if node.left.value < node.right.value :
		node.value = node.left.value
	else:
		node.value = node.right.value

def find_min(root, s, e, rs, re):

	if s == rs and e <= re:
		return root.value
	if re == e and rs <= s:
		return root.value
	mid = (e + s) // 2
	left, right = -1, -1
	if s <= rs <= mid:
		left = find_min(root.left, s, mid, rs, re)
	if e >= re >= mid + 1:
		right = find_min(root.right, mid + 1, re, rs, re)
	if left == -1 :
		return right
	else:
		return left

def query(root, array_size, s, e):

	if s == e:
		return root.value
	length = e - s + 1

while True:
	heights = list(map(int, input().rstrip().split()))
	n = heights.pop(0)
	if n == 0:
		break
	
	root = Node(None, None, 0)
	init_tree(root, 0, n - 1, heights)

	
