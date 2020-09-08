
testcase = []
testcase.append(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# 두 번째 코드
# 공간복잡도 활용

def solution(record) :
	users = {}
	users_index = {}
	result = []
	count = 0
	for str in record :
		if str[0] == 'E' or str[0] == 'C' :
			command, uid, nick = str.split(" ")
			if uid not in users.keys() :
				users_index[uid] = []
			users[uid] = nick
			if command == "Enter" :
				users_index[uid].append(count)
				count += 1
				result.append(uid + "님이 들어왔습니다.")
		else :
			command, uid = str.split(" ")
			users_index[uid].append(count)
			result.append(uid + "님이 나갔습니다.")
			count += 1
	for uid in users.keys() :
		for index in users_index[uid] :
			result[index] = result[index].replace(uid, users[uid])
	answer = result
	return answer


'''
# 처음 코드
# 공간복잡도를 활용을 못한 예

def solution(record) :
	users = {}
	result = ""
	for str in record :
		if str[0] == 'E' or str[0] == 'C' :
			command, uid, nick = str.split(" ")
			users[uid] = nick
			if command == "Enter" :
				result += uid + "님이 들어왔습니다.#"
		else :
			command, uid = str.split(" ")
			result += uid + "님이 나갔습니다.#"
	for uid in users.keys() :
		#print(uid, users[uid])
		result = result.replace(uid, users[uid])
	if result[-1] == '#' :
		result = result[:-1]
	#print(result.split("#"))
	answer = result.split("#")
	return answer
'''

print(solution(testcase.pop()))
