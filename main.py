import pygame, sys
from setup.settings import *
from mechanics.level import Level

class Game:
    def __init__(self):
        # configuração geral[
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()

        self.level = Level()
        main_sound = pygame.mixer.Sound(fr'C:\Users\mathe\Documents\Projetos\Python projects\zelda\lvl_graphics\audio\main.ogg')
        main_sound.play(loops= -1)
        main_sound.set_volume(0.1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            #debug("hello :)")

            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()

    game.run()
