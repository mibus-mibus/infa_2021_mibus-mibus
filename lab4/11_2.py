import pygame
from pygame.draw import *

FPS = 30
screen = pygame.display.set_mode((800, 1000))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220, 220, 220)
DARK_GRAY = (170, 180, 170)
LIGHT_BROWN = (190, 140, 75)
BROWN = (172, 120, 69)
DARK_BROWN = (101, 67, 33)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


def draw_environment():
    """
    Draw ground and sky
    """
    rect(screen, LIGHT_GRAY, (0, 0, 800, 450))  # grey sky
    rect(screen, WHITE, (0, 450, 800, 1000))  # white ground


def draw_iglu(s, posX, posY, scale=600):
    """
    Draw iglu
    """
    surface_resolution = 600
    x, y = surface_resolution//2, surface_resolution//2
    surface = pygame.Surface((surface_resolution, surface_resolution), pygame.SRCALPHA, 32).convert_alpha()
    # Fill iglu:
    polygon(surface, LIGHT_GRAY,
            [[x-300, y+70], [x-283, y+5], [x-262, y-45],
             [x-200, y-90], [x-150, y-100], [x-100, y-90],
             [x-38, y-45], [x-17, y+5], [x, y+70], [x-150, y+80]])
    # iglu's border:
    arc(surface, BLACK, (x-300, y-100, 300, 350), 0, 3.14, 4)

    draw_bricks_iglu(surface, x, y)

    surface_scale = pygame.transform.scale(surface, (scale, scale))
    return s.blit(surface_scale, (posX, posY))


def horizontal_arcs_iglu(s, x, y):
    """Draw horisontal iglu's arcs"""
    arc(s, BLACK, (x-350, y+55, 350, 20), 3.14, 0)
    arc(s, BLACK, (x-290, y+10, 280, 20), 3.14, 0)
    arc(s, BLACK, (x-270, y-40, 240, 20), 3.14, 0)
    arc(s, BLACK, (x-230, y-80, 160, 20), 3.14, 0)


def vertival_lines_iglu(s, x, y):
    """Draw vertical iglu's lines"""
    # top first line
    line(s, BLACK, (x-170, y-100), (x-180, y-60))
    line(s, BLACK, (x-130, y-100), (x-120, y-60))
    # second line
    line(s, BLACK, (x-200, y-62), (x-210, y-20))
    line(s, BLACK, (x-150, y-62), (x-150, y-20))
    line(s, BLACK, (x-100, y-62), (x-90, y-20))
    # third line
    line(s, BLACK, (x-235, y-23), (x-255, y+25))
    line(s, BLACK, (x-180, y-20), (x-185, y+28))
    line(s, BLACK, (x-115, y-20), (x-110, y+28))
    line(s, BLACK, (x-65, y-20), (x-50, y+28))
    # forth line
    line(s, BLACK, (x-280, y+25), (x-290, y+70))
    line(s, BLACK, (x-225, y+30), (x-235, y+80))
    line(s, BLACK, (x-150, y+30), (x-150, y+80))
    line(s, BLACK, (x-80, y+30), (x-80, y+80))
    line(s, BLACK, (x-20, y+25), (x-10, y+70))


def draw_bricks_iglu(s, x, y):
    """Draw ilu's bricks"""
    horizontal_arcs_iglu(s, x, y)
    vertival_lines_iglu(s, x, y)


def draw_chukcha(s, posX, posY, scale=600):
    """Draw chukcha"""
    surface_resolution = 600
    x, y = surface_resolution//2, surface_resolution//2
    surface = pygame.Surface((surface_resolution, surface_resolution), pygame.SRCALPHA, 32).convert_alpha()
    draw_chukcha_hand(surface, (x-70, y-110, 100, 30))
    draw_chukcha_hand(surface, (x+110, y-110, 100, 30))
    draw_chukcha_leg(surface, x, y, "left")
    draw_chukcha_leg(surface, x, y, "right")
    draw_chukcha_body(surface, x, y)
    draw_chukcha_head(surface, x, y)
    draw_spear(surface, x, y)
    surface_scale = pygame.transform.scale(surface, (scale, scale))
    return s.blit(surface_scale, (posX, posY))

def draw_chukcha_head(s, x, y):
    """ Draw head's chukcha"""
    draw_chukcha_hood(s, x, y)
    draw_chukcha_face(s, x, y)


def draw_chukcha_face(s, x, y):
    """Draw face's chukcha"""
    # Face:
    ellipse(s, LIGHT_GRAY, (x+30, y-200, 80, 60))
    # Left eye:
    line(s, BLACK, (x+43, y-180), (x+57, y-175))
    # Right eye:
    line(s, BLACK, (x+80, y-175), (x+94, y-180))
    # Mouse:
    lines(s, BLACK, False, [[x+50, y-155], [x+58, y-160], [x+82, y-160], [x+90, y-155]])


def draw_chukcha_hood(s, x, y):
    """Draw hood's chukcha"""
    # Foor:
    ellipse(s, LIGHT_GRAY, (x+10, y-220, 120, 100))
    # Hood:
    ellipse(s, LIGHT_BROWN, (x+20, y-210, 100, 80))


def draw_chukcha_body(s, x, y):
    polygon(s, BROWN, [[x, y], [x+10, y-70], [x+30, y-150], [x+110, y-150], [x+130, y-70], [x+140, y]])
    # Horizontal fur line on the chukcha's coat:
    rect(s, DARK_BROWN, (x, y-10, 140, 10))
    # Vertical fur line on the chukcha's coat:
    rect(s, DARK_BROWN, (x+60, y-150, 20, 150))


def draw_chukcha_hand(s, position):
    """Draw hand"""
    ellipse(s, BROWN, position)


