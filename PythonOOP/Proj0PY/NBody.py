
import numpy as np
from Planet import Planet 
import sys
#from PyQt5 import  QtGui, QtWidgets, QtCore, QtHelp
import pygame
from pygame.locals import *

import time



class NBody(object):
	""" docstring for NBody
	* Datapath = "C:/Users/varga_000/Documents/cs61b/skeleton-sp17/proj0/data/"
	* starfield = "starfield.jpg"
	* AudioPath = "C:/Users/varga_000/Documents/cs61b/skeleton-sp17/proj0/audio/"
	* ExamplePaht = "C:/Users/varga_000/Documents/cs61b/skeleton-sp17/proj0/examples/"
	* imagesPath = "C:/Users/varga_000/Documents/cs61b/skeleton-sp17/proj0/images/"
	"""
	

	def readRadius(fname):
		data = open( fname)
		numPlanets = int(data.readline())
		radius = float(data.readline())
		return radius

	def readPlanets(fname):
		data = open( fname)
		numPlanets = int(data.readline())
		radius = float(data.readline())
		planetsList = [Planet(*data.readline().split()) for planet in range(numPlanets)]
		return planetsList

	def XScale2pix(width, x, Xmin, Xmax):
		return  width * ((x - Xmin)/ (Xmax - Xmin))

	def YScale2pix(height, y, Ymin, Ymax):
		return  height * ((Ymax - y)/ (Ymax - Ymin))

	def __main__():
		try:
			""" 
				* Command line requires Time(ms), dt(ms) and fname
				* EX)>>>python NBody.py Time dt data/planets.txt' 
			"""
			T, dt, fname = sys.argv[1:]
			#print(T, dt)
			T, dt = float(T), float(dt)
			imagesPath = "./images/"

			width, height = 800, 800

			
			def Window():
				radius = int(NBody.readRadius('./data/' + fname))
			
				#print(radius)
				planets = NBody.readPlanets('./data/' + fname)
				screen = pygame.display.set_mode((width, height))
				bkgImg = pygame.image.load(imagesPath + 'starfield.jpg')
				bkgImg = pygame.transform.scale(bkgImg,(width, height))

				
				time  = 0
				while time < T:
					xForces = []
					yForces = []
					screen.blit(bkgImg,(0,0))
					for plnt in planets:
						pi = pygame.image.load(imagesPath + plnt.imgFileName)
					
						x,y = NBody.XScale2pix(width, plnt.xxPos, -radius, radius) , NBody.YScale2pix( height, plnt.yyPos, -radius, radius)						
						
						screen.blit(pi,(x,y))

					for plnt in planets:
						xForces += [plnt.calcNetForceExertedByX(planets)]
						yForces += [plnt.calcNetForceExertedByY(planets)]
					for i in range(len(planets)):
						#print("{:.4E}".format(planets[i].xxPos), "{:.4E}".format(planets[i].yyPos), "{:.4E}".format(planets[i].xxVel), "{:.4E}".format(planets[i].yyVel), "{:.4E}".format(planets[i].mass), planets[i].imgFileName)
						planets[i].update(dt, xForces[i], yForces[i])
					#print()


					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							sys.exit()
					time += dt
					pygame.display.update()
				#print(len(planets))
				#print(radius)
				for i in range(len(planets)):
					print("{:.4E}".format(planets[i].xxPos), "{:.4E}".format(planets[i].yyPos), "{:.4E}".format(planets[i].xxVel), "{:.4E}".format(planets[i].yyVel), "{:.4E}".format(planets[i].mass), planets[i].imgFileName)
				sys.exit()


			Window()








		except ValueError as err:
			print('ValueError: system args missing ','(ie. T , dt, fileName)')
			print('if running from command line use the following syntax: ')
			print('>>>python NBody.py 157788000.0 25000.0 data/planets.txt')
			pass





NBody.__main__()

