class Hw0():
	def __init__(self):
		x = 5
	def MaxWhile(self, arr):
		i = 0
		dummy = arr[0]

		while i < len(arr) :
			if arr[i] > dummy:
				dummy = arr[i]
			i+=1
		return dummy

	def MaxFor(self, arr):
		dummy = arr[0]
		for i in arr:
			if i > dummy:
				dummy = i
		return dummy

	def sum3(self,arr):
		for i in arr:
			for j in arr:
				for k in arr:
					print(i,j,k)
					if i + j + k == 0:
						return True
		return False

a = Hw0()

#print(a.MaxWhile([1,2,8,4,2,5]))
#print(a.MaxFor([1,2,4,2,5]))
print(a.sum3([5, 1, 0, 3, 6]))
