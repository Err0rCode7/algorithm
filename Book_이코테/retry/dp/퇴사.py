import sys

input = sys.stdin.readline

n = int(input().rstrip())

calendar = []

for i in range(n):
	time, price = map(int, input().rstrip().split())

	calendar.append([time, price])

result = 0

for i in range(n - 1, -1, -1):
	time, price = calendar[i]

	if i + time > n:
		calendar[i][1] = 0
		continue
	if i + time != n:
		_max = 0
		for j in range(i + time, n):
			t, p = calendar[j]
			_max = max(_max, p)
		calendar[i][1] += _max
	result = max(result, calendar[i][1])
print(result)

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
'''