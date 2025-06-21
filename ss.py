import pygame

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Перемога!")

# Вибір шрифту та розміру
font = pygame.font.Font(None, 60)
text = font.render("Ти переміг!", True, (255, 255, 255))  # Білий колір тексту

# Отримуємо прямокутник тексту для центрування
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Колір фону (чорний)
background_color = (0, 0, 0)

# Головний цикл
running = True
while running:
    screen.fill(background_color)  # Заповнюємо фон
    screen.blit(text, text_rect)  # Малюємо текст
    pygame.display.flip()  # Оновлюємо екран

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()