# import math
# from OpenGL.GL import *
# from OpenGL.GLUT import *

# shoulder = 0
# elbow = 0
# thigh = 0
# shin = 0
# fast = 0
# rad = 0

# def myInit():
#     glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
#     glutInitWindowSize(500, 500)
#     glutInitWindowPosition(0, 0)
#     glutCreateWindow(b"p3-robot")
#     glClearColor(0.0, 0.0, 0.0, 0.0)

# def myDisplay():
#     glClear(GL_COLOR_BUFFER_BIT)

#     glTranslated(0.0, 0.0, 0.0)
#     glPushMatrix()
#     glScaled(3.0, 4.0, 1.0)
#     glutWireCube(1.0)
#     glPopMatrix()

#     glPushMatrix()
#     glPushMatrix()
#     glTranslated(2.0, 2.0, 0.0)
#     glPushMatrix()
#     glScaled(0.0, 0.0, 0.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glRotated(shoulder, 1.0, 0.0, 0.0)
#     glTranslated(0.0, -1.0, 0.0)
#     glPushMatrix()
#     glScaled(1.0, -2.0, 1.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glTranslated(0.0, -1.0, 0.0)
#     glRotated(elbow, 1.0, 0.0, 0.0)
#     glTranslated(0.0, -1.0, 0.0)
#     glPushMatrix()
#     glScaled(1.0, 2.0, 1.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glPopMatrix()

#     glPushMatrix()
#     glTranslated(-2.0, 2.0, 0.0)
#     glPushMatrix()
#     glScaled(0.0, 0.0, 0.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glRotated(-shoulder, 1.0, 0.0, 0.0)
#     glTranslated(0.0, -1.0, 0.0)
#     glPushMatrix()
#     glScaled(1.0, -2.0, 1.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glTranslated(0.0, -1.0, 0.0)
#     glRotated(-elbow + 180, 1.0, 0.0, 0.0)
#     glTranslated(0.0, -1.0, 0.0)
#     glPushMatrix()
#     glScaled(1.0, 2.0, 1.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glPopMatrix()

#     glPushMatrix()
#     glTranslated(0.0, 3.0, 0.0)
#     glPushMatrix()
#     glutWireSphere(1.0, 10, 10)
#     glPopMatrix()
#     glPopMatrix()

#     glPushMatrix()
#     glTranslated(1.0, -2.0, 0.0)
#     glPushMatrix()
#     glScaled(0.0, 0.0, 0.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glRotated(-thigh - 15, 1.0, 0.0, 0.0)
#     glTranslated(0.0, -1.5, 0.0)
#     glPushMatrix()
#     glScaled(1.0, -3.0, 1.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glTranslated(0.0, -1.5, 0.0)
#     glRotated(-shin + 15, 1.0, 0.0, 0.0)
#     glTranslated(0.0, -1.0, 0.0)
#     glPushMatrix()
#     glScaled(1.0, 2.0, 1.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glPopMatrix()

#     glPushMatrix()
#     glTranslated(-1.0, -2.0, 0.0)
#     glPushMatrix()
#     glScaled(0.0, 0.0, 0.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glRotated(thigh - 15, 1.0, 0.0, 0.0)
#     glTranslated(0.0, -1.5, 0.0)
#     glPushMatrix()
#     glScaled(1.0, -3.0, 1.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glTranslated(0.0, -1.5, 0.0)
#     glRotated(shin + 15, 1.0, 0.0, 0.0)
#     glTranslated(0.0, -1.0, 0.0)
#     glPushMatrix()
#     glScaled(1.0, 2.0, 1.0)
#     glutWireCube(1.0)
#     glPopMatrix()
#     glPopMatrix()

#     glPopMatrix()

#     glutSwapBuffers()

# def myReshape(width, height):
#     glViewport(0, 0, width, height)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluPerspective(60.0, width / height, 0.1, 20.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#     gluLookAt(0.0, 0.0, 15.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

# def myKeyboard(key, x, y):
#     global fast
#     if key == b'u':
#         fast = 0.002 - fast
#     elif key == b'\x1b':
#         sys.exit()

