import time
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def midpoint(a, b, r):
    d = 1 - r / 2
    x = 0
    y = r

    while x <= y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * x - 2 * y + 5
            y -= 1
        x += 1
        draw_points((a + x)/2, (b + y)/2)
        draw_points((a - x)/2, (b + y)/2)
        draw_points((a + x)/2, (b - y)/2)
        draw_points((a - x)/2, (b - y)/2)
        draw_points((a + y)/2, (b + x)/2)
        draw_points((a - y)/2, (b + x)/2)
        draw_points((a + y)/2, (b - x)/2)
        draw_points((a - y)/2, (b - x)/2)

def draw_circle(a, b, r, num=10):
   num2 = math.pi * 2 / num
   for a in range(num):
       midpoint(a + (r / 2) * math.cos(a * num2), b + (r / 2) * math.sin(a * num2), r / 2)

def iterate():
  glViewport(0, 0, 700, 700)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
  glMatrixMode (GL_MODELVIEW)
  glLoadIdentity()

def showScreen():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glLoadIdentity()
   iterate()
   glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
   #call the draw methods here
   draw_circle(500, 500, 300, num)
   #draw_points(250, 250, 200)
   glutSwapBuffers()


#WIDTH, HEIGHT = 2,2
num = 10

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)


glutMainLoop()