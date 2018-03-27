

from decimal import Decimal
from decimal import ROUND_HALF_UP
#from decimal import  decimal
from Planet import Planet
"""
 *  Tests setNetForce
"""
class TestCalcNetForceExertedByXY():

	"""
	 *  Tests setNetForce.
	"""
	def __init__(self):
		self.calcNetForceExertedByXY()
	
	"""
	 *  Checks whether or not two Doubles are equal and prints the result.
	 *
	 *  @param  expected    Expected double
	 *  @param  actual      Double received
	 *  @param  label   Label for the 'test' case
	"""
	def checkEquals(self, expected, actual,  label):
		if (expected == actual):
			print("PASS: " + label + ": Expected "  , expected, " and you gave " , actual)
		else:
			print("FAIL: " + label + ": Expected "  , expected, " and you gave " , actual)
	
	"""
	 *  Rounds a double value to a number of decimal places.
	 *
	 *  @param  value   Double to be rounded.
	 *  @param  places  Integer number of places to round VALUE to.
	"""
	def round(self, value, places):
		

		bd = Decimal(value)
		bd = bd.quantize(Decimal(places),rounding=ROUND_HALF_UP)
		return float(bd)


	"""
	 *  Checks the Planet class to make sure setNetForce works.
	"""
	def calcNetForceExertedByXY(self):
		print("Checking setNetForce...")

		p1 = Planet(1.0, 1.0, 3.0, 4.0, 5.0, "jupiter.gif")
		p2 = Planet(2.0, 1.0, 3.0, 4.0, 4e11, "jupiter.gif")
		
		p3 = Planet(4.0, 5.0, 3.0, 4.0, 5.0, "jupiter.gif")
		p4 = Planet(3.0, 2.0, 3.0, 4.0, 5.0, "jupiter.gif")

		planets = [p2, p3, p4]

		xNetForce = p1.calcNetForceExertedByX(planets)
		yNetForce = p1.calcNetForceExertedByY(planets)
		print(xNetForce, yNetForce)

		self.checkEquals(133.4, self.round(xNetForce, '.01'), "calcNetForceExertedByX()")
		self.checkEquals(0.0, self.round(yNetForce, '.01'), "calcNetForceExertedByY()")
	
		print("Running test again, but with array that contains the target planet.")

		planets = [p1, p2, p3, p4]

		xNetForce = p1.calcNetForceExertedByX(planets)
		yNetForce = p1.calcNetForceExertedByY(planets)

		self.checkEquals(133.4, self.round(xNetForce, '.01'), "calcNetForceExertedByX()")
		self.checkEquals(0.0, self.round(yNetForce, '.01'), "calcNetForceExertedByY()")

TestCalcNetForceExertedByXY()