"""
 *  Tests calcDistance
 """

from Planet import Planet

class TestCalcDistance():

	"""
	 *  Tests calcDistance.
	"""
	def __init__(self):
		self.checkCalcDistance()

	"""
	 *  Checks whether or not two Doubles are equal and prints the result.
	 *
	 *  @param  expected    Expected double
	 *  @param  actual      Double received
	 *  @param  label   Label for the 'test' case
	 *  @param  eps     Tolerance for the double comparison.
	 """
	def checkEquals(self, actual, expected, label, eps):
		if abs(expected - actual) <= eps * max(expected, actual):
			print("PASS: " + label + ": Expected " , expected , " and you gave " , actual)
		else:
			print("FAIL: " + label + ": Expected " , expected , " and you gave " , actual)
		

	"""
	 *  Checks the Planet class to make sure calcDistance works.
	"""
	def checkCalcDistance(self):
		print("Checking calcDistance...")

		p1 = Planet(1.0, 1.0, 3.0, 4.0, 5.0, "jupiter.gif")
		p2 = Planet(2.0, 1.0, 3.0, 4.0, 5.0, "jupiter.gif")
		p3 = Planet(4.0, 5.0, 3.0, 4.0, 5.0, "jupiter.gif")

		self.checkEquals(p1.calcDistance(p2), 1.0, "calcDistance()", 0.01)
		self.checkEquals(p1.calcDistance(p3), 5.0, "calcDistance()", 0.01)
TestCalcDistance()