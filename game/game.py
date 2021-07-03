import pygame
import sys
from .config import *
from .platform import Platform
from .player import Player
from .wall import Wall
from .coin import Coin
import random

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.surface = pygame.display.set_mode((WIDTH,HEIGHT))

        pygame.display.set_caption(TITLE)
        self.font = pygame.font.match_font(FONT)

        self.running = True
        self.playing = True

    def start(self):
        self.new()

    def new(self):
        self.score = 0
        self.generate_elements()
        self.run()

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
        
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self.player.jump()
    
    def draw(self):
        self.surface.fill(LIGHTPURPLE)
        self.sprites.draw(self.surface)
        self.draw_text()

    def update(self):
        if self.playing:

            pygame.display.flip() #es igual que update pero lo hace solo sobre la surface

            wall = self.player.collide_with(self.walls)
            if wall:
                if self.player.collide_bottom(wall):
                    self.player.skid(wall)
                else:
                    self.stop()

            coin = self.player.collide_with(self.coins)
            if coin:
                self.score += 1
                coin.kill()

            self.sprites.update()

            self.player.validate_platform(self.platform)
            self.update_elements(self.walls)
            self.update_elements(self.coins)
            self.generate_walls()

    def update_elements(self,elements):
        for element in elements:
            if not element.rect.right > 0:
                element.kill()

    
    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100,self.platform.rect.top-200)
        self.walls = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.sprites = pygame.sprite.Group()

        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        self.generate_walls()
        self.generate_coins()


    def generate_walls(self):

        last_position = WIDTH + 100

        if not len(self.walls) > 0:
            for w in range(0,MAX_WALLS):
                left = random.randrange(last_position + 200, last_position + 400)
                wall = Wall(left,self.platform.rect.top)
                last_position = wall.rect.right
                self.sprites.add(wall)
                self.walls.add(wall)

    def generate_coins(self):
        last_position = WIDTH + 100

        for c in range(0,MAX_COINS):
            pos_x = random.randrange(last_position + 180, last_position + 300)

            coin = Coin(pos_x,150)

            last_position = coin.rect.right

            self.sprites.add(coin)
            self.coins.add(coin)

    def stop(self):
        self.player.stop()
        self.stop_elements(self.walls)
        self.playing = False
        pass

    def stop_elements(self,elements):
        for element in elements:
            element.stop()

    def score_format(self):
        return 'Score:{} '.format(self.score)

    def draw_text(self):
        self.display_text(str(self.score_format()),36,WHITE,WIDTH//2,30)

    def display_text(self,text,size,color,pos_x,pos_y):
        font = pygame.font.Font(self.font, size)
        text = font.render(text,True,color)
        rect = text.get_rect()
        rect.midtop = (pos_x,pos_y)
        self.surface.blit(text,rect)