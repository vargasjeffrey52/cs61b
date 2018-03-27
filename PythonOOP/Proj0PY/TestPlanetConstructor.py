from Planet import Planet
# Tests the Planet constructor.
class TestPlanetConstructor(object):
	"""Tests the Planet constructor to make sure it's working correctly."""
	def __init__(self):
		super(TestPlanetConstructor, self).__init__()
		self.checkPlanetConstructor()

	"""
		*  Checks whether or not two Doubles are equal and prints the result.
		*
		*  @param  expected    Expected double
		*  @param  actual      Double received
		*  @param  label   Label for the 'test' case
	"""

	def checkEquals(self, expected, actual, label):
		if expected == actual:
			print("PASS: " + label + ": Expected " , expected , " and you gave " , actual)
		else:
			print("FAIL: " + label + ": Expected " , expected , " and you gave " , actual)
	
	def checkStringEquals(Self, expected, actual, label):
		if expected == actual :
			print("PASS: " + label + ": Expected " , expected , " and you gave " , actual)
		else:
			print("FAIL: " + label + ": Expected " , expected , " and you gave " , actual)

	"""
		*  Checks Planet constructors to make sure they are setting instance
		*  variables correctly.
	"""
	def checkPlanetConstructor(self):
		print("Checking Planet constructor...");

		xxPos = 1.0
		yyPos = 2.0
		xxVel = 3.0
		yyVel = 4.0
		mass = 5.0

		imgFileName = "jupiter.gif";

		p = Planet(xxPos, yyPos, xxVel, yyVel, mass, imgFileName)
		

		self.checkEquals(xxPos, p.xxPos, "x")
		self.checkEquals(yyPos, p.yyPos, "y")
		self.checkEquals(xxVel ,p.xxVel, "xVelocity")
		self.checkEquals(yyVel, p.yyVel, "yVelocity")
		self.checkEquals(mass, p.mass, "mass")
		self.checkStringEquals(imgFileName, p.imgFileName, "path to image")

		pCopy = Planet().PlanetCopy(p)

		self.checkEquals(p.xxPos, pCopy.xxPos, "x")
		self.checkEquals(p.yyPos, pCopy.yyPos, "y")
		self.checkEquals(p.xxVel, pCopy.xxVel, "xVelocity")
		self.checkEquals(p.yyVel, pCopy.yyVel, "yVelocity")
		self.checkEquals(p.mass, pCopy.mass, "mass")
		self.checkStringEquals(p.imgFileName, pCopy.imgFileName, "path to image")
TestPlanetConstructor()
