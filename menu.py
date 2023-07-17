from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

sizeOfTeapot = 1.0

def myKeyboard(key, x, y):
    if key == b'\x1b':
        sys.exit(0)

def myInit(progname):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(progname.decode())
    # glutCreateWindow(progname.encode())
    glClearColor(0.0, 0.0, 0.0, 1.0)

def myReshape(width, height):
    ratio, a = 5.0, 5.0

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if width <= height:
        ratio = height / width
        glOrtho(-a, a, -a * ratio, a * ratio, -10.0, 10.0)
    else:
        ratio = width / height
        glOrtho(-a * ratio, a * ratio, -a, a, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def getValueFromMenu(value):
    global sizeOfTeapot
    if value == 1:
        sizeOfTeapot = 0.5
    elif value == 2:
        sizeOfTeapot = 1.0
    elif value == 3:
        sizeOfTeapot = 2.0

def mySetMenu():
    menu = glutCreateMenu(getValueFromMenu)
    glutAddMenuEntry("x 0.5", 1)
    glutAddMenuEntry("x 1.0", 2)
    glutAddMenuEntry("x 2.0", 3)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

def myDisplay():
    text = "Size is"

    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslated(0.0, 0.0, -3.0)
    glColor3d(1.0, 0.0, 0.0)
    glutWireTeapot(sizeOfTeapot)

    glRasterPos3d(-1.0, -3.0, 0.0)
    for char in (text + "{:.1f}".format(sizeOfTeapot)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
    glPopMatrix()
    glutSwapBuffers()

def myIdle():
    glutPostRedisplay()

def main():
    progname = sys.argv[0].encode()
    myInit(progname)
    mySetMenu()
    glutKeyboardFunc(myKeyboard)
    glutIdleFunc(myIdle)
    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisplay)
    glutMainLoop()

if __name__ == "__main__":
    main()
