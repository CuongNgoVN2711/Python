
#DECODE from CSDojo video
# mapping = dict(zip([key for key in range(1,27)],[chr(value) for value in range(ord('a'), ord('z') + 1)]))


def Decode(data):
	all_way = []
	a_way = []
	all_message = []
	def Recursion(data, i, all_way, a_way):
		if i < len(data):
			for j in range(1,3):
				if i+j == len(data):
					a_way += [data[i:i+j]]
					all_way += [a_way]
					break
				else:
					Recursion(data, i+j, all_way, a_way + [data[i:i+j]])
		else:
			print(a_way)
			all_way += [a_way]
	Recursion(data,0,all_way,a_way)
	print(all_way)