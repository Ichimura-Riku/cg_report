/* p7-textureTile.c
 * An image in PPM format as texture is mapped onto the flat planes.
 * 
 */
#include <stdio.h>
#include <GL/glut.h>

#define	imageWidth 256
#define	imageHeight 256

unsigned char texImage[imageHeight][imageWidth][3];

void readPPMImage(char* filename)
{
	FILE *fp;
	int  ch, i;

	if (fopen_s(&fp,filename, "r") != 0){
    	fprintf(stderr, "Cannot open ppm file %s\n",filename);
		exit(1);
	}
	for (i = 0; i < 4; i++){ 						// skip four in header
    	while (1){
			if ((ch = fgetc(fp)) != '#') break;		// skip comment
			fgets((char*)texImage, 1024, fp);   	// dummy read
			while(isspace(ch)) ch = fgetc(fp);  	// skip space
    	}
    	while (!isspace(ch)) ch = fgetc(fp);		// read header
/* Newline or other single terminator after header may exist. */
		if (i < 3){
			while (isspace(ch)) ch = fgetc(fp);		// skip terminator
		}
	}
	fread(texImage, 1, imageWidth*imageHeight*3, fp);	// read RGB data
	fclose(fp);
}

void setUpTexture(void)
{
	readPPMImage("texture2.ppm");
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imageWidth, imageHeight, 
					0, GL_RGB, GL_UNSIGNED_BYTE, texImage);
}

void myInit(char *progname)
{    
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(0, 0);
	glutCreateWindow(progname);
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glShadeModel(GL_SMOOTH);
	glEnable(GL_DEPTH_TEST);
}

void myDisplay(void)
{
	double	tc = 2.0;
	double	p0[]={-2.0, -1.0, 0.0}, p1[]={-2.0, 1.0, 0.0},
			p2[]={0.0, 1.0, 0.0},   p3[]={0.0, -1.0, 0.0};
	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glEnable(GL_TEXTURE_2D);
	
	glBegin(GL_QUADS);
	glTexCoord2d(0.0, 0.0); glVertex3dv(p0);
	glTexCoord2d(0.0, tc ); glVertex3dv(p1);
	glTexCoord2d(tc , tc ); glVertex3dv(p2);
	glTexCoord2d(tc , 0.0); glVertex3dv(p3);

	glTexCoord2d(0.0, 0.0); glVertex3d(1.0, -1.0, 0.0);
	glTexCoord2d(0.0, 1.0); glVertex3d(1.0, 1.0, 0.0);
	glTexCoord2d(1.0, 1.0); glVertex3d(2.41421, 1.0, -1.41421);
	glTexCoord2d(1.0, 0.0); glVertex3d(2.41421, -1.0, -1.41421);
	glEnd();

	glFlush();
	glDisable(GL_TEXTURE_2D);
}

void myReshape(int width, int height)
{
	glViewport(0, 0, width, height);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(60.0, (double)width / (double)height, 0.1, 20.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslated(0.0, 0.0, -3.6);
}

void myKeyboard(unsigned char key, int x, int y)
{
	if (key == 27 ) exit (0);
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	myInit(argv[0]);
	setUpTexture();
	glutKeyboardFunc(myKeyboard);
	glutReshapeFunc(myReshape);
	glutDisplayFunc(myDisplay);
	glutMainLoop();
	return 0; 
}
