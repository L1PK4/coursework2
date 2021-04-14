import pygame
import pickle
import numpy as np

pygame.init()
width, heigth = 500, 500
ui = pygame.display.set_mode( (width, heigth))

def translate(theta, ro):
	return ro * np.cos(theta), ro * np.sin(theta) 

def main():                                                                     
	with open('data/data.pickle', 'rb') as f:
		arr = pickle.load(f)
	n = len(arr)
	#TODO: 	> Rewrite rosbag without enumerate or with pickle
	#		> Draw laserscan with pygame
	#		> make an aproximation
	#print(arr)
	running = True                                                                  
	ui.fill((255,255,255))   
	i = 0                                                      
	font=pygame.font.SysFont("arial",16)                                           
	while running:                                                                  
		ui.fill((255,255,255))   
		for theta, ro in enumerate(arr[i]):
			print(np.radians(theta))
			x, y = translate(np.radians(theta), ro)
			pygame.draw.circle(ui, (255, 0, 0), (20 * x + width / 2, 20 * y + heigth / 2), 2)
		for event in pygame.event.get():                                           
			if event.type == pygame.QUIT:                                          
				running = False
		i += 1
		pygame.display.flip()
		pygame.time.delay(100)
		



if __name__ == "__main__":
	main()