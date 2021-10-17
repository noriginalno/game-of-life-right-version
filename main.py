import pygame
from numpy.random import binomial as rnd
from get_new import get_next_generation
from information_dashboard import InformationWindow


# Гиперпараметры на игру
SIZE = 20
AMOUNT_WIDTH = 30
AMOUNT_HEIGHT = 20
WIDTH = SIZE * AMOUNT_WIDTH
HEIGHT = SIZE * AMOUNT_HEIGHT
FPS = 30
BERNULLI = 0.3

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOUR = [(228, 3, 3), (255, 140, 0), (255, 237, 0), (0, 128, 38), (0, 77, 255), (117, 7, 135)]


fld = [[0 for i in range(AMOUNT_WIDTH)] for j in range(AMOUNT_HEIGHT)]


# Спрайты
class Cell(pygame.sprite.Sprite):
    def __init__(self, colour, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE - 1, SIZE - 1))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        self.image.fill(BLACK if fld[self.rect.y//SIZE][self.rect.x//SIZE]
                        else COLOUR[int(6 * (self.rect.y / HEIGHT))])


# Инициализируем игру
pygame.init()
pygame.mixer.init()
pygame.font.init()
click_sound = pygame.mixer.Sound('klich.ogg')
pygame.mixer.music.load('gachi.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
cells = pygame.sprite.Group()
textbar = pygame.sprite.GroupSingle()
paused = True

# Создаём поле
for i in range(len(fld)):
    for j in range(len(fld[0])):
        cell = Cell(COLOUR[int(6 * (SIZE * i / HEIGHT))], SIZE*j, SIZE*i)
        cells.add(cell)

bar = InformationWindow(screen=screen)
textbar.add(bar)

# Запускаем игровой цикл
running = True
while running:
    pygame.display.set_caption('GAY')
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():

        # Проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

        # Пошаговое воспроизведение стрелочкой
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            paused = True
            get_next_generation(fld)

        # Рестарт на плобел
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            paused = True
            for i in range(len(fld)):
                for j in range(len(fld[0])):
                    fld[i][j] = 0

        # пауза на эскейп
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            paused = not paused

        # Рандомное запонение поля на R
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            paused = True
            for i in range(len(fld)):
                for j in range(len(fld[0])):
                    fld[i][j] = rnd(1, BERNULLI, 1)

        # Клик мыши оживляет или убивает
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            if event.button == 1:
                fld[event.pos[1] // SIZE][event.pos[0] // SIZE] = 1
            elif event.button == 3:
                fld[event.pos[1] // SIZE][event.pos[0] // SIZE] = 0

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            bar.is_drawn = not bar.is_drawn

    # Обновление
    if not paused:
        get_next_generation(fld)

    cells.update()
    textbar.update()

    # Визуализация (сборка)
    screen.fill(BLACK)
    cells.draw(screen)
    screen.blit(bar.image, (0, 0))
    screen.blit(bar.text0, (0, 0))
    screen.blit(bar.text1, (0, 20))
    screen.blit(bar.text2, (0, 40))
    screen.blit(bar.text3, (0, 60))
    screen.blit(bar.text4, (0, 80))
    screen.blit(bar.text5, (0, 100))
    screen.blit(bar.text6, (0, 120))
    pygame.display.flip()


pygame.quit()
