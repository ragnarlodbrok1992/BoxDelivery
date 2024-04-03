from src.graph.shaders.ui_shaders import VERTEX_SHADER, FRAGMENT_SHADER

import pygame


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class Engine:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            # Inputs - events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # Rendering
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    print("Box delivery - tech demo.")
    engine = Engine()
    engine.run()
