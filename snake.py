import pygame
from constants import *
from circleshape import CircleShape
import sys

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.move_direction = pygame.Vector2(0, -1)
        self.position = pygame.Vector2(x, y)
        self.speed = PLAYER_SPEED
        self.rotation_cooldown = 0.2
        self.time_since_last_rotation = 0
        self.body = [self.position.copy()]  

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  
        for segment in self.body[1:]:  
            pygame.draw.circle(screen, "green", segment, self.radius)


    def triangle(self):
        forward = self.move_direction * self.radius
        right = pygame.Vector2(-self.move_direction.y, self.move_direction.x) * self.radius / 1.5
        a = self.position + forward
        b = self.position - forward - right
        c = self.position - forward + right
        return [a, b, c]

    def update(self, dt):
        self.time_since_last_rotation += dt

        keys = pygame.key.get_pressed()
        if self.time_since_last_rotation >= self.rotation_cooldown:
            if keys[pygame.K_a]:
                self.rotate(-90)
                self.time_since_last_rotation = 0
            elif keys[pygame.K_d]:
                self.rotate(90)
                self.time_since_last_rotation = 0

        self.move(dt)

    def rotate(self, angle):
        self.rotation = (self.rotation + angle) % 360
        self.update_direction()

    def update_direction(self):
        if self.rotation == 0:
            self.move_direction = pygame.Vector2(0, -1)
        elif self.rotation == 90:
            self.move_direction = pygame.Vector2(1, 0)
        elif self.rotation == 180:
            self.move_direction = pygame.Vector2(0, 1)
        elif self.rotation == 270:
            self.move_direction = pygame.Vector2(-1, 0)

    def move(self, dt):

        self.position += self.move_direction * self.speed * dt


        self.body.insert(0, self.position.copy())

      
        self.body.pop()

    def append_body(self):

        if len(self.body) > 1:
            offset = self.body[-1] - self.body[-2]
        else:
            offset = -self.move_direction * self.radius * 3 

        if offset.length() != 0:
            offset = offset.normalize() * self.radius * 3  

      
        new_segment_position = self.body[-1] - offset
        self.body.append(new_segment_position)

    