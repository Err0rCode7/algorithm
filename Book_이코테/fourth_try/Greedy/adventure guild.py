'''
모험가 길드

공포도가 X인 모험가는 반드시 X명 이상으로 구성
'''

import sys

# Input

input = sys.stdin.readline
n = int(input())
phobiaLevelList = list(map(int, input().rstrip().split()))

# Sort

phobiaLevelList.sort()

# Main

count = 0
groupCount = 0

for level in phobiaLevelList :
	count += 1
	if count >= level :
		count = 0
		groupCount += 1
print(groupCount)