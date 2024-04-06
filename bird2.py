import pygame as pg


class Bird(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((30, 30))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 2
        self.jump_time = None

    def jump(self):
        self.vector = -5
        self.jump_time = pg.time.get_ticks()

    def update(self):
        self.rect.y += self.vector
        ##

