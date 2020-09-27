
def dfs_permu(mylist, selected, level, result, index) :

	if level != len(mylist) :
		for i in range(len(mylist)) :
			if selected[i] :  continue
			selected[i] = True
			if level > 0 and len(result[index[0]]) == 0:
				for j in range(level):
					result[index[0]].append(result[index[0] - 1][j])
			result[index[0]].append(mylist[i])
			dfs_permu(mylist, selected, level + 1, result, index)
			selected[i] = False
	else :
		result.append([])
		index[0] += 1

def solution(mylist) :
	length = len(mylist)

	selected = [False for i in range(length)]
	result = [[]]
	dfs_permu(mylist, selected, 0, result, [0])
	return (sorted(result[:-1]))


solution([2,1])
solution([1,2,3,4])
