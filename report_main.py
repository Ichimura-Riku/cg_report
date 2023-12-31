import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from PIL import Image
import numpy as np


shoulder = 0
elbow = 0
thigh = 0
shin = 0
fast = 0
rad = 0
endF = 0
gPitch = 0
gYaw = 0
gZ = 0
gX = 0
Table_Width = 1.27
Table_Height = 2.54
imageWidth = 256
imageHeight = 256
texImage = np.zeros((imageHeight, imageWidth, 3), dtype=np.uint8)
view = 180
tile = 'yuka.ppm'
xStart, yStart = 0, 0
xAngle , yAngle = 0.0, 0.0
mouseFlag = GL_FALSE

def myInit():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"report_main")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)

def mySetLight():
    light0_position = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light0_position)
    glEnable(GL_LIGHT0)
    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)

def robotBody():

    x = 3.0 / 2
    y = 4.0 / 2
    z = 1.0 / 2

    glPushMatrix()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, -0.5)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(-x, y, z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, y, z)
    glVertex3d(x, -y, z)

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
    glVertex3d(-x, -y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(x, -y, z)
    glVertex3d(-x, -y, z)

    glEnd()

    glPopMatrix()

def robotRightArm():
    x =1.0 / 2
    y = -2.0 / 2
    z = 1.0 / 2
    glPushMatrix()



    glTranslated(2.0, 2.0, 0.0)
    glRotated(shoulder, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, -0.5)
    glVertex3d(-x, -y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, -y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, -z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, y, z)
    glVertex3d(-x, y, z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()


    glPopMatrix()

    glTranslated(0.0, -1.0, 0.0)
    glRotated(elbow, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)

    glPushMatrix()
    glBegin(GL_QUADS)


    glNormal3d(0, 0, -0.5)
    glVertex3d(-x, -y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, -y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, -z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, y, z)
    glVertex3d(-x, y, z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()
    glPopMatrix()
    glPopMatrix()

def robotLeftArm():
    x =1.0 / 2
    y = -2.0 / 2
    z = 1.0 / 2
    glPushMatrix()



    glTranslated(-2.0, 2.0, 0.0)
    glRotated(-shoulder, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, -0.5)
    glVertex3d(-x, -y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, -y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, -z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, y, z)
    glVertex3d(-x, y, z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()


    glPopMatrix()

    glTranslated(0.0, -1.0, 0.0)
    glRotated(-elbow + 180, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)

    glPushMatrix()
    glBegin(GL_QUADS)


    glNormal3d(0, 0, -0.5)
    glVertex3d(-x, -y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, -y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, -z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, y, z)
    glVertex3d(-x, y, z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()
    glPopMatrix()
    glPopMatrix()

def robotRightLeg():
    x =1.0 / 2
    y = -2.0 / 2
    z = 1.0 / 2
    glPushMatrix()



    glTranslated(-1.0, -2.0, 0.0)
    glRotated(thigh - 15, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, -0.5)
    glVertex3d(-x, -y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, -y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, -z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, y, z)
    glVertex3d(-x, y, z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()


    glPopMatrix()

    glTranslated(0.0, -1.0, 0.0)
    glRotated(shin + 15, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)

    glPushMatrix()
    glBegin(GL_QUADS)


    glNormal3d(0, 0, -0.5)
    glVertex3d(-x, -y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, -y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, -z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, y, z)
    glVertex3d(-x, y, z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()
    glPopMatrix()
    glPopMatrix()

def robotLeftLeg():
    x =1.0 / 2
    y = -2.0 / 2
    z = 1.0 / 2
    glPushMatrix()



    glTranslated(1.0, -2.0, 0.0)
    glRotated(-thigh - 15, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)
    glPushMatrix()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, -0.5)
    glVertex3d(-x, -y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, -y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, -z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, y, z)
    glVertex3d(-x, y, z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()


    glPopMatrix()

    glTranslated(0.0, -1.0, 0.0)
    glRotated(-shin + 15, 1.0, 0.0, 0.0)
    glTranslated(0.0, -1.0, 0.0)

    glPushMatrix()
    glBegin(GL_QUADS)


    glNormal3d(0, 0, -0.5)
    glVertex3d(-x, -y, -z)
    glVertex3d(x, -y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(-x, y, -z)

    glNormal3d(0, 0, 0.5)
    glVertex3d(-x, y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, -y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(1, 0, 0)
    glVertex3d(x, -y, z)
    glVertex3d(x, y, z)
    glVertex3d(x, y, -z)
    glVertex3d(x, -y, -z)

    glNormal3d(-1, 0, 0)
    glVertex3d(-x, -y, -z)
    glVertex3d(-x, y, -z)
    glVertex3d(-x, y, z)
    glVertex3d(-x, -y, z)

    glNormal3d(0, 1, 0)
    glVertex3d(-x, y, -z)
    glVertex3d(x, y, -z)
    glVertex3d(x, y, z)
    glVertex3d(-x, y, z)

    glNormal3d(0, -1, 0)
    glVertex3d(-x, -y, z)
    glVertex3d(x, -y, z)
    glVertex3d(x, -y, -z)
    glVertex3d(-x, -y, -z)

    glEnd()
    glPopMatrix()
    glPopMatrix()

def robotHead():
    glPushMatrix()

    glTranslated(0, 3.0, 0)
    glutSolidSphere(1, 20, 16)
    glPopMatrix()

def robotDisplay():
    ambient = [0.75, 0.75, 0.75, 1.0]
    diffuse = [0.4, 0.4, 0.4, 1.0]
    specular = [0.774597, 0.774597, 0.774597, 1.0]
    insideface = [1.0, 0.0, 0.0, 1.0]
    shininess = [76.8]
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)
    glMaterialfv(GL_BACK, GL_AMBIENT_AND_DIFFUSE, insideface)
    glMaterialf(GL_BACK, GL_SHININESS, 60)
    glPushMatrix()
    glRotated(view, 0, 1, 0)
    glRotated(gYaw, 0, 1, 0)

    robotBody()
    robotRightArm()
    robotLeftArm()
    robotRightLeg()
    robotLeftLeg()
    robotHead()
    glPopMatrix()

def readPPMImage(filename):
    with open(filename, 'rb') as fp:
        for i in range(4):
            while True:
                ch = fp.read(1)
                if ch != b'#':
                    break
                fp.readline()
                while ch.isspace():
                    ch = fp.read(1)
            while not ch.isspace():
                ch = fp.read(1)
            if i < 3:
                while ch.isspace():
                    ch = fp.read(1)
        fp.readinto(texImage)

def setUpTexture():
    readPPMImage(tile)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imageWidth, imageHeight, 0, GL_RGB, GL_UNSIGNED_BYTE, texImage)

def texDisplay():
    ambient = [1.0, 1.0, 1.0, 1.0]
    diffuse = [1.0, 1.0, 1.0, 1.0]
    specular = [0.0, 0.0, 0.0, 1.0]
    shininess = [76.8]
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

    tc = 1.0
    txX = 600.0
    p0 = [-txX,  -6.5, -txX]
    p1 = [-txX, -6.5,  txX]
    p2 = [txX, -6.5,  txX]
    p3 = [txX,  -6.5, -txX]

    glPushMatrix()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, 1)
    glTexCoord2d(0.0, 0.0)
    glVertex3dv(p0)
    glTexCoord2d(0.0, tc)
    glVertex3dv(p1)
    glTexCoord2d(tc, tc)
    glVertex3dv(p2)
    glTexCoord2d(tc, 0.0)
    glVertex3dv(p3)
    glEnd()
    glPopMatrix()

    glDisable(GL_TEXTURE_2D)


def myDisplay():

    glLoadIdentity()
    gluLookAt(15*math.sin(gYaw / 180 * math.pi) , 5.0, 15.0*math.cos(gYaw / 180 * math.pi), 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)



    setUpTexture()
    glPushMatrix()
    robotDisplay()

    glTranslated(gX, 0.0, gZ)


    texDisplay()
    glPopMatrix()

    glutSwapBuffers()

def myReshape(width, height):

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, width / height, 0.1, 1200.0)
    glMatrixMode(GL_MODELVIEW)

def myKeyboard(key, x, y):
    global fast, gYaw, gX, gZ, xAngle

    if key == b'u':
        fast = 1 - fast
    elif key == b'\x1b':
        endF += 1
    elif key == b'j':
        gYaw = (gYaw + 6) % 360
    elif key == b'l':
        gYaw = (gYaw - 6) % 360
    elif key == b'e' :
        if abs(gZ + (10 ** fast)*math.cos(gYaw / 180 * math.pi)) <= 600:
            gZ += (10 ** fast)*math.cos(gYaw / 180 * math.pi)
        if abs(gX + (10 ** fast)*math.sin(gYaw / 180 * math.pi)) <= 600:
            gX += (10 ** fast)*math.sin(gYaw / 180 * math.pi)
    elif key == b'd':
        if abs(gZ - (10 ** fast)*math.cos(gYaw / 180 * math.pi)) <= 600:
            gZ -= (10 ** fast)*math.cos(gYaw / 180 * math.pi)
        if abs(gX - (10 ** fast)*math.sin(gYaw / 180 * math.pi)) <= 600:
            gX -= (10 ** fast)*math.sin(gYaw / 180 * math.pi)
    elif key == b's':
        if abs(gZ - (10 ** fast)*math.sin(gYaw / 180 * math.pi)) <= 600:
            gZ -= (10 ** fast)*math.sin(gYaw / 180 * math.pi)
        if abs(gX + (10 ** fast)*math.cos(gYaw / 180 * math.pi)) <= 600:
            gX += (10 ** fast)*math.cos(gYaw / 180 * math.pi)
    elif key == b'f':
        if abs(gZ + (10 ** fast)*math.sin(gYaw / 180 * math.pi)) <= 600:
            gZ += (10 ** fast)*math.sin(gYaw / 180 * math.pi)
        if abs(gX - (10 ** fast)*math.cos(gYaw / 180 * math.pi)) <= 600:
            gX -= (10 ** fast)*math.cos(gYaw / 180 * math.pi)


def myIdle():

    global rad, shoulder, elbow, thigh, shin
    rad = (rad + 0.0001 + fast*0.02) % 2.0
    shoulder = int(math.sin(rad * math.pi) * 60)
    elbow = int(-math.sin(rad * math.pi) * 60 - 90)
    thigh = int(math.sin(rad * math.pi) * 30)
    shin = int(-math.sin(rad * math.pi) * 30)
    glutPostRedisplay()

def getValueFromMenu(value):
    global view, tile
    if value == 1:
        view =180
    elif value == 2:
        view = 0
    elif value == 3:
        tile = 'yuka.ppm'
    elif value == 4:
        tile = 'ice.ppm'
    elif value == 5:
        tile = 'walnut.ppm'

def mySetMenu():
    menu = glutCreateMenu(getValueFromMenu)
    glutAddMenuEntry("back view", 1)
    glutAddMenuEntry("front view", 2)
    glutAddMenuEntry("changeTile -> yuka", 3)
    glutAddMenuEntry("changeTile -> ice", 4)
    glutAddMenuEntry("changeTile -> walnut", 5)


    glutAttachMenu(GLUT_RIGHT_BUTTON)

def myTimer(value):

    if value == 1:
        glutTimerFunc(30, myTimer, 1)
        global gPitch
        gPitch = (gPitch + 2) % 360
        glutPostRedisplay()

def myMouseMotion(x, y):
    global xStart, yStart, xAngle , yAngle, mouseFlag
    xdis, ydis = 0, 0
    a = 0.5

    if mouseFlag == GL_FALSE :
        return
    xdis = x - xStart
    ydis = y - yStart

    xAngle += xdis *a
    yAngle += ydis *a

    xStart = x
    yStart = y
    glutPostRedisplay()

def myMouseFunc(button, state, x, y):
    global xStart, yStart, xAngle , yAngle, mouseFlag

    print((not button) and (not state))
    if (not button) and (not state):
        xStart = x
        yStart = y
        mouseFlag = GL_TRUE

    else:
        mouseFlag = GL_FALSE


def main():
    glutInit()
    myInit()
    mySetMenu()

    glutKeyboardFunc(myKeyboard)
    glutTimerFunc(30, myTimer, 1)
    glutReshapeFunc(myReshape)
    glutIdleFunc(myIdle)
    mySetLight()
    setUpTexture()
    glutMouseFunc(myMouseFunc);
    glutMotionFunc(myMouseMotion);
    glutDisplayFunc(myDisplay)
    glutMainLoop()


if __name__ == "__main__":
    main()
