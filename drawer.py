import pygame
import pickle
from aprox.newton import approximate
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-P", '--path', type=str)
parser.add_argument('-A', '--approximate', action="store_true")
args = parser.parse_args()
SCALE = 40

pygame.init()
width, heigth = 1000, 1000
ui = pygame.display.set_mode((width, heigth))

def translate(theta, ro):
	return ro * np.cos(theta), ro * np.sin(theta) 

def rawtoapprox(arr):
	f = approximate(arr[0], arr[1])
	x = list(range(360))
	a = [x, [f(i) for i in x] ]
	return a
	

def main():    
	with open(args.path, 'rb') as f:
		arr = pickle.load(f)
	running = True                                                                  
	ui.fill((255,255,255))  

	while running:               
		ui.fill((255,255,255))   
		pygame.draw.line(ui, (0, 0, 0), (0, heigth / 2), (width , heigth / 2))
		pygame.draw.line(ui, (0, 0, 0), (heigth/ 2, width), (heigth / 2, 0))
		if args.approximate:
			data = rawtoapprox(arr)
			arr.pop(0)
		else:
			data = arr.pop(0)

		for theta, ro in zip(data[0], data[1]):
			theta = np.radians(theta)
			x, y = translate(theta, ro)
			pygame.draw.circle(ui, (255, 0, 0), (SCALE * x + width / 2, SCALE * y + heigth / 2), 1)

		for event in pygame.event.get():                                           
			if event.type == pygame.QUIT:                                          
				running = False
		pygame.display.flip()
		pygame.time.delay(100)
		



if __name__ == "__main__":
	main()