import pygame


pygame.init()
ui = pygame.display.set_mode( (1000, 1000))


def main():                                                                     
	f = open("data.txt", "rt")
	s = f.readline()
	s = s.split("][")
	arr = []
	n = 0
	for i in s:
		while(len(i)):
			pass
	#TODO: 	> Rewrite rosbag without enumerate or with pickle
	#		> Draw laserscan with pygame
	#		> make an aproximation

	running = True                                                                  
	ui.fill((255,255,255))                                                         
	font=pygame.font.SysFont("arial",16)                                           


	while running:                                                                  
		pygame.draw.circle(ui, (0, 0, 0), )
		for event in pygame.event.get():                                           
			if event.type == pygame.QUIT:                                          
				running = False
		



if __name__ == "__main__":
	main()