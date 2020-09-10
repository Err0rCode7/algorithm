import sys
sys.setrecursionlimit(10**6)

class node :

	def __init__(self, x, y, idx) :
		self.x = x
		self.y = y
		self.idx = idx
		self.left = 0
		self.right= 0
		self.r_boundary = 0
		self.l_boundary = 0

	def get_attr(self) :
		return (self.x, self.y, self.idx)

	def get_left(self) :
		return self.left

	def get_right(self) :
		return self.right

	def set_right(self, right) :
		self.right = right

	def set_left(self, left) :
		self.left = left

	def get_l_boundary(self) :
		return self.l_boundary

	def get_r_boundary(self) :
		return self.r_boundary

	def set_r_boundary(self, value) :
		self.r_boundary = value

	def set_l_boundary(self, value) :
		self.l_boundary = value

def	preorder(root, result) :
	if root == 0:
		return
	left = root.get_left()
	right = root.get_right()
	result.append(root.get_attr()[2])
	preorder(left, result)
	preorder(right, result)
	return (result)

def postorder(root, result) :
	if root == 0:
		return
	left = root.get_left()
	right = root.get_right()
	postorder(left, result)
	postorder(right, result)
	result.append(root.get_attr()[2])
	return (result)

# node : x, y, idx
# y가 클 수록 트리의 레벨이 낮음

## 100점, 간단한 문제 풀이
def solution(nodeinfo):
	for idx, _node in enumerate(nodeinfo) :
		_node.append(idx + 1)
	nodeinfo.sort(key= lambda x : (-x[1],x[0]))
	root = 0
	for x, y, idx in nodeinfo :

		c_node = root
		pre_node = 0
		while True :
			if root == 0 :
				root = node(x, y, idx)
				break
			cx, cy, c_idx = c_node.get_attr()
			if x < cx :
				pre_node = c_node
				c_node = c_node.get_left()
				if c_node == 0 :
					pre_node.set_left(node(x, y, idx))
					break
			else :
				pre_node = c_node
				c_node = c_node.get_right()
				if c_node == 0 :
					pre_node.set_right(node(x, y, idx))
					break
	return ([preorder(root, []), postorder(root, [])])

## 96점: 테스트 21번 실패
def solution_2(nodeinfo):
	x_len = 0
	for idx, _node in enumerate(nodeinfo) :
		if x_len < _node[0] :
			x_len = _node[0]
		_node.append(idx + 1)
	nodeinfo.sort(key= lambda x : (-x[1],x[0]))
	top = nodeinfo[0][1]
	level = [[]]
	level_idx = 0
	for x, y, idx in nodeinfo :
		if top == y :
			level[level_idx].append(node(x, y, idx))
		else :
			level.append([])
			top = y
			level_idx += 1
			level[level_idx].append(node(x, y, idx))

	if len(level) == 1 :
		return [[1],[1]]

	child = level[1]
	parent = level[0][0]
	px, py, pidx = parent.get_attr()
	root = parent
	root.set_l_boundary(0)
	root.set_r_boundary(x_len + 1)
	for c_node in child :
		cx, cy, cidx = c_node.get_attr()
		if cx > px :
			c_node.set_l_boundary(px)
			c_node.set_r_boundary(root.get_r_boundary())
			root.set_right(c_node)
		else :
			c_node.set_l_boundary(root.get_l_boundary())
			c_node.set_r_boundary(px)
			root.set_left(c_node)

	for i in range(1, len(level) - 1) :
		parent = level[i]
		child = level[i + 1]

		child_idx = 0
		for p_node in parent:
			for c_i in range(child_idx, len(child)) :
				c_node = child[c_i]
				r_b, l_b = p_node.get_r_boundary(), p_node.get_l_boundary()
				px, py, pidx = p_node.get_attr()
				cx, cy, cidx = c_node.get_attr()
				# 부모의 오른쪽 자식
				if px < cx and cx < r_b:
					c_node.set_l_boundary(px)
					c_node.set_r_boundary(r_b)
					p_node.set_right(c_node)
				# 부모의 왼쪽 자식
				elif l_b < cx and cx < px:
					c_node.set_l_boundary(l_b)
					c_node.set_r_boundary(px)
					p_node.set_left(c_node)
				else :
					child_idx = c_i
					break
			if c_i == len(child) : break
	pre_result = []
	post_result = []
	preorder(root, pre_result)
	postorder(root, post_result)
	answer = []
	answer.append(pre_result)
	answer.append(post_result)
	return answer

testcases = []
testcases.append([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	)
#testcases.append([[5,3],[4,2]])

print(solution(testcases.pop()))
