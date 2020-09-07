# 이차원 배열을 다뤄서 해결 하는 문제
# 두개의 사각형의 맵을 이용하여 하나는 자물쇠로 사용하고 하나는 열쇠로 사용하여 완전 탐색하는 문제이다.
# 맵을 회전하는 방법을 알고 있어야한다. (이차원 배열 인덱스 인풋, 아웃풋 값을 이용해여 회전을 유도하면 된다.)
# 아래의 코드구현은 키에 해당하는 맵을 상하좌우를 자물쇠의 크기만큼 확장하여 5중 반복문을 사용하여 완전 탐색했다.
# 시간복잡도 분석을 하면 O(4 * (key + lock)^2 * lock^2)로 O(n^4)가 된다.
# 추가로 예외처리(if문 처리)를 이용하여 굳이 맵을 확장하지 않고 기존의 맵을 갖고 적용하여 풀 수도 있을 것 같다.

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate(key) :
	length = len(key)
	rotate = [[] for _ in range(length)]
	for y in range(length) :
		for x in range(length) :
			rotate[y].append(key[length - 1 - x][y])
	return rotate

def reverse(key) :
	length = len(key)
	reverse = [[] for _ in range(length)]
	for x in range(length) :
		reverse[y].append(key[y][length - 1 - x])
	return reverse

def is_valid(lock, key_extend, a, b, key_len) :
	for y in range(len(lock)) :
		for x in range(len(lock)) :
			if lock[y][x] + key_extend[a + y][b + x] >= 2  or \
				lock[y][x] + key_extend[a + y][b + x] == 0 :
				return False
	return True

def solution(key, lock) :
	key_len = len(key)
	lock_len = len(lock)
	key_extend = [[0 for _ in range(key_len + lock_len * 2)] for _ in range(key_len + lock_len * 2)]
	for y in range(key_len) :
		for x in range(key_len) :
			key_extend[y + lock_len][x + lock_len] = key[y][x]
	i = 0
	while i < 4 :
		for a in range(0, lock_len + key_len + 1) :
			for b in range(0, lock_len + key_len + 1) :
				if is_valid(lock, key_extend, a, b, key_len) :
					return True
		key_extend = rotate(key_extend)
		i += 1
	return False

print(solution(key, lock))
