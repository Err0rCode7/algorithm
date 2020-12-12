import sys

input = sys.stdin.readline

instr = input().rstrip()

pre = 2
group = [0, 0]

for i in instr :
	num = int(i)
	if pre == num :
		continue
	else :
		group[num] += 1
	pre = num
print(min(group))
