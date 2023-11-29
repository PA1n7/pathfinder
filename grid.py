import pygame

class grid:
    def __init__(self, size=(25, 25), spacing = 5):
        self.size = size
        self.spacing = spacing
        self.savedScreen = pygame.Surface((0, 0))
        self.colorList = [[(12, 0, 25) for _ in range(self.size[0])] for __ in range(self.size[1])]
        self.rects = [["" for _ in range(self.size[0])] for __ in range(self.size[1])]
    def calcSL(self, screen):
        _tempsize = screen.get_size()
        _tempsize = [_tempsize[0]-self.spacing*(1+self.size[0]), _tempsize[1]-self.spacing*(1+self.size[1])]
        _index = 0 if self.size[0] > self.size[1] else 1
        if _tempsize[_index] > _tempsize[0 if _index else 1]:
            _index = 0 if _index else 1
        self.sideLength = _tempsize[_index]/max(self.size)
    def reset(self):
        self.colorList = [[(12, 0, 25) for _ in range(self.size[0])] for __ in range(self.size[1])]
        self.savedScreen = pygame.Surface((0, 0))
    def changeColor(self, point, color=(125, 25, 150)):
        # Enter point as (x, y)
        self.colorList[point[1]][point[0]] = color
        if min(self.savedScreen.get_size()) != 0:
            pygame.draw.rect(self.savedScreen, color, pygame.Rect(self.spacing*(point[0]+1)+self.sideLength*(point[0]), self.spacing*(point[1]+1)+self.sideLength*(point[1]), self.sideLength, self.sideLength))
    def get_collide(self, point):
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                if self.rects[y][x].collidepoint(point[0], point[1]):
                    return [x, y]
        return False
    def draw(self, screen:pygame.Surface):
        if screen.get_size() == self.savedScreen.get_size():
            screen.blit(self.savedScreen, (0, 0))
            return
        else:
            self.savedScreen = pygame.Surface(screen.get_size())
            self.savedScreen.fill((255, 255, 255))
        self.calcSL(screen)
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                self.rects[y][x] = pygame.Rect(self.spacing*(x+1)+self.sideLength*(x), self.spacing*(y+1)+self.sideLength*(y), self.sideLength, self.sideLength)
                pygame.draw.rect(self.savedScreen, self.colorList[y][x], self.rects[y][x])
        screen.blit(self.savedScreen, (0, 0))
