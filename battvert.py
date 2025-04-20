import pygame

pygame.init()
WIDTH, HEIGHT = 480, 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battery Bar Test")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# Bar config
bar_x, bar_y = 60, 60
bar_width, bar_height = 60, 200
max_value = 12.6  # e.g. full voltage
value = 0

# Color gradient function
def get_bar_color(value, max_value):
    ratio = value / max_value

    if ratio < 0.7:
        r = int(255 * (ratio / 0.7))
        g = 255
        b = 0
    elif ratio < 0.9:
        r = 255
        g = 255
        b = 0
    else:
        r = 255
        g = int(255 * ((1 - ratio) / 0.1))
        b = 0
    return (r, g, b)

# Draw vertical bar
def draw_vertical_bar(screen, x, y, w, h, value, max_value, label):
    fill_ratio = value / max_value
    fill_height = int(h * fill_ratio)
    color = get_bar_color(value, max_value)

    # Background
    pygame.draw.rect(screen, (50, 50, 50), (x, y, w, h), border_radius=8)

    # Filled part (bottom up)
    pygame.draw.rect(screen, color, (x, y + h - fill_height, w, fill_height), border_radius=8)

    # Label & value
    label_text = font.render(f"{label}", True, (255, 255, 255))
    value_text = font.render(f"{value:.2f}V", True, (255, 255, 255))
    screen.blit(label_text, (x, y - 30))
    screen.blit(value_text, (x - 10, y + h + 10))

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate battery charging
    value += 0.01
    if value > max_value:
        value = 0

    draw_vertical_bar(screen, bar_x, bar_y, bar_width, bar_height, value, max_value, "Battery")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
