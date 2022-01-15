import heapq

n, k = input().rstrip().split()
k = int(k)

hq = []
result = [0 for _ in range(len(n))]
result[0] = int(n[0])
exist = [0 for _ in range(10)]
hasDup = False
for i in range(1, len(n)):
	heapq.heappush(hq, (-int(n[i]), -i))
	result[i] = int(n[i])
	exist[result[i]] += 1
	if exist[result[i]] >= 2:
		hasDup = True

count = 0
i = 0
fail = False
answer = []
while count < k and len(result) > 1:
	if i + 2 == len(n):
		j = i + 1
		# 중복인데, 뒤에있는 수가 작으면 스왑 X
		if hasDup and result[i] >= result[j]:
			if i == 0 and result[i] == 0:
				fail = True
			break
		result[i], result[j] = result[j], result[i]
		if result[i] == 0 and i == 0:
			fail = True
			break
		count += 1
		continue

	# heap에서 빼기전에 힙의 최댓값이 현재 커서보다 작으면 커서를 넘어간다.
	# 이때 중복이 있다면 카운트도 넘어간다.
	if result[i] > -hq[0][0]:
		if i < -hq[0][1]:
			i += 1
			if hasDup:
				count += 1
			continue
	
	number, j = heapq.heappop(hq)
	number = -number
	j = -j
	# 동기화되지 않은 내용물
	if j < i or result[j] != number:
		continue
	# 자리 그대로 유지
	if result[i] == number and j == i:
		i += 1
		continue

	if i < j and result[j] < result[i]:
		i += 1
		continue

	# i를 j로 사용할 수 있도록 함
	heapq.heappush(hq, (-result[i], -j))
	# swap
	result[i], result[j] = result[j], result[i]
	if result[i] == 0 and i == 0:
		fail = True
		break
	count += 1
	i += 1

if fail or len(result) <= 1:
	print(-1)
else:
	for i in range(len(result)):
		print(result[i], end='')
	print()


'''
135745 5
135745 6 # 위 아래 경우가 같아야함

'''