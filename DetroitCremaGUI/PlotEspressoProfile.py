import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import os

class ProfilePlot:
	def __init__(self):
		super().__init__()
		self.time = np.array([0,0,0,0,0,0,0])
		self.pressure = np.array([0,0,0,0,0,0,0])
		self.touch_dpi = 133
		self.graph_width = 800
		self.graph_height = 350
		self.interpolate_list = []
		if os.path.isfile("BrewGraph.png"):
			print('Removing Previous Graph Pic')
			os.remove("BrewGraph.png")
	def create_plot(self, time, pressure):
		self.time = np.array(time)
		self.pressure = np.array(pressure)
		self.y_data = interp1d(self.time, self.pressure)
		for i in range(100000):
			try:
				self.interpolate_list.append(self.y_data[i])
			except:
				break
		fig = plt.figure(figsize = (self.graph_width/self.touch_dpi, self.graph_height/self.touch_dpi), dpi = self.touch_dpi, facecolor = '#04043B')
		ax = fig.add_subplot(111)
		ax.set_facecolor('#04043B')
		ax.set_xlabel('Time (sec)')
		ax.set_ylabel('Pressure (Bar)')
		ax.xaxis.label.set_color('#ff8c00')
		ax.yaxis.label.set_color('#ff8c00')
		ax.tick_params(axis = 'x', colors = '#ff8c00')
		ax.tick_params(axis = 'y', colors = '#ff8c00')
		ax.spines['left'].set_visible(False)
		ax.spines['right'].set_visible(False)
		ax.spines['top'].set_visible(False)
		ax.spines['bottom'].set_visible(False)
		#default_x_ticks = range(len(time))
		#plt.xticks(default_x_ticks, time)
		plt.plot(self.time,self.pressure, color = '#ff8c00', marker = 'o', label = "Desired Pressure")
		
		
		
		if os.path.isfile("BrewGraph.png"):
			print('Removing Previous Graph Pic')
			os.remove("BrewGraph.png")
		plt.savefig("BrewGraph.png")
		#plt.show()
	def getPressureTarg(self, elapsedTime):
		self.val = self.y_data(elapsedTime)
		return self.val

#p = ProfilePlot()
#p.create_plot([0,8,10,20,30,40,50], [2,2,3,5,6,3,0])