# def myIdle():
#     global rad, shoulder, elbow, thigh, shin
#     rad = (rad + 0.0001 + fast) % 2.0
#     shoulder = int(math.sin(rad * math.pi) * 60)
#     elbow = int(-math.sin(rad * math.pi) * 60 - 90)
#     thigh = int(math.sin(rad * math.pi) * 30)
#     shin = int(-math.sin(rad * math.pi) * 30)
#     glutPostRedisplay()

# def main():
#     glutInit()
#     myInit()
#     glutKeyboardFunc(myKeyboard)
#     glutReshapeFunc(myReshape)
#     glutIdleFunc(myIdle)
#     glutDisplayFunc(myDisplay)
#     glutMainLoop()

# if __name__ == "__main__":
#     main()

########################################################################
########################################################################
########################################################################
########################################################################
########################################################################



# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
# import sys
# endF = 0


# def mySetLight():
#     light0_position = [1.0, 1.0, 1.0, 1.0]  # point light source
#     light1_position = [-1.0, -1.0, 1.0, 1.0]  # point light source
#     light1_ambient = [0.0, 0.0, 0.5, 1.0]
#     light1_diffuse = [0.0, 0.0, 1.0, 1.0]
#     light1_specular = [0.0, 0.0, 1.0, 1.0]

#     glLightfv(GL_LIGHT0, GL_POSITION, light0_position)
#     glLightfv(GL_LIGHT1, GL_POSITION, light1_position)
#     glLightfv(GL_LIGHT1, GL_AMBIENT, light1_ambient)
#     glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
#     glLightfv(GL_LIGHT1, GL_SPECULAR, light1_specular)

#     glEnable(GL_LIGHT0)
#     glEnable(GL_LIGHT1)

# def myInit():
#     glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
#     glutInitWindowSize(500, 500)
#     glutInitWindowPosition(0, 0)
#     glutCreateWindow(b"p6-Lights")

#     glClearColor(0.0, 0.0, 0.0, 0.0)
#     glShadeModel(GL_FLAT)

# def myDisplay():
#     mtrl_specular = [1.0, 1.0, 1.0, 1.0]
#     mtrl_shininess = [50.0]

#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glEnable(GL_DEPTH_TEST)
#     glEnable(GL_LIGHTING)

#     glMaterialfv(GL_FRONT, GL_SPECULAR, mtrl_specular)
#     glMaterialfv(GL_FRONT, GL_SHININESS, mtrl_shininess)
#     glutSolidSphere(1.0, 20, 16)
#     glFlush()

# def myReshape(width, height):
#     a = 1.5
#     z = 10.0

#     glViewport(0, 0, width, height)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     if width <= height:
#         glOrtho(-a, a, -a * height / width, a * height / width, -z, z)
#     else:
#         glOrtho(-a * width / height, a * width / height, -a, a, -z, z)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()

# def myKeyboard(key, x, y):
#     if key == b'\x1b':
#         endF += 1
# def myIdle():

#     if endF:
#         sys.exit()


# def main():
#     glutInit(sys.argv)
#     myInit()
#     mySetLight()
#     glutKeyboardFunc(myKeyboard)
#     glutReshapeFunc(myReshape)
#     glutDisplayFunc(myDisplay)
#     glutIdleFunc(myIdle)
#     glutMainLoop()

# if __name__ == "__main__":
#     main()


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

gPitch = 30
gYaw = 30
endF = 0

def mySetLight():
    light0_position = [1.0, 1.0, 1.0, 1.0]


    glLightfv(GL_LIGHT0, GL_POSITION, light0_position)
    glEnable(GL_LIGHT0)
    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    # glLightModelf(GL_LIGHT_MODEL_AMBIENT, [1, 1, 1, 1])

def myInit():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"p6-LightModel")

    glClearColor(0.2, 0.0, 0.3, 1.0)
    glShadeModel(GL_FLAT)

