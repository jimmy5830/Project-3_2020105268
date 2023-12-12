import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math



def draw_triangle(color):
    glBegin(GL_TRIANGLES)
    
    if color == 'R':
        glColor3f(1.0, 0.0, 0.0)  # Red
    elif color == 'G':
        glColor3f(0.0, 1.0, 0.0)  # Green
    elif color == 'B':
        glColor3f(0.0, 0.0, 1.0)  # Blue
    elif color == 'Y':
        glColor3f(1.0, 1.0, 0.0)  # Yellow
    elif color == 'M':
        glColor3f(1.0, 0.0, 1.0)  # Magenta
    elif color == 'C':
        glColor3f(0.0, 1.0, 1.0)  # Cyan
    elif color == 'K':
        glColor3f(0.0, 0.0, 0.0)  # Black
    elif color == 'W':
        glColor3f(1.0, 1.0, 1.0)  # White
    else:
        glColor3f(1.0, 1.0, 1.0)  # Default to white
    
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, -1.0)
    
    glEnd()
    
def draw_rectangle(color):
    glBegin(GL_QUADS)
    
    if color == 'R':
        glColor3f(1.0, 0.0, 0.0)  # Red
    elif color == 'G':
        glColor3f(0.0, 1.0, 0.0)  # Green
    elif color == 'B':
        glColor3f(0.0, 0.0, 1.0)  # Blue
    elif color == 'Y':
        glColor3f(1.0, 1.0, 0.0)  # Yellow
    elif color == 'M':
        glColor3f(1.0, 0.0, 1.0)  # Magenta
    elif color == 'C':
        glColor3f(0.0, 1.0, 1.0)  # Cyan
    elif color == 'K':
        glColor3f(0.0, 0.0, 0.0)  # Black
    elif color == 'W':
        glColor3f(1.0, 1.0, 1.0)  # White
    else:
        glColor3f(1.0, 1.0, 1.0)  # Default to white
    
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    
    glEnd()
    
def draw_pentagon(color):
    glBegin(GL_POLYGON)
    
    if color == 'R':
        glColor3f(1.0, 0.0, 0.0)  # Red
    elif color == 'G':
        glColor3f(0.0, 1.0, 0.0)  # Green
    elif color == 'B':
        glColor3f(0.0, 0.0, 1.0)  # Blue
    elif color == 'Y':
        glColor3f(1.0, 1.0, 0.0)  # Yellow
    elif color == 'M':
        glColor3f(1.0, 0.0, 1.0)  # Magenta
    elif color == 'C':
        glColor3f(0.0, 1.0, 1.0)  # Cyan
    elif color == 'K':
        glColor3f(0.0, 0.0, 0.0)  # Black
    elif color == 'W':
        glColor3f(1.0, 1.0, 1.0)  # White
    else:
        glColor3f(1.0, 1.0, 1.0)  # Default to white
    

    # Vertices for a simple pentagon
    glVertex3f(0.0, 1.2, 0.0)
    glVertex3f(-1.05, 0.45, 0.0)
    glVertex3f(-0.75, -0.75, 0.0)
    glVertex3f(0.75, -0.75, 0.0)
    glVertex3f(1.05, 0.45, 0.0)
    
    glEnd()

def draw_hexagon(color):
    glBegin(GL_POLYGON)
    
    if color == 'R':
        glColor3f(1.0, 0.0, 0.0)  # Red
    elif color == 'G':
        glColor3f(0.0, 1.0, 0.0)  # Green
    elif color == 'B':
        glColor3f(0.0, 0.0, 1.0)  # Blue
    elif color == 'Y':
        glColor3f(1.0, 1.0, 0.0)  # Yellow
    elif color == 'M':
        glColor3f(1.0, 0.0, 1.0)  # Magenta
    elif color == 'C':
        glColor3f(0.0, 1.0, 1.0)  # Cyan
    elif color == 'K':
        glColor3f(0.0, 0.0, 0.0)  # Black
    elif color == 'W':
        glColor3f(1.0, 1.0, 1.0)  # White
    else:
        glColor3f(1.0, 1.0, 1.0)  # Default to white

    radius = 1.2
    
    for i in range(6):
        angle = 2 * math.pi * i / 6
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0.0)
    
    glEnd()
    
def draw_heptagon(color):
    glBegin(GL_POLYGON)
    
    if color == 'R':
        glColor3f(1.0, 0.0, 0.0)  # Red
    elif color == 'G':
        glColor3f(0.0, 1.0, 0.0)  # Green
    elif color == 'B':
        glColor3f(0.0, 0.0, 1.0)  # Blue
    elif color == 'Y':
        glColor3f(1.0, 1.0, 0.0)  # Yellow
    elif color == 'M':
        glColor3f(1.0, 0.0, 1.0)  # Magenta
    elif color == 'C':
        glColor3f(0.0, 1.0, 1.0)  # Cyan
    elif color == 'K':
        glColor3f(0.0, 0.0, 0.0)  # Black
    elif color == 'W':
        glColor3f(1.0, 1.0, 1.0)  # White
    else:
        glColor3f(1.0, 1.0, 1.0)  # Default to white

    radius = 1.2
    
    for i in range(7):
        angle = 2 * math.pi * i / 7
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0.0)
    
    glEnd()
    
