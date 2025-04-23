import pygame
from settings import WIDTH
from settings import HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Bar config
# max_value = 12.6
# value = 0


# Color gradient function
def get_bar_color(value, max_value):
    ratio = value / max_value

    if ratio < 0.3:
        # Green to Yellow
        r = 255
        g = 0
        b = 0
    elif ratio < 0.7:
        # Yellow
        r = 255
        g = 255
        b = 0
    else:
        # Yellow to red
        r = 0
        g = 255
        b = 0
    return (r, g, b)


# Draw vertical bar
def draw_vertical_bar(screen, x, y, w, h, value, max_value, label):
    fill_ratio = value / max_value
    fill_height = int(h * fill_ratio)
    color = get_bar_color(value, max_value)
    percent = fill_ratio * 100

    # Background
    pygame.draw.rect(screen, (50, 50, 50), (x, y, w, h), border_radius=8)

    # Filled part (bottom up)
    pygame.draw.rect(screen, color, (x, y + h - fill_height, w, fill_height), border_radius=8)

    # Label & value , value and percent changeable
    label_text = font.render(f"{label}", True, (255, 255, 255))
    #value_text = font.render(f"{value:.2f}V", True, (255, 255, 255))
    percent_text = font.render(f"{percent:.1f}%", True, (255, 255, 255))
    screen.blit(label_text, (x, y - 30))
    #screen.blit(value_text, (x - 10, y + h + 10))
    screen.blit(percent_text, (x - 2, y + h + 10))

