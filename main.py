import pygame
import pygame.locals
import pygame.math

class Game:
    def __init__(self, name = "My Game", screensize = (800, 600)):
        print("Loading Game: " + name)
        pygame.init()
        Game.game = self
        self.sprites = pygame.sprite.Group()
        self.screensize = screensize
        displayoptions = (pygame.HWSURFACE | pygame.SCALED)
        self.display = pygame.display.set_mode(screensize, displayoptions)
        self.clock = pygame.time.Clock()
        self.eventlist = []
        self.background_colour = (16, 64, 16)
        self.exit = False
        pygame.display.set_caption(name)
    def update(self, deltaTime):
        for event in self.eventlist:
            self.processEvent(event)
        self.sprites.update()
    def processEvent(self, event):
        if event.type == pygame.QUIT:
            self.exit = True
            
    def draw(self):
        self.display.fill(self.background_colour)
        self.sprites.draw(self.display)
    def run(self):
        while not self.exit:
            deltaTime = self.clock.tick(60)
            self.eventlist = pygame.event.get()
            self.update(deltaTime)
            self.draw()
            pygame.display.update()
        pygame.quit()
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 80])
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.paddleup = False
        self.paddledown = False
    def update(self):
        super().update()
        if self.paddleup == True:
            if self.rect.y < 50:
                return
            self.rect.y -= 5
        if self.paddledown == True:
            if self.rect.y > 475:
                return
            self.rect.y += 5
class PongGame(Game):
    def __init__(self):
        super().__init__(name = "Pong")
        #self.player1 = pygame.sprite.Sprite()
        #self.player1.image = pygame.Surface([15, 80])
        #self.player1.image.fill((255, 255, 255))
        self.player1 = Paddle(45, 300)
        self.player2 = Paddle(750, 300)
        self.ball = Ball(385,300)
        self.sprites.add(self.player1)
        self.sprites.add(self.player2)
        self.sprites.add(self.ball)
   

    def processEvent(self, event):
        super().processEvent(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.locals.K_w:
                print("W pressed")
                self.player1.paddleup = True
            if event.key == pygame.locals.K_s:
                print("S pressed")
                self.player1.paddledown = True
            if event.key == pygame.locals.K_UP:
                print("Arrow UP pressed")
                self.player2.paddleup = True
            if event.key == pygame.locals.K_DOWN:
                print("Arrow DOWN pressed")
                self.player2.paddledown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.locals.K_w:
                print("W released")
                self.player1.paddleup = False
            if event.key == pygame.locals.K_s:
                print("S released")
                self.player1.paddledown = False
            if event.key == pygame.locals.K_UP:
                print("Arrow UP released")
                self.player2.paddleup = False
            if event.key == pygame.locals.K_DOWN:
                print("Arrow DOWN released")
                self.player2.paddledown = False
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.velocity = pygame.math.Vector2 (6, 3)
        self.image = pygame.image.load("voltorb.png")
        self.image = pygame.transform.scale(self.image, [45, 45])
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    def update(self):
        (vx, vy) = self.velocity
        player1_pos = Game.game.player1.rect.center
        player2_pos = Game.game.player2.rect.center
        if self.rect.x > 750 or self.rect.x < 5:
            vx = -1 * vx
        if self.rect.y > 550 or self.rect.y < 5:
            vy = -1 * vy
        if self.rect.colliderect(Game.game.player1.rect):
            vx = -1 * vx
        if self.rect.colliderect(Game.game.player2.rect):
            vx = -1 * vx
        self.velocity = pygame.math.Vector2(vx, vy)
        self.rect.x += vx
        self.rect.y += vy

PongGame().run()

