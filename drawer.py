import pygame
import pickle
from aprox.newton import approximate
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-P", '--path', type=str)
parser.add_argument('-A', '--approximate', action="store_true")
args = parser.parse_args()

pygame.init()
width, heigth = 500, 500
ui = pygame.display.set_mode( (width, heigth))

def translate(theta, ro):
	return ro * np.cos(theta), ro * np.sin(theta) 

def main():    
	if (not args.approximate):                                                          
		with open(args.path, 'rb') as f:
			arr = pickle.load(f)
	else:
		with open(args.path, 'rb') as f:
			a = pickle.load(f)

	#TODO: 	
	#		> make an aproximation
	running = True                                                                  
	ui.fill((255,255,255))   
	i = 0                                                      
	font=pygame.font.SysFont("arial",16)                                           
	while running:                                                                  
		ui.fill((255,255,255))   
		pygame.draw.line(ui, (0, 0, 0), (0, heigth / 2), (width , heigth / 2))
		pygame.draw.line(ui, (0, 0, 0), (heigth/ 2, width), (heigth / 2, 0))
		if args.approximate:
			f = approximate(a[i][0], a[i][1])
			arr = (np.arange(0, 360, 1), [f(i) for i in np.arange(0, 360, 1)])
		for theta, ro in zip(arr[0], arr[1]):
			x, y = translate(theta, ro)
			print(type(x), type(y))
			pygame.draw.circle(ui, (255, 0, 0), (20 * x + width / 2, 20 * y + heigth / 2), 1)
		for event in pygame.event.get():                                           
			if event.type == pygame.QUIT:                                          
				running = False
		#i += 1
		n = len(arr)
		if i >= n:
			running = False
		pygame.display.flip()
		pygame.time.delay(100)
		



if __name__ == "__main__":
	main()