import sys

input = sys.stdin.readline

instr = input().rstrip()

left, right = 0, 0
for i in range(len(instr) // 2) :
	left += int(instr[i])
	right += int(instr[-(i + 1)])

if left == right :
	print('LUCKY')
else :
	print('READY')
