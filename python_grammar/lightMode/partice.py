#coding:utf-8
 
import sys
from math import pi as PI
from math import sin, cos
from math import sqrt
 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
#将指定为三个坐标组的法线向量换算。
def ReduceToUnit(vector): 
	# 计算向量长度
	length = sqrt((vector[0]*vector[0]) + (vector[1]*vector[1]) +(vector[2]*vector[2]));
	#防止计算值太接近0
	if (length == 0.0):
		length = 1.0 
	#按长度划分每个元素将得到单位法线向量
	vector[0] /= length 
	vector[1] /= length 
	vector[2] /= length 
 
# 按逆时针方向指定点p1,p2,p3
def calcNormal(v,out):
	v1=[0.0 for i in range(3)]
	v2=[0.0 for i in range(3)]
	out=[0.0 for i in range(3)]	
	xx = 0 
	yy = 1
	zz = 2
 
	# 计算两个向量
	v1[xx] = v[0][xx] - v[1][xx] 
	v1[yy] = v[0][yy] - v[1][yy] 
	v1[zz] = v[0][zz] - v[1][zz] 
 
	v2[xx] = v[1][xx] - v[2][xx] 
	v2[yy] = v[1][yy] - v[2][yy] 
	v2[zz] = v[1][zz] - v[2][zz] 
 
	# 取两个向量的叉积
	out[xx] = v1[yy]*v2[zz] - v1[zz]*v2[yy] 
	out[yy] = v1[zz]*v2[xx] - v1[xx]*v2[zz] 
	out[zz] = v1[xx]*v2[yy] - v1[yy]*v2[xx] 
 
	# 矢量归一化
	ReduceToUnit(out) 
 
def RenderHead():
	global x,y,angle	# 计算位置


	height = 25.0
	diameter = 30.0
	#存储顶点和法线
	corners = [[0.0 for i in range(3)] for i in range(4)]
	normal=[0.0 for i in range(3)]
	step = (PI/3.0)     # 步长设为６０度
    
	# 设置材料颜色
	glColor3f(0.0, 0.0, 0.7) 
 
    # -----开始一个三角形扇面覆盖顶面------
	glFrontFace(GL_CCW)
	glBegin(GL_TRIANGLE_FAN)
	#所有顶部的法线都垂直于Ｚ轴
	glNormal3f(0.0, 0.0, 1.0)
	#八面体中心在原点上
	glVertex3f(0.0, 0.0, height/2.0)

	#把圆圈分成6个部分，然后开始下降点来绘制扇面.  避免使用glFrontFace()进行状态改变
	# 第一个和最后一个顶点封闭扇面
	glVertex3f(0.0, diameter, height/2.0)

	angle=(2.0*PI)-step
	while angle>1 :
		#计算下一个向量的x,y
		x = diameter* sin(angle)
		y = diameter* cos(angle)
		#指定三角形扇形的下一个顶点
		glVertex3f(x, y, height/2.0)
		angle-=step

	# 最后一个顶点闭合扇面
	glVertex3f(0.0, diameter, height/2.0)
	glEnd()
 
    # 开始一个三角形扇面覆盖底面
	glBegin(GL_TRIANGLE_FAN)
 
	glNormal3f(0.0, 0.0, -1.0)
	glVertex3f(0.0, 0.0, -height/2.0)
 
	angle=0
	while angle < (2.0*PI)-step :
		x = diameter* sin(angle)
		y = diameter* cos(angle)
		glVertex3f(x, y, -height/2.0)
		angle+=step

	glVertex3f(0.0, diameter, -height/2.0)
	glEnd()
 
    #开始一个四角形覆盖侧面
	glBegin(GL_QUADS)
	angle=0
	while angle<(2.0*PI)-step :
		x = diameter* sin(angle)
		y = diameter* cos(angle)              
		#从上面的底部开始
		corners[0][0] = x
		corners[0][1] = y
		corners[0][2] = -height/2.0
 
		#顶到头部
		corners[1][0] = x
		corners[1][1] = y
		corners[1][2] = height/2.0
 
		#计算下一个十六进制点
		x = diameter* sin(angle+step) 
		y = diameter* cos(angle+step) 
 
		#确保在绘制之前没有绘制过
		if (angle+step < 3.1415*2.0):
			#如果已经绘制过了,则在已知点上闭合即可
			corners[2][0] = x
			corners[2][1] = y
			corners[2][2] = height/2.0
 
			corners[3][0] = x
			corners[3][1] = y 
			corners[3][2] = -height/2.0 
		else:
			corners[2][0] = 0.0 
			corners[2][1] = diameter 
			corners[2][2] = height/2.0 
 
			corners[3][0] = 0.0 
			corners[3][1] = diameter 
			corners[3][2] = -height/2.0 
 
		calcNormal(corners, normal) 
		glNormal3fv(normal) 
        
		glVertex3fv(corners[0])
		glVertex3fv(corners[1])
		glVertex3fv(corners[2])
		glVertex3fv(corners[3])
		angle+=step
				
	glEnd() 
 
 
 