def myDisplay():
    ambient = [0.7, 0.7, 0.7, 1.0]
    diffuse = [0.75, 0.75, 0.75, 1.0]
    specular = [0.25, 0.25, 0.25, 1.0]
    insideface = [1.0, 0.0, 0.0, 1.0]

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)


    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT, GL_SHININESS, 50)
    glMaterialfv(GL_BACK, GL_AMBIENT_AND_DIFFUSE, insideface)
    glMaterialf(GL_BACK, GL_SHININESS, 60)
    # glMaterialfv(GL_BACK, GL_COLOR_INDEXES, [0, 0, 1])


    # glPushMatrix()
    # glRotated(gPitch, 1, 0, 0)
    # glRotated(gYaw, 0, 0, 1)

    # glBegin(GL_QUADS)
    # glNormal3d(0, 0, -1)
    # glVertex3d(-1, -1, -1)
    # glVertex3d(-1, 1, -1)
    # glVertex3d(1, 1, -1)
    # glVertex3d(1, -1, -1)

    # glNormal3d(1, 0, 0)
    # glVertex3d(1, -1, -1)
    # glVertex3d(1, 1, -1)
    # glVertex3d(1, 1, 1)
    # glVertex3d(1, -1, 1)

    # glNormal3d(-1, 0, 0)
    # glVertex3d(-1, -1, -1)
    # glVertex3d(-1, -1, 1)
    # glVertex3d(-1, 1, 1)
    # glVertex3d(-1, 1, -1)

    # glNormal3d(0, 1, 0)
    # glVertex3d(-1, 1, -1)
    # glVertex3d(-1, 1, 1)
    # glVertex3d(1, 1, 1)
    # glVertex3d(1, 1, -1)

    # glNormal3d(0, -1, 0)
    # glVertex3d(-1, -1, -1)
    # glVertex3d(1, -1, -1)
    # glVertex3d(1, -1, 1)
    # glVertex3d(-1, -1, 1)

    # glEnd()

    # glPopMatrix()


    # x = 3.0 / 2
    # y = 4.0 / 2
    # z = 1.0 / 2

    # glPushMatrix()

    # glBegin(GL_QUAD_STRIP)
    # glNormal3d(0, 0, -1)
    # glVertex3d(x, y, -z)
    # glVertex3d(-x, y, -z)
    # glVertex3d(x, -y, -z)
    # glVertex3d(-x, -y, -z)

    # glNormal3d(1, 0, 0)
    # glVertex3d(x, y, z)
    # glVertex3d(x, -y, z)
    # glVertex3d(x, y, -z)
    # glVertex3d(x, -y, -z)

    # glNormal3d(-1, 0, 0)
    # glVertex3d(-x, y, z)
    # glVertex3d(-x, -y, z)
    # glVertex3d(-x, y, -z)
    # glVertex3d(-x, -y, -z)

    # glNormal3d(0, 1, 0)
    # glVertex3d(x, y, z)
    # glVertex3d(-x, y, z)
    # glVertex3d(x, y, -z)
    # glVertex3d(-x, y, -z)

    # glNormal3d(0, -1, 0)
    # glVertex3d(x, -y, z)
    # glVertex3d(-x, -y, z)
    # glVertex3d(x, -y, -z)
    # glVertex3d(-x, -y, -z)

    # glEnd()

    # glPopMatrix()
    glutSwapBuffers()

def myReshape(width, height):
    a = 3.0
    z = 20.0

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if width <= height:
        glOrtho(-a, a, -a * height / width, a * height / width, -z, z)
    else:
        glOrtho(-a * width / height, a * width / height, -a, a, -z, z)
    # gluPerspective(60.0, width / height, -0.01, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def myTimer(value):
    if value == 1:
        glutTimerFunc(30, myTimer, 1)
        global gPitch, gYaw
        gYaw = (gYaw + 2) % 360
        gPitch = (gPitch + 2) % 360
        glutPostRedisplay()

def myKeyboard(key, x, y):
    if key == b'\x1b':
        endF += 1

def myIdle():
    if endF:
        sys.exit()

def main():
    glutInit(sys.argv)
    myInit()
    mySetLight()
    glutKeyboardFunc(myKeyboard)
    glutTimerFunc(30, myTimer, 1)
    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisplay)
    glutIdleFunc(myIdle)
    glutMainLoop()

if __name__ == "__main__":
    main()
