import sys

# 이분탐색 문제

# n개의 떡을 남는 떡의 길이의 합이 m이 되도록 자를려고 할 때 자르는 길이가 최대가 되도록하는 길이

# solution :
# 이분탐색을 이용하여 자르는 길이를 최소값과 최대값범위에 따라 조정해나가면서 남는 떡의 길이를 비교한다.

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


