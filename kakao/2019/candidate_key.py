
testcases = []
testcases.append([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

from itertools import combinations

def solution(relation) :

	row_len = len(relation)
	col_len = len(relation[0])
	col_list = range(col_len)

	unique = []
	for i in range(1, col_len + 1) :
		# combinations을 이용하여 col 인덱스를 이용한 모든 조합을 시도해본다.
		comb = combinations(col_list, i)
		for comb_col_list in list(comb) :
			# tmp에 튜플 형태로 row에 해당하는 값을 넣고
			# 집합 형태로 만들어서 중복을 제거한다
			# 이 집합의 길이가 릴레이션의 행의 수와 다르다면 유일성을 만족하지 못한다.
			tmp = [tuple([row[idx] for idx in comb_col_list]) for row in relation]
			if len(set(tmp)) == row_len :
				unique.append(set(comb_col_list))

	# slice를 이용하여 remove가 for loop에 영향을 미치지 않도록 한다.
	for l1 in unique[:] :
		for l2 in unique[:] :
			# 두 개의 집합을 비트 & 연산하여
			# l2가 l1을 포함하고 있는지 확인
			if l1 == l1 & l2 :
				# l2가 l1을 포함하고 있고 l1과 다르다면 l2는 최소성을 만족하지 못한다.
				if l1 != l2 :
					unique.remove(l2)
	answer = len(unique)
	return answer

print(solution(testcases.pop()))
