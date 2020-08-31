import sys

def ft_get_maxcut() :
	start, end = 0, max(items)
	result = 0

	while start <= end :
		height = 0
		cut_size = (start + end) // 2
		for i in items :
			if i - cut_size > 0 :
				height += i - cut_size
		if height >= m :
			start = cut_size + 1
			result = cut_size
		elif height < m :
			end = cut_size - 1
	return result

n, m = map(int, sys.stdin.readline().rstrip().split())
items = list(map(int, sys.stdin.readline().rstrip().split()))
print(ft_get_maxcut())


