from bisect import bisect_left, bisect_right
import sys

# 이분탐색을 이용한 라이브러리 사용해보기

# bisect_left : 이분탐색을 이용하여 리스트에서 왼쪽부터 값이 일치하는 첫번째 인덱스 값
# bisect_right : 이분탐색을 이용하여 리스트에서 오른쪽부터 값이 일치하는 인덱스의 다음 값

def count_by_range(array, left_value, right_value) :
	right_index = bisect_right(array, right_value)
	left_index = bisect_left(array, left_value)
	return right_index - left_index

n, x = map(int, sys.stdin.readline().rstrip().split())
input_list = list(map(int, sys.stdin.readline().rstrip().split()))
input_list.sort()
count = count_by_range(input_list, x, x)
print(-1 if count == 0 else count)
