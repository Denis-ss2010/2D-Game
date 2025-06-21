import pygame

# Ініціалізація pygame
pygame.init()

# Налаштування екрану
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Персонаж")

# Колір
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Гравітація
GRAVITY = 0.5

# Клас гравця
class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = WIDTH // 2
        self.y = HEIGHT - self.height - 50
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.jump_power = -10
        self.on_ground = False

    def move(self, keys):
        self.velocity_x = 0
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False

    def check_collision(self, platforms):
        for platform in platforms:
            # Перевірка колізій по X
            if (self.x + self.width > platform.x and self.x < platform.x + platform.width and
                self.y + self.height > platform.y and self.y < platform.y + platform.height):
                # Якщо персонаж рухається праворуч і стикається з платформою
                if self.velocity_x > 0:
                    self.x = platform.x - self.width
                # Якщо персонаж рухається ліворуч і стикається з платформою
                elif self.velocity_x < 0:
                    self.x = platform.x + platform.width

    def update(self, platforms):
        # Рух по осі X
        self.x += self.velocity_x
        self.check_collision(platforms)  # Перевірка колізій з платформами

        # Гравітація
        self.velocity_y += GRAVITY
        self.y += self.velocity_y

        # Обмеження нижньою межею
        if self.y + self.height >= HEIGHT:
            self.y = HEIGHT - self.height
            self.velocity_y = 0
            self.on_ground = True

        # Перевірка колізій з платформами
        self.on_ground = False
        for platform in platforms:
            # Перевірка, чи персонаж на платформі
            if (self.x + self.width > platform.x and self.x < platform.x + platform.width and
                self.y + self.height > platform.y and self.y + self.height - self.velocity_y <= platform.y):
                self.y = platform.y - self.height
                self.velocity_y = 0
                self.on_ground = True

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

# Клас платформи
class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# Ініціалізація гравця і платформи
player = Player()
platforms = [Platform(300, 550, 200, 20)]

# Основний цикл гри
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # 60 кадрів в секунду
    screen.fill(WHITE)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.update(platforms)

    # Малюємо об'єкти
    player.draw(screen)
    for platform in platforms:
        platform.draw(screen)

    pygame.display.flip()

pygame.quit()