"""The Planet class creates planets with physical properties"""
import copy
import numpy as np


class Planet(object):
    G = 6.67e-11  # gravitiatonal Constant (N-m^2/Kg^2)

    """docstring for Planet"""

    def __init__(self, xxPos=0, yyPos=0, xxVel=0, yyVel=0, mass=0, imgFileName=None):
        super(Planet, self).__init__()
        # current x and y position
        self.xxPos = float(xxPos)
        self.yyPos = float(yyPos)
        # current x and y velocity
        self.xxVel = float(xxVel)
        self.yyVel = float(yyVel)
        # mass of planet
        self.mass = float(mass)
        # The name of an image in the images Directory that depicts the planet
        self.imgFileName = str(imgFileName)

    def PlanetCopy(self, p):
        """ Creates a copy of the planet """
        return copy.deepcopy(p)

    def xxDiff(self, p):
        """ return the difference in xxPoss wrt itself """
        return p.xxPos - self.xxPos

    def yyDiff(self, p):
        """ return the difference in yyPoss wrt itself """
        return p.yyPos - self.yyPos

    def calcDistance(self, planetB):
        """ returns the distance to another planet with respect to it's self"""
        return np.sqrt((self.xxDiff(planetB))**2 + (self.yyDiff(planetB))**2)

    def calcForceExertedBy(self, planetB):
        """ Returns the relative gravitational force between planetB and itself  """
        return (self.G * (self.mass * planetB.mass)) / ((self.calcDistance(planetB))**2)

    def calcForceExertedByX(self, planetB):
        """ Returns the x-component of the relative gravitational force between planetB and itself  """
        return self.calcForceExertedBy(planetB) * (self.xxDiff(planetB) / self.calcDistance(planetB))

    def calcForceExertedByY(self, planetB):
        """ Returns the y-component of the relative gravitational force between planetB and itself  """
        return (self.calcForceExertedBy(planetB) * (self.yyDiff(planetB) / self.calcDistance(planetB)))

    def calcNetForceExertedByX(self, planetArr):
        """ Returns the x-component of the net force exterted by all planets  """
        return sum([self.calcForceExertedByX(planet)for planet in planetArr if planet is not self])

    def calcNetForceExertedByY(self, planetArr):
        """ Returns the y-component of the net force exterted by all planets """
        return sum([self.calcForceExertedByY(planet) for planet in planetArr if planet is not self])

    def update(self, dt, Fx, Fy):
        """ Given a Force (Fx, Fy) 'update',
            Updates the x and y position and the Vx ,Vy velocity of a planet
        """
        ax = Fx / self.mass
        ay = Fy / self.mass

        self.xxVel = self.xxVel + ax * dt
        self.yyVel = self.yyVel + ay * dt

        self.xxPos = self.xxPos + dt * self.xxVel
        self.yyPos = self.yyPos + dt * self.yyVel


samh = Planet(1, 0, mass=10)
rocinate = Planet(5, -3, mass=50)
AEgir = Planet(3, 3, mass=5)