def draw_chukcha_leg(s, x, y, left_right):
    """Draw leg"""
    # Draw left leg:
    if left_right == "left":
        # Draw leg
        ellipse(s, BROWN, (x+25, y-30, 40, 100))
        # Draw foot
        ellipse(s, BROWN, (x, y+42, 60, 30))
    # Draw right leg:
    elif left_right == "right":
        # Draw leg:
        ellipse(s, BROWN, (x+80, y-30, 40, 100))
        # Draw foot:
        ellipse(s, BROWN, (x+85, y+42, 60, 30))


def draw_spear(s, x, y):
    """Draw spear"""
    line(s, BLACK, (x-60, y-250), (x-60, y+70), 3)


def draw_cat(s, posX, posY, scale=600):
    """Draw cat"""
    surface_resolution = 600
    x, y = surface_resolution//2, surface_resolution//2
    surface = pygame.Surface((surface_resolution, surface_resolution), pygame.SRCALPHA, 32).convert_alpha()
    # Cat's body
    ellipse(surface, LIGHT_GRAY, (x, y, 150, 40))
    # Cat's legs
    tilted_ellipse(surface, x-45, y+10, 100, 15, LIGHT_GRAY, 15)
    tilted_ellipse(surface, x-60, y+10, 100, 15, LIGHT_GRAY, 5)
    tilted_ellipse(surface, x+75, y-140, 100, 15, LIGHT_GRAY, 150)
    tilted_ellipse(surface, x+55, y-130, 100, 15, LIGHT_GRAY, 150)
    # Cat's tail:
    tilted_ellipse(surface, x+135, y-45, 120, 20, LIGHT_GRAY, 20)

    draw_fish(surface, x-75, y-15)
    draw_cat_head(surface, x+5, y-25)

    surface_scale = pygame.transform.scale(surface, (scale, scale))
    return s.blit(surface_scale, (posX, posY))

def draw_cat_head(s, x, y):
    """ Draw cat head"""
    draw_cat_fang(s, x, y)
    draw_cat_fang(s, x + 14, y + 4)
    ellipse(s, LIGHT_GRAY, (x, y, 50, 35))
    # Cat's nose:
    polygon(s, BLACK, [[x + 10, y + 18], [x + 16, y + 18], [x + 13, y + 22]])
    # Left cat's eye:
    draw_cat_eye(s, x + 5, y + 5)
    # Right cat's eye:
    draw_cat_eye(s, x + 25, y + 10)
    # Left cat's ear:
    draw_cat_ear(s, x + 18, y)
    # Right cat's ear:
    draw_cat_ear(s, x + 36, y + 5)


def draw_cat_eye(s, x, y):
    """Draw cat' eye"""
    ellipse(s, WHITE, (x, y, 13, 8))
    # Pupil:
    circle(s, BLACK, (x + 9, y + 4), 3)


def draw_cat_ear(s, x, y):
    """ Draw cat's ear"""
    polygon(s, LIGHT_GRAY, [[x, y], [x + 5, y - 10], [x + 13, y + 5]])


def draw_cat_fang(s, x, y):
    """ Draw cat's fang"""
    polygon(s, WHITE, [[x + 4, y + 28], [x + 8, y + 28], [x + 6, y + 34]])


def tilted_ellipse(s, pos1, pos2, size_x, size_y, color, angle):
    """
    Draws an ellipse that is tilted at an angle
    s - an surface
    pos1, pos2 - surface coordinates
    size_x, size_y - ellipse's size
    color - which color of ellipse is
    angle - ellipse tilting angle
    """
    surface_ellipse = pygame.Surface((150, 150), pygame.SRCALPHA, 32).convert_alpha()
    ellipse(surface_ellipse, color, (0, 0, size_x, size_y))
    surface_ellipse2 = pygame.transform.rotate(surface_ellipse, angle)
    return s.blit(surface_ellipse2, (pos1, pos2))


def draw_fish(s, x, y):
    """Draw fish"""
    polygon(s, RED, [[x + 75, y + 10], [x + 68, y], [x + 81, y + 3], [x + 81, y + 10]])
    # Fish's bottom fin
    polygon(s, RED, [[x + 70, y + 20], [x + 68, y + 22], [x + 70, y + 27], [x + 100, y + 45], [x + 90, y + 30],
                          [x + 90, y + 20]])
    # Fish's body:
    tilted_ellipse(s, x, y, 70, 16, DARK_GRAY, -20)
    # Fish's tail:
    polygon(s, DARK_GRAY, [[x + 108, y + 30], [x + 140, y + 23], [x + 135, y + 46]])
    # Fish's eye:
    circle(s, BLUE, (x + 58, y + 10), 3)
    # Fish's top fin


def draw_picture():
    """
    Draw picture:
    Chukcha, cat with fish, iglu
    """
    draw_environment()

    draw_iglu(screen, 30, 320, 250)
    draw_iglu(screen, 300, 350, 250)
    draw_iglu(screen, 50, 200)
    draw_iglu(screen, 45, 450, 250)
    draw_iglu(screen, 200, 450, 300)

    draw_chukcha(screen, 580, 450, 100)
    draw_chukcha(screen, 480, 460, 200)
    draw_chukcha(screen, 335, 500, 200)
    draw_chukcha(screen, 480, 450, 100)
    draw_chukcha(screen, 570, 450, 200)
    draw_chukcha(screen, 650, 550, 200)
    draw_chukcha(screen, 420, 530, 200)
    draw_chukcha(screen, 250, 550)

    draw_cat(screen, -130, 410)
    draw_cat(screen, -250, 550)
    draw_cat(screen, -400, 370)
    draw_cat(screen, -160, 680)
    draw_cat(screen, 160, 680)

draw_picture()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
