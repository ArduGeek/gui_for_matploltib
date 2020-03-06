#!/usr/bin/env python3

from guizero import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

app = App(title="Gui for MatPlotLib", height=400, width=720,layout="grid",bg="white")
app.text_size = 20

def Plot_Sine():
	start = float(array_start.value)
	end = float(array_end.value)
	decimal_step = array_step.value/10
	step = decimal_step
	array = np.arange(start,end,step)
	values = []
	for i in array:
		values.append(np.sin(i))
	plt.plot(array,values)
	plt.axhline(y=0, color="black")
	plt.axvline(x=0, color="black")
	plt.show()
def Plot_Cosine():
	start = float(array_start.value)
	end = float(array_end.value)
	decimal_step = array_step.value/10
	step = decimal_step
	array = np.arange(start,end,step)
	values = []
	for i in array:
		values.append(np.cos(i))
	plt.plot(array,values)
	plt.axhline(y=0, color="black")
	plt.axvline(x=0, color="black")
	plt.show()
def Plot_Tangent():
	start = float(array_start.value)
	end = float(array_end.value)
	decimal_step = array_step.value/10
	step = decimal_step
	array = np.arange(start,end,step)
	values = []
	for i in array:
		values.append(np.tan(i))
	plt.plot(array,values)
	plt.axhline(y=0, color="black")
	plt.axvline(x=0, color="black")
	plt.show()
def Plot_Power():
	power = int(combo.value)
	start = float(array_start.value)
	end = float(array_end.value)
	decimal_step = array_step.value/10
	step = decimal_step
	array = np.arange(start,end,step)
	values = []
	for i in array:
		b = i**power
		values.append(b)
	plt.plot(array,values)
	plt.axhline(y=0, color="black")
	plt.axvline(x=0, color="black")
	plt.show()
def Plot_Sqrt():
	start = float(array_start.value)
	end = float(array_end.value)
	decimal_step = array_step.value/10
	step = decimal_step
	array = np.arange(start,end,step)
	values = []
	for i in array:
		values.append(np.sqrt(i))
	plt.plot(array,values)
	plt.axhline(y=0, color="black")
	plt.axvline(x=0, color="black")
	plt.show()
def Plot_Cbrt():
	start = float(array_start.value)
	end = float(array_end.value)
	decimal_step = array_step.value/10
	step = decimal_step
	array = np.arange(start,end,step)
	values = []
	for i in array:
		values.append(np.cbrt(i))
	plt.plot(array,values)
	plt.axhline(y=0, color="black")
	plt.axvline(x=0, color="black")
	plt.xlabel("array")
	plt.ylabel("values")
	plt.show()
def Plot_Values():
	start = float(array_start.value)
	end = float(array_end.value)
	decimal_step = array_step.value/10
	step = decimal_step
	array = np.arange(start,end,step)
	values = []
	for i in array:
		values.append(i)
	plt.plot(array,values)
	plt.axhline(y=0, color="black")
	plt.axvline(x=0, color="black")
	plt.xlabel("array")
	plt.ylabel("values")
	plt.show()
def Plot_Circle():
	start = float(array_start.value)
	end = float(array_end.value)
	decimal_step = array_step.value/10
	step = decimal_step
	t = np.arange(start,end,step)
	x = []
	y = []
	for i in t:
		x.append(np.cos(i)*10)
	for i in t:
		y.append(np.sin(i)*10)
	plt.plot(x,y)
	plt.axhline(y=0, color="black")
	plt.axvline(x=0, color="black")
	plt.xlabel("array")
	plt.ylabel("values")
	plt.show()
def Plot_Helix():
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	start = float(array_start.value)
	end = float(array_end.value)
	decimal_step = array_step.value/10
	step = decimal_step
	t = np.arange(start,end,step)
	x = []
	y = []
	z = []
	for i in t:
		x.append(np.cos(i)*10)
	for i in t:
		y.append(np.sin(i)*10)
	for i in t:
		z.append(i*2)
	ax.plot(x,y,z)
	plt.show()
def Exit():
	exit()
	

array_start = TextBox(app,grid=[0,0],align="left",width=12)
text1 = Text(app, text="Start of the array",grid=[0,1],align="left")
array_end = TextBox(app,grid=[0,2],align="left",width=12)
text2 = Text(app, text="End of the array",grid=[0,3],align="left")
array_step = Slider(app, start=1, end=10,grid=[0,4])
text3 = Text(app, text="Step of the array\nReal value is\ndivided by 10",grid=[0,5],align="left")
sine_button = PushButton(app, command=Plot_Sine, text="Plot Sine",grid=[1,0],align="left",width=12)
cosine_button = PushButton(app, command=Plot_Cosine, text="Plot Cosine",grid=[1,1],align="left",width=12)
tangent_button = PushButton(app, command=Plot_Tangent, text="Plot Tangent",grid=[1,2],align="left",width=12)
combo = Combo(app, options=["2", "3", "4", "5"],grid=[1,3])
text4 = Text(app, text="Power of plot values",grid=[1,4],align="left")
power_button = PushButton(app, command=Plot_Power, text="Plot Power",grid=[1,5],align="left",width=12)
sqrt_button = PushButton(app, command=Plot_Sqrt, text="Plot Square Root",grid=[2,0],align="left",width=12)
cbrt_button = PushButton(app, command=Plot_Cbrt, text="Plot Cube Root",grid=[2,1],align="left",width=12)
values_button = PushButton(app, command=Plot_Values, text = "Plot Values",grid=[2,2],align="left",width=12)
circle_button = PushButton(app, command=Plot_Circle, text = "Plot Circle",grid=[2,3],align="left",width=12)
helix_button = PushButton(app, command=Plot_Helix, text = "Plot Helix",grid=[2,4],align="left",width=12)
exit_button = PushButton(app, command=Exit, text = "Exit",grid=[2,5],align="left",width=12)
app.display()
