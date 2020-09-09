n = int(input())

def has_three(string) :
	for c in string :
		if c == '3' :
			return True
	return False

result = 0
for h in range(n + 1) :
	for m in range(60) :
		for s in range(60) :
			#if has_three(str(s)) or has_three(str(m)) or has_three(str(h)) :
			if '3' in str(s) + str(m) + str(h) :
				result += 1
print(result)
