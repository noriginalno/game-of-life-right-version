class InformationWindow(pygame.sprite.Sprite):
    def __init__(self, colour=(0, 0, 0), x=0, y=0, size_x=182, size_y=140, screen=None):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.Surface((size_x, size_y))
        self.image.set_alpha(128)
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.font = pygame.font.SysFont("arial", 12)
        self.is_drawn = True
        self.text0 = self.font.render(self.is_drawn * 'i = open/close infomation', True, (255, 255, 255))
        self.text1 = self.font.render(self.is_drawn * 'esc = pause/start', True, (255, 255, 255))
        self.text2 = self.font.render(self.is_drawn * 'space = clear field', True, (255, 255, 255))
        self.text3 = self.font.render(self.is_drawn * 'right = pause + next generation', True, (255, 255, 255))
        self.text4 = self.font.render(self.is_drawn * 'mouse_left = make cell alive', True, (255, 255, 255))
        self.text5 = self.font.render(self.is_drawn * 'mouse_right = to kill cell', True, (255, 255, 255))
        self.text6 = self.font.render(self.is_drawn * 'r = clear field + random fill', True, (255, 255, 255))

    def update(self):
        self.image.set_alpha(self.is_drawn * 128)
        self.text0 = self.font.render(self.is_drawn * 'i = open/close infomation', True, (255, 255, 255))
        self.text1 = self.font.render(self.is_drawn * 'esc = pause/start', True, (255, 255, 255))
        self.text2 = self.font.render(self.is_drawn * 'space = clear field', True, (255, 255, 255))
        self.text3 = self.font.render(self.is_drawn * 'right = pause + next generation', True, (255, 255, 255))
        self.text4 = self.font.render(self.is_drawn * 'mouse_left = make cell alive', True, (255, 255, 255))
        self.text5 = self.font.render(self.is_drawn * 'mouse_right = to kill cell', True, (255, 255, 255))
        self.text6 = self.font.render(self.is_drawn * 'r = clear field + random fill', True, (255, 255, 255))
