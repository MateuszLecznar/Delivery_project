import time
import pygame
pygame.init()



class Hungry_man:

    def __init__(self,x,y):

        self.x = x-25
        self.y = y-25
        self.width = 0
        self.height = 0
        self.image = pygame.image.load('hungry-man-cartoon.png')

    def draw(self):
        window.blit(self.image, (self.x, self.y))



pygame.init()
window = pygame.display.set_mode((800, 600))


def main():
    x = 0
    y = 0

    player = pygame.rect.Rect(x, y, 100, 100)

    run = True
    mans=[]
    while run:
        #pygame.time.Clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                test = Hungry_man(mx,my)
                mans.append(test)
                print(mx, my)

        time.sleep(0.03)

        window.fill((24, 160, 240))
        for el in mans:
            el.draw()
        pygame.display.update()



if __name__=="__main__":
    main()