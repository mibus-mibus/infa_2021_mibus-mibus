import pygame
from pygame.draw import *

FPS = 30
screen = pygame.display.set_mode((800, 1000))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220, 220, 220)
LIGHT_BROWN = (190, 140, 75)
BROWN = (172, 120, 69)
DARK_BROWN = (101, 67, 33)

def draw_environment():
    """
    Draw ground and sky
    """
    rect(screen, LIGHT_GRAY, (0, 0, 800, 450))  # grey sky
    rect(screen, WHITE, (0, 450, 800, 1000))  # white ground

def horizontal_arcs_iglu():
    """Draw horisontal iglu's arcs"""
    arc(screen, BLACK, (50, 560, 300, 20), 3.14, 0)
    arc(screen, BLACK, (60, 510, 280, 20), 3.14, 0)
    arc(screen, BLACK, (80, 460, 240, 20), 3.14, 0)
    arc(screen, BLACK, (120, 420, 160, 20), 3.14, 0)

def vertival_lines_iglu():
    """Draw vertical iglu's lines"""
    # top first line
    line(screen, BLACK, (180, 400), (170, 440))
    line(screen, BLACK, (220, 400), (230, 440))
    # second line
    line(screen, BLACK, (150, 438), (140, 480))
    line(screen, BLACK, (200, 438), (200, 480))
    line(screen, BLACK, (250, 438), (260, 480))
    # third line
    line(screen, BLACK, (115, 477), (95, 525))
    line(screen, BLACK, (170, 480), (165, 528))
    line(screen, BLACK, (235, 480), (240, 528))
    line(screen, BLACK, (285, 480), (300, 528))
    # forth line
    line(screen, BLACK, (70, 525), (60, 570))
    line(screen, BLACK, (125, 530), (115, 580))
    line(screen, BLACK, (200, 530), (200, 580))
    line(screen, BLACK, (270, 530), (275, 580))
    line(screen, BLACK, (330, 525), (340, 570))

def draw_bricks_iglu():
    """Draw ilu's bricks"""
    horizontal_arcs_iglu()
    vertival_lines_iglu()

def draw_iglu():
    """
    Draw iglu
    """
    # Fill iglu:
    polygon(screen, LIGHT_GRAY,
            [[50, 570], [67, 505], [88, 455],
             [150, 410], [200, 400], [250, 410],
             [312, 455], [333, 505], [350, 570], [200, 580]])
    # iglu's border:
    arc(screen, BLACK, (50, 400, 300, 350), 0, 3.14, 4)

    draw_bricks_iglu()

def draw_chukcha():
    draw_chukcha_body()
    draw_chukcha_head()
    draw_chukcha_hand()
    draw_chukcha_leg()
    draw_spear()

def draw_chukcha_head():
    """ Draw head's chukcha"""
    draw_chukcha_hood()
    draw_chukcha_face()


def draw_chukcha_face():
    """Draw face's chukcha"""
    #Face:
    ellipse(screen, LIGHT_GRAY, (550, 550, 80, 60))
    #Left eye:
    line(screen, BLACK, (563, 570), (577, 575))
    #Right eye:
    line(screen, BLACK, (600, 575), (614, 570))
    #Mause:
    lines(screen, BLACK, False, [[570, 595], [578, 590], [602, 590], [610, 595]])

def draw_chukcha_hood():
    """Draw hood's chukcha"""
    #Foor:
    ellipse(screen, LIGHT_GRAY, (530, 530, 120, 100))
    #Hood:
    ellipse(screen, LIGHT_BROWN, (540, 540, 100, 80))

def draw_chukcha_body():
    polygon(screen, BROWN, [[520, 750], [530, 680], [550, 600], [630, 600], [650, 680], [660, 750]])
    #Horizontal fur line on the chukcha's coat:
    rect(screen, DARK_BROWN, (520, 740, 140, 10))
    #Vertical fur line on the chukcha's coat:
    rect (screen, DARK_BROWN, (580, 600, 20, 150))

def draw_chukcha_hand():
    pass

def draw_chukcha_leg():
    pass

def draw_spear():
    pass


def draw_cat():
    pass


def draw_fish():
    pass


def draw_picture():
    """
    Draw picture:
    Chukcha, cat with fish, iglu
    """
    draw_environment()
    draw_iglu()
    draw_chukcha()
    draw_cat()
    draw_fish()


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