def RenderScene():
	global xRot,yRot
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)					
 
	# 保存矩阵状态
	glMatrixMode(GL_MODELVIEW) 
	glPushMatrix() 
    # 绕X轴和Y轴旋转(角度,x,y,z)
	glRotatef(xRot, 1.0, 0.0, 0.0)
	glRotatef(yRot, 0.0, 0.0, 1.0)	
	#只渲染上部
	RenderHead()
	glPopMatrix()
	glutSwapBuffers()					
 
#设置渲染状态
def SetupRC():	
	#光照的值和坐标；环境光，漫射光，镜面光，光的坐标,
	ambientLight = [0.4, 0.4, 0.4, 1.0 ]
	diffuseLight = [0.7, 0.7, 0.7, 1.0 ]
	specular = [ 0.9, 0.9, 0.9, 1.0]
	lightPos = [ -50.0, 200.0, 200.0, 1.0]
	specref =  [ 0.6, 0.6, 0.6, 1.0]
 
 
	glEnable(GL_DEPTH_TEST)	# 去除隐藏面
	glEnable(GL_CULL_FACE)	# 不计算八面体的内部
	glFrontFace(GL_CCW) 
	
	glEnable(GL_LIGHTING) 
 
	# 设置光照
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT,ambientLight) 
	glLightfv(GL_LIGHT0,GL_AMBIENT,ambientLight) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,diffuseLight) 
	glLightfv(GL_LIGHT0,GL_SPECULAR,specular) 
 
	#设置光的位置并设置光照为开启状态
	glLightfv(GL_LIGHT0,GL_POSITION,lightPos) 
	glEnable(GL_LIGHT0) 
 
	# 启用颜色跟踪
	glEnable(GL_COLOR_MATERIAL) 
	
	# 设置材料属性跟随GLULL值
	glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE) 

 	#所有材料都具有完全的镜面反射率,中等亮度
	glMaterialfv(GL_FRONT, GL_SPECULAR,specref)
	glMateriali(GL_FRONT,GL_SHININESS,64) 
	
	glClearColor(0.0, 0.0, 0.0, 1.0)  #背景置为黑色
	
 
#改变窗口大小时调用
def ChangeSize(w,h):
	nRange = 100.0
	if(h == 0):     #防止除数为0
		h = 1
	glViewport(0, 0, w, h)						#设置视区大小
	glMatrixMode(GL_PROJECTION)					#投影矩阵模式
	glLoadIdentity()							#矩阵堆栈清空
	#设置裁剪窗口大小
	if (w <= h): 
		glOrtho (-nRange, nRange, -nRange*h/w, nRange*h/w, -nRange*2.0, nRange*2.0)	
	else: 
		glOrtho (-nRange*w/h, nRange*w/h, -nRange, nRange, -nRange*2.0, nRange*2.0)	
						
	glMatrixMode(GL_MODELVIEW)					#模型矩阵模式
	glLoadIdentity()
 
def SpecialKeys(key,x,y):
	global xRot,yRot
	if(key == GLUT_KEY_UP):
		xRot-= 5.0
	if(key == GLUT_KEY_DOWN):
		xRot += 5.0
	if(key == GLUT_KEY_LEFT):
		yRot -= 5.0
	if(key == GLUT_KEY_RIGHT):
		yRot += 5.0
	if(key > 356.0):
		xRot = 0.0
	if(key < -1.0):
		xRot = 355.0
	if(key > 356.0):
		yRot = 0.0
	if(key < -1.0):
		yRot = 355.0
	glutPostRedisplay()
 
xRot=0.0
yRot=0.0
print("按箭头键改变视角,查看光照！")
#使用glut初始化OpenGL
glutInit()
glutInitWindowSize(700,700)
#设置显示模式；（双缓冲）
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB| GLUT_DEPTH)
glutCreateWindow("光照模型")
 
glutReshapeFunc(ChangeSize)
glutSpecialFunc(SpecialKeys)     #注册键盘回调函数
#调用函数绘制图像
glutDisplayFunc(RenderScene)
SetupRC()
#主循环
glutMainLoop()
 
