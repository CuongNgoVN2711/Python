#CSDojo

from itertools import product

#STEP
allowed_step = [1,2,3,4,5]
max_step = 5
#cach 1
def num_ways(max_step, allowed_step):
	all_ways = []
	a_way = []
	def recursion(position, i, a_way, all_ways):
		if position < max_step:
			for i in allowed_step:
				recursion(position+i, i, a_way + [i], all_ways)
		else:
			if position == max_step:
				all_ways += [a_way]
				print(a_way)
	recursion(0,allowed_step[0],a_way,all_ways)
	print(all_ways)

#cach 2
def num_ways_2(max_step, allowed_step):
	all_ways = []
	a_way = []
	for i in range(1, max_step):
		to_string = ''.join(allowed_step)
		list_product = list(product(to_string, repeat = i))
		for i in list_product:
			to_int = [int(j) for j in i]
			if sum(to_int) == max_step:
				all_ways += [to_int]
	print(all_ways)
#num_ways(max_step,allowed_step)
#num_ways_2(max_step, [str(i) for i in allowed_step])

