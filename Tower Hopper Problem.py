towers = [1, 0]

def IsHopperTower(towers):
	all_way = []
	a_way = []
	def FindAWay(towers, i, a_way, all_way):
		if i < len(towers):
			for j in range(1, towers[i] + 1):
				FindAWay(towers, i + j, a_way + [i], all_way)
		else:
			all_way += [a_way + [i]]
	FindAWay(towers, 0, a_way, all_way)
	print(all_way)
	if len(all_way) == 0:
		return False
	else:
		return True
	
print(IsHopperTower(towers))