# test case

# Q:
# 02984
# A:
# 576

# Q:
# 567
# A:
# 210

import sys

input = sys.stdin.readline

string = input().rstrip()

sum = 0

for s in string :
	n = int(s)

	if sum == 0 :
		sum += n
	else :
		sum *= n

print(sum)
