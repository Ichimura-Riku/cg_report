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
gPitch = 30
gYaw = 30

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

def robotBody():

    x = 3.0 / 2
    y = 4.0 / 2
    z = 1.0 / 2

    glPushMatrix()
    # glRotated(gPitch, 1, 0, 0)
    # glRotated(gYaw, 0, 0, 1)

    glBegin(GL_QUADS)
    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, -y, -z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()

    glPopMatrix()
def robotRightArm():
    x = 3.0 / 2
    y = 4.0 / 2
    z = 1.0 / 2

    glPushMatrix()
    # glRotated(gPitch, 1, 0, 0)
    # glRotated(gYaw, 0, 0, 1)

    glBegin(GL_QUADS)
    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, -y, -z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()

    glPopMatrix()




def myDisplay():

    # ambient = [0.7, 0.7, 0.7, 1.0]
    # diffuse = [0.75, 0.75, 0.75, 1.0]
    # specular = [0.25, 0.25, 0.25, 1.0]
    ambient = [0.25, 0.25, 0.25, 1.0]
    diffuse = [0.4, 0.4, 0.4, 1.0]
    specular = [0.774597, 0.774597, 0.774597, 1.0]
    shininess = [76.8]
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

    # 図形描写
    # robotBody()


    glTranslated(0.0, 0.0, 0.0)
    # 多分胴体
    # glPushMatrix()
    # glScaled(3.0, 4.0, 1.0)
    # glutWireCube(1.0)
    # glPopMatrix()

    # glPushMatrix()
    # 右側の腕
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



    # glPushMatrix()
    # glTranslated(-2.0, 2.0, 0.0)
    # glPushMatrix()
    # glScaled(0.0, 0.0, 0.0)
    # glutWireCube(1.0)
    # glPopMatrix()
    # glRotated(-shoulder, 1.0, 0.0, 0.0)
    # glTranslated(0.0, -1.0, 0.0)
    # glPushMatrix()
    # glScaled(1.0, -2.0, 1.0)
    # glutWireCube(1.0)
    # glPopMatrix()
    # glTranslated(0.0, -1.0, 0.0)
    # glRotated(-elbow + 180, 1.0, 0.0, 0.0)
    # glTranslated(0.0, -1.0, 0.0)
    # glPushMatrix()
    # glScaled(1.0, 2.0, 1.0)
    # glutWireCube(1.0)
    # glPopMatrix()
    # glPopMatrix()

    # glPushMatrix()
    # glTranslated(0.0, 3.0, 0.0)
    # glPushMatrix()
    # glutWireSphere(1.0, 10, 10)
    # glPopMatrix()
    # glPopMatrix()

    # glPushMatrix()
    # glTranslated(1.0, -2.0, 0.0)
    # glPushMatrix()
    # glScaled(0.0, 0.0, 0.0)
    # glutWireCube(1.0)
    # glPopMatrix()
    # glRotated(-thigh - 15, 1.0, 0.0, 0.0)
    # glTranslated(0.0, -1.5, 0.0)
    # glPushMatrix()
    # glScaled(1.0, -3.0, 1.0)
    # glutWireCube(1.0)
    # glPopMatrix()
    # glTranslated(0.0, -1.5, 0.0)
    # glRotated(-shin + 15, 1.0, 0.0, 0.0)
    # glTranslated(0.0, -1.0, 0.0)
    # glPushMatrix()
    # glScaled(1.0, 2.0, 1.0)
    # glutWireCube(1.0)
    # glPopMatrix()
    # glPopMatrix()

    # glPushMatrix()
    # glTranslated(-1.0, -2.0, 0.0)
    # glPushMatrix()
    # glScaled(0.0, 0.0, 0.0)
    # glutWireCube(1.0)
    # glPopMatrix()
    # glRotated(thigh - 15, 1.0, 0.0, 0.0)
    # glTranslated(0.0, -1.5, 0.0)
    # glPushMatrix()
    # glScaled(1.0, -3.0, 1.0)
    # glutWireCube(1.0)
    # glPopMatrix()
    # glTranslated(0.0, -1.5, 0.0)
    # glRotated(shin + 15, 1.0, 0.0, 0.0)
    # glTranslated(0.0, -1.0, 0.0)
    # glPushMatrix()
    # glScaled(1.0, 2.0, 1.0)
    # glutWireCube(1.0)
    # glPopMatrix()
    # glPopMatrix()

    # glPopMatrix()

    glutSwapBuffers()

def myReshape(width, height):
    a = 3.0
    z = 20.0
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # gluPerspective(60.0, width / height, 0.1, 20.0)
    if width <= height:
        glOrtho(-a, a, -a * height / width, a * height / width, -z, z)
    else:
        glOrtho(-a * width / height, a * width / height, -a, a, -z, z)
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

def myTimer(value):
    if value == 1:
        glutTimerFunc(30, myTimer, 1)
        global gPitch, gYaw
        gYaw = (gYaw + 2) % 360
        gPitch = (gPitch + 2) % 360
        glutPostRedisplay()

def main():
    glutInit()
    myInit()
    glutKeyboardFunc(myKeyboard)
    glutTimerFunc(30, myTimer, 1)
    glutReshapeFunc(myReshape)
    glutIdleFunc(myIdle)
    mySetLight()
    glutDisplayFunc(myDisplay)
    glutMainLoop()


if __name__ == "__main__":
    main()
