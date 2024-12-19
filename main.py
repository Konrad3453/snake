import pygame
import sys
from constants import *
from snake import Player
from lives import Life
from score import Score
from fruits import Fruit
from field import *

def draw_grid(screen, color, cell_size):
    """Draws a grid on the screen."""
    for x in range(0, SCREEN_WIDTH, cell_size):
        pygame.draw.line(screen, color, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, cell_size):
        pygame.draw.line(screen, color, (0, y), (SCREEN_WIDTH, y))

def main():
    def over_edge():
        if player.position.x > SCREEN_WIDTH or player.position.y > SCREEN_HEIGHT or player.position.y < 0 or player.position.x < 0:
            print("Game over!")
            sys.exit()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    lives = Life(pygame.font.SysFont('Arial', 30), SCREEN_WIDTH - 350, 10)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    fruits = pygame.sprite.Group()
    score = Score(pygame.font.SysFont('Arial', 30), SCREEN_WIDTH - 150, 10)
    Player.containers = (updatable, drawable)
    Fruit.containers = (fruits, updatable, drawable)
    Field.containers = updatable
    field = Field()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in updatable:
            i.update(dt)
        
        for fruit in fruits:
            if fruit.collision(player):
                score.increase()
                fruit.kill()
                player.append_body()
                player.append_body()
                player.append_body()
                player.append_body()
                player.append_body()
                player.append_body()
        

        screen.fill("black")
      
    
        for i in drawable:
            i.draw(screen)
        score.draw(screen)
        lives.draw(screen)
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        over_edge()

if __name__ == "__main__":
    main()