#CSDojo

a_string = 'ABCDD'

def Longest(a_string):
	dic = dict()
	stack = ''
	i = 0
	for i in range(len(a_string)):
		if a_string[i] in stack:
			stack += a_string[i]
			if i == len(a_string) - 1:
				dic[a_string[i]] = len(stack)
		else:
			if stack != '':
				dic[stack[0]] = len(stack)
				stack = a_string[i]
				if i == len(a_string) - 1:
					dic[a_string[i]] = len(stack)
			else:
				stack += a_string[i]
				if i == len(a_string) - 1:
					dic[a_string[i]] = len(stack)
	print(dic)
	return [item for item in dic.items() if item[1] == max(dic.values())]
print(Longest(a_string))

