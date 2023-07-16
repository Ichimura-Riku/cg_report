import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


shoulder = 0
elbow = 0
thigh = 0
shin = 0
fast = 0
rad = 0
endF = 0

def end():
    sys.exit()

def myInit():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"p3-robot")
    glClearColor(0.0, 0.0, 0.0, 0.0)

def mySetLight():
    glEnable(GL_LIGHT0)


def myDisplay():
    mtrl_specular = [1.0, 1.0, 1.0, 1.0]
    mtrl_shininess = [50.0]
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mtrl_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mtrl_shininess)

    glTranslated(0.0, 0.0, 0.0)
    glPushMatrix()
    glScaled(3.0, 4.0, 1.0)
    glutWireCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glPushMatrix()
    glTranslated(2.0, 2.0, 0.0)
    glPushMatrix()
    glScaled(0.0, 0.0, 0.0)
    glutWireCube(1.0)
    glPopMatrix()
    glRotated(shoulder, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()
    glScaled(1.0, -2.0, 1.0)
    glutWireCube(1.0)
    glPopMatrix()
    glTranslated(0.0, -1.0, 0.0)
    glRotated(elbow, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()
    glScaled(1.0, 2.0, 1.0)
    glutWireCube(1.0)
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    glTranslated(-2.0, 2.0, 0.0)
    glPushMatrix()
    glScaled(0.0, 0.0, 0.0)
    glutWireCube(1.0)
    glPopMatrix()
    glRotated(-shoulder, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()
    glScaled(1.0, -2.0, 1.0)
    glutWireCube(1.0)
    glPopMatrix()
    glTranslated(0.0, -1.0, 0.0)
    glRotated(-elbow + 180, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()
    glScaled(1.0, 2.0, 1.0)
    glutWireCube(1.0)
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.0, 3.0, 0.0)
    glPushMatrix()
    glutWireSphere(1.0, 10, 10)
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.0, -2.0, 0.0)
    glPushMatrix()
    glScaled(0.0, 0.0, 0.0)
    glutWireCube(1.0)
    glPopMatrix()
    glRotated(-thigh - 15, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.5, 0.0)
    glPushMatrix()
    glScaled(1.0, -3.0, 1.0)
    glutWireCube(1.0)
    glPopMatrix()
    glTranslated(0.0, -1.5, 0.0)
    glRotated(-shin + 15, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()
    glScaled(1.0, 2.0, 1.0)
    glutWireCube(1.0)
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    glTranslated(-1.0, -2.0, 0.0)
    glPushMatrix()
    glScaled(0.0, 0.0, 0.0)
    glutWireCube(1.0)
    glPopMatrix()
    glRotated(thigh - 15, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.5, 0.0)
    glPushMatrix()
    glScaled(1.0, -3.0, 1.0)
    glutWireCube(1.0)
    glPopMatrix()
    glTranslated(0.0, -1.5, 0.0)
    glRotated(shin + 15, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()
    glScaled(1.0, 2.0, 1.0)
    glutWireCube(1.0)
    glPopMatrix()
    glPopMatrix()

    glPopMatrix()

    glutSwapBuffers()

def myReshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, width / height, 0.1, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 15.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def myKeyboard(key, x, y):
    global fast

    if key == b'u':
        fast = 0.002 - fast
    elif key == b'\x1b':
        endF += 1

def myIdle():
    global rad, shoulder, elbow, thigh, shin
    rad = (rad + 0.0001 + fast) % 2.0
    shoulder = int(math.sin(rad * math.pi) * 60)
    elbow = int(-math.sin(rad * math.pi) * 60 - 90)
    thigh = int(math.sin(rad * math.pi) * 30)
    shin = int(-math.sin(rad * math.pi) * 30)
    glutPostRedisplay()
    if endF:
        end()

def main():
    glutInit()
    myInit()
    glutKeyboardFunc(myKeyboard)
    glutReshapeFunc(myReshape)
    glutIdleFunc(myIdle)
    mySetLight()
    glutDisplayFunc(myDisplay)
    glutMainLoop()


if __name__ == "__main__":
    main()
