import pickle
import numpy as np
from scipy.interpolate import interp1d

class Data:
	def __init__(self, xi = [], yi = []):
		self.x = xi
		self.y = yi
	
	def __str__(self):
		return f"""
[{self.x[0]:.2f},\t{self.y[0]:.2f}]
[{self.x[1]:.2f},\t{self.y[1]:.2f}]
   . . .
[{self.x[-2]:.2f},\t{self.y[-2]:.2f}]
[{self.x[-1]:.2f},\t{self.y[-1]:.2f}]
"""
	def add(self, x, y):
		self.x.append(x)
		self.y.append(y)
	
	def load(self, path = '/home/l15k4/programs/coursework2/data/data.pickle'):
		with open(path, 'rb') as f:
			rest = pickle.load(f)
		d = rest.pop(0)
		self.x = []
		self.y = []
		for i, j in zip(*d):
			self.x.append(np.deg2rad(i))
			self.y.append(j)
		return rest

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def intrpolate(self):
		try:
			f = interp1d(self.x, self.y)
		except Exception as e:
			print(e.__class__)
			return self
		xi = np.linspace(self.x[0], self.x[-1], num=1000)
		return Data(xi, f(xi))