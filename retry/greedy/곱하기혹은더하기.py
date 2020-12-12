import sys

input = sys.stdin.readline

S = input().rstrip()

result = 0
for i in S :
	num = int(i)
	if result <= 1 or num <= 1:
		result += num
	else :
		result *= num
print(result)
