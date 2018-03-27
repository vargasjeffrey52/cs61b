from Planet import Planet
"""
 *  Tests Planet's update() method
 """
class TestUpdate():

	"""
	 *  Tests update.
	 """
	def __init__(self):
		self.checkUpdate()
	
	"""
	 *  Checks whether or not two Doubles are equal and prints the result.
	 *
	 *  @param  expected    Expected double
	 *  @param  actual      Double received
	 *  @param  label   Label for the 'test' case
	 *  @param  eps     Tolerance for the double comparison.
	 """
	def checkEquals( self,expected,  actual, label,  eps):
		if abs(expected - actual) <= eps * max(expected, actual):
			print("PASS: " + label + ": Expected " , expected , " and you gave " , actual)
		else:
			print("FAIL: " + label + ": Expected " , expected , " and you gave " , actual)
	

	"""
	 *  Checks the class to make sure update works.
	 """
	def checkUpdate(self):
		print("Checking update...")

		p1 = Planet(1.0, 1.0, 3.0, 4.0, 5.0, "jupiter.gif")

		p1.update(2.0, 1.0, -0.5)

		self.checkEquals(7.8, p1.xxPos, "update()", 0.01)
		self.checkEquals(8.6, p1.yyPos, "update()", 0.01)
		self.checkEquals(3.4, p1.xxVel, "update()", 0.01)
		self.checkEquals(3.8, p1.yyVel, "update()", 0.01)
		
TestUpdate()