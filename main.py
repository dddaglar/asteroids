import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots,updatable,drawable)
	ast_field = AsteroidField()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		for thing in updatable:
			thing.update(dt)
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.collision(shot):
					asteroid.split()
					shot.kill()
		

		pygame.display.flip()
		dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()
