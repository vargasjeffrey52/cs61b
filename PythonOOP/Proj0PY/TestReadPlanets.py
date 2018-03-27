"""
 *  Tests Nbody.readPlanets. Reads in ./data/planets.txt and checks output of
 *  readPlanets().
 """
from NBody import NBody
class TestReadPlanets:

	def doubleEquals(self, actual, expected, eps):
		return abs(expected - actual) <= eps * max(expected, actual)
	

	""" Checks to make sure that readPlanets() works perfectly. """
	def checkReadPlanets(self):
		print("Checking readPlanets...")
		#planetsTxtPath = "./data/planets.txt"
		planetsTxtPath = "./data/planets.txt"
		""" If the following line fails to compile, you probably need to make
		 * a certain method static! """
		actualOutput = NBody.readPlanets(planetsTxtPath)

		""" Check the simple things: """
		if (actualOutput == None):
			return "FAIL: readPlanets() None output"
		
		if (len(actualOutput) != 5):
			return "FAIL: readPlanets().length: Expected 5 and you gave " + actualOutput.length
		

		""" Check to make sure every planet exists, plus random spot checks """
		foundEarth = False
		foundMars = False
		foundMercury = False
		foundSun = False
		foundVenus = False
		randomChecksOkay = True
		for p in  actualOutput:
			
			if "earth.gif" == p.imgFileName:
				foundEarth = True
				if not self.doubleEquals(p.xxPos, 1.4960e+11, 0.01):
					print("Advice: Your Earth doesn't have the right xxPos!")
					randomChecksOkay = false
				if not self.doubleEquals(p.yyPos, 0.0000e+00, 0.01):
					print("Advice: Your Earth doesn't have the right yyPos!")
					randomChecksOkay = false

				if not self.doubleEquals(p.xxVel, 0.0000e+00, 0.01):
					print("Advice: Your Earth doesn't have the right xxVel!")
					randomChecksOkay = false
				if not self.doubleEquals(p.yyVel, 2.9800e+04 , 0.01):
					print("Advice: Your Earth doesn't have the right yyVel!")
					randomChecksOkay = False

				
			elif "mars.gif" == p.imgFileName:
				foundMars = True
				if not self.doubleEquals(p.xxPos, 2.2790e+11, 0.01):
					print("Advice: Your Earth doesn't have the right xxPos!")
					randomChecksOkay = false
				if not self.doubleEquals(p.yyPos, 0.0000e+00, 0.01):
					print("Advice: Your Earth doesn't have the right yyPos!")
					randomChecksOkay = false

				if not self.doubleEquals(p.xxVel, 0.0000e+00, 0.01):
					print("Advice: Your Earth doesn't have the right xxVel!")
					randomChecksOkay = false
				if not self.doubleEquals(p.yyVel, 2.4100e+04 , 0.01):
					print("Advice: Your Earth doesn't have the right yyVel!")
				if not self.doubleEquals(p.mass,6.4190e+23 ,0.01):
					randomChecksOkay = False
			elif "mercury.gif" == p.imgFileName:
				foundMercury = True
				if not self.doubleEquals(p.yyPos, 0, 0.01):
					print("Advice: Your Mercury doesn't have the right yyPos!")
					randomChecksOkay = false
				
			elif "sun.gif" == p.imgFileName:
				foundSun = True
			elif "venus.gif" == p.imgFileName:
				foundVenus = True
				if not self.doubleEquals(p.mass, 4.8690e+24, 0.01):
					print("Advice: Your Venus doesn't have the right mass!")
					randomChecksOkay = false
				
			
		

		""" Build up a nice list of missing planets """
		missingPlanets = ""
		if not foundEarth:
			missingPlanets += "Earth, "
		
		if not foundMars:
			missingPlanets += "Mars, "
		
		if not foundMercury:
			missingPlanets += "Mercury, "
		
		if not foundSun:
			missingPlanets += "Sun, "
		
		if not foundVenus:
			missingPlanets += "Venus, "
			
		if len(missingPlanets) > 0:
			answer = "FAIL: readPlanets() Missing these planets: "
			answer += missingPlanets#.substring(0, missingPlanets - 2)
			return answer
		
		if not randomChecksOkay:
			return "FAIL: readPlanets() Not all planets have correct info!"
		
		return "PASS: readPlanets() Congrats! This was the hardest test!"
	

	
testResult = TestReadPlanets().checkReadPlanets()
print(testResult)
	

