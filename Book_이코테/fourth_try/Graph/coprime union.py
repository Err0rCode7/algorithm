
def find_parent(parent, x):
	if parent[x]!= x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union(parent, a, b):

	pa = find_parent(parent, a)
	pb = find_parent(parent, b)

	if pa < pb :
		parent[b] = pa
	else :
		parent[a] = pb
	
