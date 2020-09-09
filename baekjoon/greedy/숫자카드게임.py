import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

max_num = 0

for i in range(N) :
	data = list(map(int, input().rstrip().split()))
	max_num = max(max_num, min(data))

print(max_num)
