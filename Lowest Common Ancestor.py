#CSDojo

#Binary Tree
class Tree():
	"""docstring for ClassName"""
	def __init__(self, data = 0):
		self.data = data
		self.right = None
		self.left = None

	def InsertNodeAuto(self, data):
		if self.data is None:
			self.data = data
		else:
			if self.data <= data:
				if self.right is None:
					self.right = Tree(data)
				else:
					self.right.InsertNodeAuto(data)
			else:
				if self.left is None:
					self.left = Tree(data)
				else:
					self.left.InsertNodeAuto(data)

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data)
		if self.right:
			self.right.PrintTree()

	def Recursion(self, a, b):
		if self.data == a and self.data == b:
			return self.data

		if self.right is None:
			r = False
		else:
			r = self.right.Recursion(a, b)

		if self.left is None:
			l = False
		else:
			l = self.left.Recursion(a ,b)

		if self.data == a or self.data == b:
			if l == True or r == True:
				return self.data
			else:
				return True

		if l == True and r == True:
			return self.data

		if l == True or r == True:
			return True
			
		if l == False and r == False:
			return False
		
		if type(l) is int:
			return l
		if type(r) is int:
			return r

root = Tree(12)
root.InsertNodeAuto(6)
root.InsertNodeAuto(14)
root.InsertNodeAuto(3)
root.InsertNodeAuto(8)
root.InsertNodeAuto(7)
root.InsertNodeAuto(13)
root.InsertNodeAuto(17)
root.InsertNodeAuto(15)
root.InsertNodeAuto(18)
#root.PrintTree()
print("LCD: {}".format(root.Recursion(3,8)))