from Planet import Planet

"""
 *  Tests calcPairwiseForce
"""
class TestCalcForceExertedByXY():

	"""
	 *  Tests calcForceExertedByXY.
	"""
	def __init__(self):
		self.checkCalcForceExertedByXY()


	""" Checks whether two doubles are approximately equal. 
	 *  @param  expected    Expected double
	 *  @param  actual      Double received
	 *  @param  eps         Tolerance for the comparison.
	"""
	def approxEqual(self, actual, expected, eps):
		return abs(expected - actual) <= eps * max(expected, actual)

	"""
	 *  Checks whether or not two Doubles are equal and prints the result.
	 *
	 *  @param  expected    Expected double
	 *  @param  actual      Double received
	 *  @param  label       Label for the 'test' case
	 *  @param  eps         Tolerance for the comparison.
	"""
	def checkEquals(self, actual, expected, label, eps):
		if (self.approxEqual(actual, expected, eps)):
			print("PASS: " + label + ": Expected " , expected, " and you gave ", actual)
		else:
			print("FAIL: " + label + ": Expected " , expected, " and you gave ", actual)
			if (self.approxEqual(actual, expected, eps)):
				print("      Hint: Your answer is exactly opposite of the correct answer.")

	"""
	 *  Checks the Planet class to make sure calcForceExertedByXY works.
	"""
	def checkCalcForceExertedByXY(self):
		print("Checking calcForceExertedByX and calcForceExertedByY...")

		p1 = Planet(1.0, 1.0, 3.0, 4.0, 5.0, "jupiter.gif")
		p2 = Planet(2.0, 1.0, 3.0, 4.0, 4e11, "jupiter.gif")
		p3 = Planet(4.0, 5.0, 3.0, 4.0, 5.0, "jupiter.gif")

		self.checkEquals(p1.calcForceExertedByX(p2), 133.4, "calcForceExertedByX()", 0.01)
		self.checkEquals(p1.calcForceExertedByX(p3), 4.002e-11, "calcForceExertedByX()", 0.01)
		self.checkEquals(p1.calcForceExertedByY(p2), 0.0, "calcForceExertedByY()", 0.01)
		self.checkEquals(p1.calcForceExertedByY(p3), 5.336e-11, "calcForceExertedByY()", 0.01)

TestCalcForceExertedByXY()