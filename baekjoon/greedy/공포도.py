import sys

input = sys.stdin.readline
n = int(input().rstrip())
fear = list(map(int, input().rstrip().split()))

count = 0
result = 0
for f in fear :
	count += 1
	if count >= f :
		result += 1
		count = 0

print(result)
