import os
import pygame
from math import sin, cos, radians, degrees, copysign
from pygame.math import Vector2
gameIcon = pygame.image.load('car1.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption('Automobili')
class Auto:
    def __init__(self, x, y, angle=0.0, length=4, max_steering=30, max_acceleration=5.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 20
        self.brake_deceleration = 10
        self.free_deceleration = 2
        self.acceleration = 0.0
        self.steering = 0.0
    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt
class Game:
    def __init__(self):
        pygame.init()
        width = 1280
        height = 720
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False
    def igraj(self):
        car_image = pygame.image.load('car.png')
        car = Auto(20,18)
        ppu = 32

        while not self.exit:
            dt = self.clock.get_time() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                if car.velocity.x < 0:
                    car.acceleration = car.brake_deceleration
                else:
                    car.acceleration += 1 * dt
            elif pressed[pygame.K_DOWN]:
                if car.velocity.x > 0:
                    car.acceleration = -car.brake_deceleration
                else:
                    car.acceleration -= 1 * dt
            elif pressed[pygame.K_SPACE]:
                if abs(car.velocity.x) > dt * car.brake_deceleration:
                    car.acceleration = -copysign(car.brake_deceleration, car.velocity.x)
                else:
                    car.acceleration = -car.velocity.x / dt
            else:
                if abs(car.velocity.x) > dt * car.free_deceleration:
                    car.acceleration = -copysign(car.free_deceleration, car.velocity.x)
                else:
                    if dt != 0:
                        car.acceleration = -car.velocity.x / dt
            car.acceleration = max(-car.max_acceleration, min(car.acceleration, car.max_acceleration))

            if pressed[pygame.K_RIGHT]:
                car.steering -= 30 * dt
            elif pressed[pygame.K_LEFT]:
                car.steering += 30 * dt
            else:
                car.steering = 0
            car.steering = max(-car.max_steering, min(car.steering, car.max_steering))
            car.update(dt)
            self.screen.fill((0, 0, 0))
            rotated = pygame.transform.rotate(car_image, car.angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, car.position * ppu -(rect.width / 2, rect.height / 2))
            x = car.position[0]*ppu - rect.width / 2
            y = car.position[1]*ppu - rect.height / 2
            a = car_image.get_width()
            b = car_image.get_height()
            x1 = x + (a*cos(car.angle))
            y1 = y - (b*sin(car.angle))
            x2 = x + (a*sin(car.angle))
            y2 = y + (b*cos(car.angle))
            x3 = x2 + (a*cos(car.angle))
            y3 = y2 - (b*sin(car.angle))
            alfa = pygame.self.screen.get_at((x,y))
            beta = pygame.self.screen.get_at((x1,y1))
            gama = pygame.self.screen.get_at((x2,y2))
            delta = pygame.self.screen.get_at((x3,y3))
            if alfa != pygame.Color('white') or beta != pygame.Color('white') or gama != pygame.Color('white') or delta != pygame.Color('white'):
                car = Car(20,18)
            pygame.display.flip()
            self.clock.tick(self.ticks)
        pygame.quit()
game = Game()
game.igraj()
