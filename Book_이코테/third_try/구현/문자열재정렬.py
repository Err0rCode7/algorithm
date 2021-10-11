# test case

# Q:
# K1KA5CB7
# A:
# AJKDLSI412K4JSJ9D

import sys

input = sys.stdin.readline

string = input().rstrip()

sortedString = sorted(string)

index = 0
sum = 0

for i in range(len(sortedString)) :
	if not ('0' <= sortedString[i] <= '9' ) :
		index = i
		break
	sum += int(sortedString[i])
print(''.join(sortedString[index:]), end='')
print(sum)
