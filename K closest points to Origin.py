

#K closest points to the origin
points = [(-2,4), (0,-2), (-1, 0), (3, 5), (-2, -3), (3, 2)]
def K_closest(points, K):
	distances = []
	K_closest_points = []
	def distance(point):
		return (point[0]**2 + point[1]**2)**0.5

	def all_distance(points, distances):
		for i in points:
			distances += [distance(i)]

	all_distance(points, distances)		
	dic = dict(zip(distances,points))
	print(dic)
	for i in range(K):
		K_closest_points += [dic.pop(min(list(dic.keys())))]
	print(K_closest_points)

K_closest(points, 2)