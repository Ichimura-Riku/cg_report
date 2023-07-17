import sys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

imageWidth = 256
imageHeight = 256
texImage = np.zeros((imageHeight, imageWidth, 3), dtype=np.uint8)

def readPPMImage(filename):
    with open(filename, 'rb') as fp:
        # header = fp.readline().decode('utf-8').strip()
        # if header != 'P6':
        #     print(f'Invalid PPM file: {filename}')
        #     sys.exit(1)
        # size = fp.readline().decode('utf-8').strip().split()
        # width, height = int(size[0]), int(size[1])
        # max_val = int(fp.readline().decode('utf-8').strip())

        # if width != imageWidth or height != imageHeight or max_val != 255:
        #     print(f'Invalid image dimensions or color range: {filename}')
        #     sys.exit(1)

        data = fp.read()
        image = Image.frombytes('RGB', (imageWidth, imageHeight), data)
        texImage[:] = np.array(image)


def setUpTexture():
    readPPMImage("texture1.ppm")
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imageWidth, imageHeight, 0, GL_RGB, GL_UNSIGNED_BYTE, texImage)

def myInit():
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"p7-textureTile")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)

def myDisplay():
    tc = 1.0
    p0 = [-2.0, -1.0, 0.0]
    p1 = [-2.0, 1.0, 0.0]
    p2 = [0.0, 1.0, 0.0]
    p3 = [0.0, -1.0, 0.0]

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)

    glBegin(GL_QUADS)
    glTexCoord2d(0.0, 0.0)
    glVertex3dv(p0)
    glTexCoord2d(0.0, tc)
    glVertex3dv(p1)
    glTexCoord2d(tc, tc)
    glVertex3dv(p2)
    glTexCoord2d(tc, 0.0)
    glVertex3dv(p3)

    glTexCoord2d(0.0, 0.0)
    glVertex3d(1.0, -1.0, 0.0)
    glTexCoord2d(0.0, 1.0)
    glVertex3d(1.0, 1.0, 0.0)
    glTexCoord2d(1.0, 1.0)
    glVertex3d(2.41421, 1.0, -1.41421)
    glTexCoord2d(1.0, 0.0)
    glVertex3d(2.41421, -1.0, -1.41421)
    glEnd()

    glFlush()
    glDisable(GL_TEXTURE_2D)

def myReshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, width / height, 0.1, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslated(0.0, 0.0, -3.6)

def myKeyboard(key, x, y):
    if key == b'\x1b':
        sys.exit(0)

def main():
    glutInit(sys.argv)
    myInit()
    setUpTexture()
    glutKeyboardFunc(myKeyboard)
    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisplay)
    glutMainLoop()

if __name__ == '__main__':
    main()
