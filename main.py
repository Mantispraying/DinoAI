from sre_constants import JUMP
import pygame
import os
import random
import sys

pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Dino","DinoRun1.png")),pygame.image.load(os.path.join("Assets/Dino","DinoRun2.png"))]

JUMPING = pygame.image.load(os.path.join("Assets/Dino","DinoJump.png"))

BG = pygame.image.load(os.path.join("Assets/Other","Track.png"))

FONT = pygame.font.Font('freesansbold.ttf',20)

def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((255,255,255))

        clock.tick(30)
        pygame.display.update()

if __name__== "__main__":
    main()