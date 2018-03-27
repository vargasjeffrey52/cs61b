
from NBody import NBody
"""
 *  Tests Nbody.readRadius. Reads in ./data/planets.txt and checks to see that
 *  result matches hard coded value.
"""
class TestReadRadius:

	"""
	 *  Checks whether or not two Doubles are equal and prints the result.
	 *
	 *  @param  expected    Expected double
	 *  @param  actual      Double received
	 *  @param  label   Label for the 'test' case
	 *  @param  eps     Tolerance for the double comparison.
	"""
	def checkEquals(self, actual,  expected, label,  eps):
		if (abs(expected - actual) <= eps * max(expected, actual)):
			print("PASS: " + label + ": Expected " , expected, " and you gave " , actual)
		else:
			print("FAIL: " + label + ": Expected " , expected, " and you gave " , actual)
			
	"""
	 *  Checks the NBody.readRadius() method.
	"""
	def checkReadRadius(self):
		print("Checking readRadius...")
		planetsTxtPath = "C:/Users/varga_000/Documents/cs61b/skeleton-sp17/proj0/data/planets.txt"
		"""
		/* If the following line fails to compile, you probably need to make
		 * a certain method static!"""
		actualOutput = NBody.readRadius(planetsTxtPath)
		self.checkEquals(actualOutput, 2.50E11, "readRadius()", 0.01)
	

TestReadRadius().checkReadRadius()