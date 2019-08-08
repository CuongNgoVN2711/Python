way = []
a_way_1 = ''
n  = m = 7
def excute(n, a_way_1):
	for i in range(1,n):
		a_way = a_way_1
		a_way += str(i)
		if len(a_way) == 4:
			a_way += str(n-i)
		if len(a_way) == 5:
			a_way = ''.join(sorted(a_way))
			a = 0
			for i in a_way:
				a += int(i)
			if a_way not in way and a == m:
				way.append(a_way)
			a_way = a_way[:len(a_way) - 2]
			continue
		excute(n-i, a_way)
excute(n, a_way_1)
print(way)