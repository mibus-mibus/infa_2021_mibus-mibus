import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))


def draw_background(color_background=(133, 133, 133)):
    """
    Draw background
    default color gray (133, 133, 133)
    """
    rect(screen, color_background, (0, 0, 400, 400), )


def draw_head(color_head=(255, 255, 0), position_head=(200, 200), radius_head=150):
    """
    Draw head
    default color - yellow (255, 255, 0)
    default position 200, 200
    default radius 150
    """
    circle(screen, color_head, position_head, radius_head)
    circle(screen, (0, 0, 0), position_head, radius_head, 5)  # border head


def draw_eye(color_eye, position_eye, radius_eye):
    """
    Draw eye
    """
    circle(screen, color_eye, position_eye, radius_eye)
    circle(screen, (0, 0, 0), position_eye, radius_eye, 2) #border eye
    circle(screen, (0, 0, 0), position_eye, 12)  # draw pupil

def draw_eyebrow(x1, y1, x2, y2):
    """Draw black eyebrow"""
    line (screen, (0, 0, 0), (x1, y1), (x2, y2), 20)

def draw_mouth(x1, y1, x2, y2):
    """Draw black mouth"""
    line(screen, (0, 0, 0), (x1, y1), (x2, y2), 50)

def draw_smile():
    """ Draw smile with head, eyes, eyebrows and mouth"""
    draw_head()
    draw_eye((255, 0, 0), (130, 180), 30) #left eye red color
    draw_eye((255, 0, 0), (270, 180), 25) #right eye red color
    draw_eyebrow(170, 160, 50, 80) #right eyebrow
    draw_eyebrow(230, 150, 350, 120)  # left eyebrow
    draw_mouth(150, 280, 250, 280)


draw_background()
draw_smile()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
