from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

win_width = 500
win_height = 500
dot_speed = 0.01
dots = []
freeze = False
blink = False
blink_interval = 0.5
last_blink_time = 0


def draw_dot(x, y, color):
    global blink
    if not blink or random.random() > 0.5:
        glColor3f(*color)
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()


def update_dots():
    global dot_speed
    for dot in dots:
        if not freeze:
            pos, color, velocity = dot
            x, y = pos
            dx, dy = velocity

            x += dx * dot_speed
            y += dy * dot_speed

            # boundaries and bounce check
            if x < 0 or x > win_width:
                dx = -dx
            if y < 0 or y > win_height:
                dy = -dy

            # Update dot information
            dot[0] = (x, y)
            dot[2] = (dx, dy)


def dot_display():
    glClear(GL_COLOR_BUFFER_BIT)
    update_dots()
    for dot in dots:
        draw_dot(*dot[0], dot[1])  # Unpack dot position and color
    glutSwapBuffers()
    glutPostRedisplay()


def mouse_right(button, state, x, y):
    global dots
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        # Random color for new dot
        direction = random.uniform(0, 2 * math.pi)
        velocity = (math.cos(direction), math.sin(direction))
        dots.append([(x, win_height - y), (random.random(), random.random(), random.random()), velocity])
        glutPostRedisplay()


def dot_blink():
    global blink
    blink = not blink


def keyboard(key, x, y):
    global freeze, dot_speed, blink, last_blink_time
    if key == b' ':
        freeze = not freeze
    elif key == GLUT_KEY_UP:
        dot_speed += 0.01
        print("Speed Up. Current Speed:", dot_speed)
    elif key == GLUT_KEY_DOWN:
        dot_speed -= 0.005
        if dot_speed < 0:
            dot_speed = 0
        print("Speed Down. Current Speed:", dot_speed)
    elif key == GLUT_KEY_LEFT:
        current_time = glutGet(GLUT_ELAPSED_TIME) / 1000.0
        if current_time - last_blink_time > blink_interval:
            dot_blink()
            last_blink_time = current_time


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(win_width, win_height)
glutCreateWindow(b"Dancing Dots")
glutDisplayFunc(dot_display)
glutMouseFunc(mouse_right)
glutKeyboardFunc(keyboard)
glutSpecialFunc(keyboard)
glColor3f(0.0, 0.0, 0.0)
gluOrtho2D(0, win_width, 0, win_height)
glutMainLoop()
