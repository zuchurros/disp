import pygame
from battvert_func_only import draw_vertical_bar
# from edit import draw_speed_bar
from speedometer_func_only import draw_speed_bar
from settings import WIDTH
from settings import HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("eKart Dashboard")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# Values
speed = 0
battery = 0
max_speed = 120
max_batt = 12.6
charging = True

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate values
    speed += 0.3
    battery += 0.01
    if speed > max_speed:
        speed = 0
    if battery > max_batt:
        battery = 0

    # Draw bars
    draw_speed_bar(screen, speed)
    draw_vertical_bar(screen, WIDTH - 60, 360, 50, 90, battery, max_batt, "")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

