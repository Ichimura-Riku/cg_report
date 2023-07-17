import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Constants
Dt = 33
Coeff_Of_Restitution = 0.5
Frame_Counter_Max = 50
Table_Width = 1.27
Table_Height = 2.54
Ball_Radius = 0.04
Image_Width = 256
Image_Height = 256
startStopFlag = None
texImage = [[[[], [], []] for j in range(Image_Width)] for i in range(Image_Height)]


# Class CBall
class CBall:
    def set(self, x, y, z, radius, theta, velocity):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.theta = math.radians(theta)
        self.velocity = velocity
        self.ambient = [1.0, 0.0, 0.0, 1.0]
        self.diffuse = [0.6, 0.1, 0.1, 1.0]
        self.specular = [1.0, 1.0, 1.0, 1.0]
        self.shininess = 128.0

    def step(self):
        c = 0.0005
        self.x -= c * Dt * self.velocity * math.sin(self.theta)
        self.z -= c * Dt * self.velocity * math.cos(self.theta)

    def draw(self):
        glMaterialfv(GL_FRONT, GL_AMBIENT, self.ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.specular)
        glMaterialf(GL_FRONT, GL_SHININESS, self.shininess)

        glPushMatrix()
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glTranslated(self.x, self.y, self.z)
        glutSolidSphere(self.radius, 20, 20)
        glDisable(GL_LIGHTING)
        glDisable(GL_DEPTH_TEST)
        glPopMatrix()

def checkForCollision():
    global ball1, ball2
    dx = ball1.x - ball2.x
    dz = ball1.z - ball2.z
    d = math.sqrt(dx * dx + dz * dz)

    if d <= (ball1.radius + ball2.radius):
        ball2.theta = math.asin(ball1.x / (2 * ball1.radius))
        ball1.theta = ball2.theta - math.pi / 2
        ball2.velocity = 0.5 * ball1.velocity * (1.0 + Coeff_Of_Restitution)
        ball1.velocity = 0.5 * ball1.velocity * (1.0 - Coeff_Of_Restitution)

def mySetUpBall():
    global ball1, ball2
    ball1 = CBall()
    ball1.set(0.04, Ball_Radius, -0.1, Ball_Radius, 0.0, 2.0)

    ball2 = CBall()
    ball2.set(0.0, Ball_Radius, -0.5, Ball_Radius, 0.0, 0.0)
    ball2.diffuse = [0.0, 0.0, 0.2, 1.0]

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

def mySetUpTexture():
    texGreenSheet = "texGreenSheet.ppm"
    readPPMImage(texGreenSheet)

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, Image_Width, Image_Height, 0, GL_RGB, GL_UNSIGNED_BYTE, texImage)

def greenCloth():
    p0 = [-(Table_Width / 2.0), 0.0, 0.0]
    p1 = [(Table_Width / 2.0), 0.0, 0.0]
    p2 = [(Table_Width / 2.0), 0.0, -Table_Height]
    p3 = [-(Table_Width / 2.0), 0.0, -Table_Height]

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3fv(p0)
    glTexCoord2f(2.0, 0.0)
    glVertex3fv(p1)
    glTexCoord2f(2.0, 2.0)
    glVertex3fv(p2)
    glTexCoord2f(0.0, 2.0)
    glVertex3fv(p3)
    glEnd()

def myDisplay():
    global ball1, ball2
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)

    greenCloth()
    glDisable(GL_TEXTURE_2D)

    glPushMatrix()

    ball1.step()
    ball2.step()
    checkForCollision()
    ball1.draw()
    ball2.draw()

    glPopMatrix()
    glutSwapBuffers()
    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)

def myReshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, width / height, 0.1, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.4, 0.5, 0.0, 0.0, -0.6, 0.0, 1.0, 0.0)

def myTimer(value):
    if value == 1:
        glutTimerFunc(Dt, myTimer, 1)
    if startStopFlag:
        glutPostRedisplay()
        global frameCounter
        frameCounter += 1
        if frameCounter >= Frame_Counter_Max:

            startStopFlag = 0

def myKeyboard(key, x, y):
    global startStopFlag
    if key == b'g':
        startStopFlag = 1
    elif key == b'\x1b':
        exit(0)

def mySetLight():
    lightPos0 = [0.0, 1.0, -0.2, 0.0]
    diffuse0 = [0.5, 0.5, 0.5, 1.0]
    specular0 = [0.2, 0.2, 0.2, 1.0]

    lightPos = [0.0, 1.0, -0.2, 1.0]
    spotDir = [0.0, -1.0, -0.5]
    ambient = [0.2, 0.2, 0.2, 1.0]
    diffuse = [1.0, 1.0, 1.0, 1.0]
    specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT1, GL_POSITION, lightPos0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse0)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular0)

    glLightfv(GL_LIGHT1, GL_POSITION, lightPos)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, spotDir)
    glLightfv(GL_LIGHT1, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, specular)
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 30.0)
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 2.0)

    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

def myInit(progname):
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(progname)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_NORMALIZE)
    glEnable(GL_AUTO_NORMAL)

def main():
    global startStopFlag, frameCounter
    startStopFlag = 0
    frameCounter = 0

    glutInit(sys.argv)
    myInit(b"Billiard")
    glutKeyboardFunc(myKeyboard)
    glutTimerFunc(Dt, myTimer, 1)
    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisplay)
    mySetLight()
    mySetUpBall()
    mySetUpTexture()

    glutMainLoop()

if __name__ == "__main__":
    main()