def draw_Octagon(color):
    glBegin(GL_POLYGON)
    
    if color == 'R':
        glColor3f(1.0, 0.0, 0.0)  # Red
    elif color == 'G':
        glColor3f(0.0, 1.0, 0.0)  # Green
    elif color == 'B':
        glColor3f(0.0, 0.0, 1.0)  # Blue
    elif color == 'Y':
        glColor3f(1.0, 1.0, 0.0)  # Yellow
    elif color == 'M':
        glColor3f(1.0, 0.0, 1.0)  # Magenta
    elif color == 'C':
        glColor3f(0.0, 1.0, 1.0)  # Cyan
    elif color == 'K':
        glColor3f(0.0, 0.0, 0.0)  # Black
    elif color == 'W':
        glColor3f(1.0, 1.0, 1.0)  # White
    else:
        glColor3f(1.0, 1.0, 1.0)  # Default to white

    radius = 1.2
    
    for i in range(8):
        angle = 2 * math.pi * i / 8
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0.0)
    
    glEnd()
    
def draw_Nonagon(color):
    glBegin(GL_POLYGON)
    
    if color == 'R':
        glColor3f(1.0, 0.0, 0.0)  # Red
    elif color == 'G':
        glColor3f(0.0, 1.0, 0.0)  # Green
    elif color == 'B':
        glColor3f(0.0, 0.0, 1.0)  # Blue
    elif color == 'Y':
        glColor3f(1.0, 1.0, 0.0)  # Yellow
    elif color == 'M':
        glColor3f(1.0, 0.0, 1.0)  # Magenta
    elif color == 'C':
        glColor3f(0.0, 1.0, 1.0)  # Cyan
    elif color == 'K':
        glColor3f(0.0, 0.0, 0.0)  # Black
    elif color == 'W':
        glColor3f(1.0, 1.0, 1.0)  # White
    else:
        glColor3f(1.0, 1.0, 1.0)  # Default to white

    radius = 1.2
    
    for i in range(10):
        angle = 2 * math.pi * i / 10
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0.0)
    
    glEnd()
    
def draw_circle(color):
    glBegin(GL_POLYGON)
    
    if color == 'R':
        glColor3f(1.0, 0.0, 0.0)  # Red
    elif color == 'G':
        glColor3f(0.0, 1.0, 0.0)  # Green
    elif color == 'B':
        glColor3f(0.0, 0.0, 1.0)  # Blue
    elif color == 'Y':
        glColor3f(1.0, 1.0, 0.0)  # Yellow
    elif color == 'M':
        glColor3f(1.0, 0.0, 1.0)  # Magenta
    elif color == 'C':
        glColor3f(0.0, 1.0, 1.0)  # Cyan
    elif color == 'K':
        glColor3f(0.0, 0.0, 0.0)  # Black
    elif color == 'W':
        glColor3f(1.0, 1.0, 1.0)  # White
    else:
        glColor3f(1.0, 1.0, 1.0)  # Default to white
        
    radius = 1
    
    for i in range(100):
        theta = 2.0 * math.pi * i / 100
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex3f(x, y, 0.0)
    
    glEnd()
        

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    
    glTranslate(0.0, 0.0, -5)
    
    color_input = ''
    Shape_input = ''  # Initialize Shape_input
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_3:
                    Shape_input = '3'
                elif event.key == K_4:
                    Shape_input = '4'
                elif event.key == K_5:
                    Shape_input = '5'
                elif event.key == K_6:
                    Shape_input = '6'
                elif event.key == K_7:
                    Shape_input = '7'
                elif event.key == K_8:
                    Shape_input = '8'
                elif event.key == K_9:
                    Shape_input = '9'
                elif event.key == K_0:
                    Shape_input = '0'
                elif event.key == K_r:
                    color_input = 'R'
                elif event.key == K_g:
                    color_input = 'G'
                elif event.key == K_b:
                    color_input = 'B'
                elif event.key == K_y:
                    color_input = 'Y'
                elif event.key == K_m:
                    color_input = 'M'
                elif event.key == K_c:
                    color_input = 'C'    
                elif event.key == K_k:
                    color_input = 'K'
                elif event.key == K_w:
                    color_input = 'W'
        
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        if Shape_input == '3':
             draw_triangle(color_input)
        elif Shape_input == '4': 
             draw_rectangle(color_input)
        elif Shape_input == '5':
             draw_pentagon(color_input)
        elif Shape_input == '6':
             draw_hexagon(color_input)
        elif Shape_input == '7':
             draw_heptagon(color_input)
        elif Shape_input == '8':
             draw_Octagon(color_input)
        elif Shape_input == '9':
             draw_Nonagon(color_input)
        elif Shape_input == '0':
             draw_circle(color_input)
            
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
