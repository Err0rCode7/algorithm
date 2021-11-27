import sys

input = sys.stdin.readline

n = int(input())
ugly = [1]

count = 0
index_2 = 0
index_3 = 0
index_5 = 0
while len(ugly) < n :

	next_value = min(ugly[index_2] * 2, ugly[index_3] * 3, ugly[index_5] * 5)
	if next_value == ugly[index_2] * 2 :
		index_2 += 1
	elif next_value == ugly[index_3] * 3 :
		index_3 += 1
	else :
		index_5 += 1
	if next_value != ugly[-1]:
		ugly.append(next_value)

print(ugly[n - 1])
