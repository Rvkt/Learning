import pygame, random
from enum import Enum
from collections import namedtuple


pygame.init()

font = pygame.font.Font('Varela.ttf', 15)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

# RGB Colors
FOODCLR = (255,5,63)
BGCLR = (223,223,234)
TXTCLR = (10,10,10) 
SNAKECLR0 = (243,144,52) 
SNAKECLR1 = (22,77,89)

''' Colors: 
TXTCLR = (10,10,10) 
SNAKECLR0 = (243,144,52) 
SNAKECLR1 = (22,77,89)
BGCLR = (223,223,234)
FOODCLR = (255,5,63)
'''

BLOCK_SIZE = 20
BLOCK_SIZE1 = 16
SPEED = 10

class SnakeGameAI:

    def __init__(self, w=1000, h=1000):
        self.w = w
        self.h = h
        
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset()

        

    def reset(self):
        # init game state
        self.direction = Direction.RIGHT
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                        Point(self.head.x-BLOCK_SIZE, self.head.y),
                        Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()


    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()


    def play_step(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN



        # 2. Move the snake
        self._move(self.direction)
        self.snake.insert(0, self.head)

        # 3. Check if the game is over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
        
        # 4. Place new food or just move
        if self.head == self.food:
            self.score += 1
            self._place_food()

        else:
            self.snake.pop()

        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. Return game over and score
        # game_over = False
        return game_over, self.score


    def _is_collision(self):
        # hits boundary
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True


        # hits itself
        if self.head in self.snake [1:]:
            return True

        return False


    def _update_ui(self):
        self.display.fill(BGCLR)
        
        for pt in self.snake:
            pygame.draw.rect(self.display, SNAKECLR0, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, SNAKECLR1, pygame.Rect(pt.x+2, pt.y+2, BLOCK_SIZE1, BLOCK_SIZE1))

        pygame.draw.rect(self.display, FOODCLR, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render('Score: ' + str(self.score),True, TXTCLR)
        self.display.blit(text, [10, 10])
        pygame.display.flip()


    def _move(self, direction):

        x = self.head.x
        y = self.head.y

        if direction == Direction.RIGHT:
            x += BLOCK_SIZE

        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE

        elif direction == Direction.DOWN:
            y += BLOCK_SIZE

        elif direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

if __name__ == '__main__':
    game = SnakeGame()

    while True:
        game_over, score = game.play_step()

        if game_over == True:
            break

    print(f'Final Score', score)
    pygame.quit()