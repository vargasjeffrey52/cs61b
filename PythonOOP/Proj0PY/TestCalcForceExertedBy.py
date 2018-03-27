
from Planet import Planet
"""
 *  Tests calcForceExertedBy
 """
class TestCalcForceExertedBy():

	"""
	 *  Tests calcForceExertedBy.
	 """
	def __init__(self):
		self.checkCalcForceExertedBy()
	

	"""
	 *  Checks whether or not two Doubles are equal and prints the result.
	 *
	 *  @param  expected    Expected double
	 *  @param  actual      Double received
	 *  @param  label   Label for the 'test' case
	 *  @param  eps     Tolerance for the double comparison.
	 """
	def checkEquals( self, actual,  expected, label,  eps):
		if (abs(expected - actual) <= eps * max(expected, actual)):
			print("PASS: " + label + ": Expected " , expected , " and you gave " , actual)
		else:
			print("FAIL: " + label + ": Expected " , expected , " and you gave " , actual)
		
	


	"""
	 *  Checks the Planet class to make sure calcForceExertedBy works.
	 """
	def checkCalcForceExertedBy(self):
		print("Checking calcForceExertedBy...")

		p1 = Planet(1.0, 1.0, 3.0, 4.0, 5.0, "jupiter.gif")
		p2 = Planet(2.0, 1.0, 3.0, 4.0, 4e11, "jupiter.gif")
		p3 = Planet(4.0, 5.0, 3.0, 4.0, 5.0, "jupiter.gif")
		print(Planet.G)


		self.checkEquals(p1.calcForceExertedBy(p2), 133.4, "calcForceExertedBy()", 0.01)
		self.checkEquals(p1.calcForceExertedBy(p3), 6.67e-11, "calcForceExertedBy()", 0.01)
	

TestCalcForceExertedBy()