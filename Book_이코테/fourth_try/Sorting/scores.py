import sys

input = sys.stdin.readline

n = int(input())

scores = []

for i in range(n):
	line = input().rstrip().split()
	line[1] = int(line[1])
	line[2] = int(line[2])
	line[3] = int(line[3])
	scores.append(line)

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for score in scores:
	print(score[0])