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

def draw_circle(a, b, r):
  d = 1 - r
  x = 0
  y = r
  while x <= y:
      x += 1
      if d < 0:
          d += 2 * x + 1
      else:
          y -= 1
          d += 2 * (x - y) + 1
      draw_points(a + x, b + y)
      draw_points(a - x, b + y)
      draw_points(a + x, b - y)
      draw_points(a - x, b - y)
      draw_points(a + y, b + x)
      draw_points(a - y, b + x)
      draw_points(a + y, b - x)
      draw_points(a - y, b - x)

def iterate():
  glViewport(0, 0, 700, 700)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(0.0, 700, 0.0, 700, 0.0, 1.0)
  glMatrixMode (GL_MODELVIEW)
  glLoadIdentity()

def showScreen():
  a = 350
  b = 350
  r = 250
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()

  glColor3f(1.0, 1.0, 0.0)
  draw_circle(a, b, r)
  q = math.floor(math.sqrt(((r/2)**2)/2))
  h = r/2

  draw_circle(a, b+h, h)
  draw_circle(a+h, b, h)
  draw_circle(a-h, b, h)
  draw_circle(a, b-h, h)
  draw_circle(a+q, b+q, h)
  draw_circle(a+q, b-q, h)
  draw_circle(a-q, b-q, h)
  draw_circle(a-q, b+q, h)


  glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Circle**9")

glutDisplayFunc(showScreen)

glutMainLoop()