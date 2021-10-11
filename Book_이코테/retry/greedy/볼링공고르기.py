import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
balls = list(map(int, input().rstrip().split()))


def solution_1():
	# O(n^2)
	global N, M, balls
	result = 0

	for i in range(len(balls)) :
		ball_1 = balls[i]
		for j in range(i + 1, len(balls)):
			if ball_1 != balls[j]:
				result += 1
	print(result)

def solution_2():
	# O(n)
	global N, M, balls
	result = 0

	ball_list = [0] * 11
	for weight in balls :
		ball_list[weight] += 1

	for count in ball_list :
		N -= count
		result += count * N
	print(result)

solution_2()
