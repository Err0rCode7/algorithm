import sys

input = sys.stdin.readline

N = int(input().rstrip())

lines = []

for i in range(N):
	line = list(input().rstrip().split())
	for j in range(1,4):
		line[j] = int(line[j])
	lines.append(line)

lines.sort(key= lambda x:(-x[1], x[2], -x[3], x[0]))

for line in lines:
	print(line[0])
