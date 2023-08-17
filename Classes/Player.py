import pygame
#клавиши используемые в игре
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# набросок.... пока не работает
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    # Обработчик событий нажатия клавиш
    def handle_key_press(self, key, player):
        if key == K_UP:
            player.move_up()
        elif key == K_DOWN:
            player.move_down()
        elif key == K_LEFT:
            player.move_left()
        elif key == K_RIGHT:
            player.move_right()

    # def __init__(self):
    #     super(Player, self).__init__()
    #     self.surf = pygame.Surface((20, 20))
    #     self.surf.fill((0, 0, 255))
    #     self.rect = self.surf.get_rect()
    #     # Move the sprite based on user keypresses
    # def update(self, pressed_keys):
    #     if pressed_keys[K_UP]:
    #         self.rect.move_ip(0, -5)
    #     if pressed_keys[K_DOWN]:
    #         self.rect.move_ip(0, 5)
    #     if pressed_keys[K_LEFT]:
    #         self.rect.move_ip(-5, 0)
    #     if pressed_keys[K_RIGHT]:
    #         self.rect.move_ip(5, 0)

        # # Keep player on the screen
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > SCREEN_WIDTH:
        #     self.rect.right = SCREEN_WIDTH
        # if self.rect.top <= 0:
        #     self.rect.top = 0
        # if self.rect.bottom >= SCREEN_HEIGHT:
        #     self.rect.bottom = SCREEN_HEIGHT