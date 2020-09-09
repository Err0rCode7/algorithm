import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())


def solution_1(N, K) :
	result = 0

	while N > 1 :
		if N >= K and N % K == 0 :
			N = N / K
		else :
			N -= 1
		result += 1
	return (result)

def solution_2(N, K) :
	result = 0

	while True :

		# K의 배수가 될 때까지 1씩 빼는 연산을 한번에 함
		target = (N // K) * K
		result += (N - target)
		# N은 현재 K의 배수
		N = target
		if N < K :
			break
		# N을 K로 나눈다.
		result += 1
		N //= K
	# N < K 의 경우 남은 1씩 빼는 연산을 한번에 수행
	result += (N - 1)
	return (result)

print(solution_2(N, K))
