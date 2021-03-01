import pygame


class Snake():
    def __init__(self, game):
        self.game = game

        self.head = [100, 10]
        self.body = [(100, 10), (90, 10), (80, 10)]
        self.snake_color = pygame.Color('green')

        self.direction = "RIGHT"
        self.new_direction = self.direction

    def move(self):
        # Изменение положения головы змейки
        if self.direction == "RIGHT":
            self.head[0] += 10
        elif self.direction == "LEFT":
            self.head[0] -= 10
        elif self.direction == "UP":
            self.head[1] -= 10
        elif self.direction == "DOWN":
            self.head[1] += 10

        # Проверка координат
        self.check_range()

        # Обновление координат змейки
        self.body.insert(0, tuple(self.head))

        # Обработка попадания на еду
        if tuple(self.head) not in self.game.food.coords:
            self.body.pop()
        else:
            self.game.food.eat(tuple(self.head))

    def check_range(self):
        # Перенос головы змейки при уходе за границу
        if self.head[0] > self.game.width:
            self.head[0] = 0
        if self.head[0] < 0:
            self.head[0] = self.game.width
        if self.head[1] > self.game.height:
            self.head[1] = 0
        if self.head[1] < 0:
            self.head[1] = self.game.height

        # Проверка на столкновение змейки
        if tuple(self.head) in self.body:
            self.game.end()

    def change_direction(self):
        # Проверка, чтобы невозможно было направить в противоположную сторону
        if any((self.new_direction == "RIGHT" and not self.direction == "LEFT",
                self.new_direction == "LEFT" and not self.direction == "RIGHT",
                self.new_direction == "UP" and not self.direction == "DOWN",
                self.new_direction == "DOWN" and not self.direction == "UP")):
            self.direction = self.new_direction

    def render(self):
        self.move()
        for pos in self.body:
            pygame.draw.rect(self.game.surface, pygame.Color('green'),
                             pygame.Rect(pos[0], pos[1], 10, 10))