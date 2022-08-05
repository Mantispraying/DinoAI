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

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self, img=RUNNING[0]):
        self.image = img
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.step_index = 0

    def update(self):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <= -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL
    
    def run(self):
        self.image = RUNNING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1
        
    def draw(self,SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

def main():
    clock = pygame.time.Clock()

    dinosaurs = [Dinosaur()]

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((255,255,255))

        for dinosaur in dinosaurs:
            dinosaur.update()
            dinosaur.draw(SCREEN)

        user_input = pygame.key.get_pressed()

        for i, dinosaur in enumerate(dinosaurs):
            if user_input[pygame.K_SPACE]:
                dinosaur.dino_jump = True
                dinosaur.dino_run = False

        clock.tick(30)
        pygame.display.update()

if __name__== "__main__":
    main()