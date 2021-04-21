import pickle
import numpy as np
from scipy.interpolate import interp1d

def find_delta(y1, y2, y3):
	return np.fabs(y3 + y1 - 2*y2)

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
	
	def load(self, path = 'data/data.pickle', step = 1, frame = 1):
		with open(path, 'rb') as f:
			rest = pickle.load(f)
		for _ in range(frame):
			try:
				d = rest.pop(0)
			except:
				break
		self.x = []
		self.y = []
		for i, j in zip(*d):
			self.x.append(np.deg2rad(i))
			self.y.append(j)
		self.x = self.x[::step]
		self.y = self.y[::step]
		return rest

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y
	
	def get_coord(self, i):
		return self.x[i], self.y[i]

	def part(self, start, stop):
		return Data(self.x[start : stop], self.y[start : stop])

	def interpolate(self):
		try:
			f = interp1d(self.x, self.y)
		except Exception as e:
			print(e.__class__)
			return self
		xi = np.linspace(self.x[0], self.x[-1], num=1000)
		return Data(xi, f(xi))

	def split(self, delta, eps):
		ans = [self.part(0, 1)]
		for i in range(1, len(self.x) - 1):
			_, y1 = self.get_coord(i - 1)
			x2, y2 = self.get_coord(i)
			x3, y3 = self.get_coord(i + 1)
			_delta = find_delta(y1, y2, y3)
			_eps = np.fabs(x3 - x2)
			if _delta > delta or _eps < eps:
				ans.append(Data([x2, x3], [y2, y3]))
				# print('appended')
			else:
				ans[-1].add(x2, y2)
				# print('added')
		ans[-1].add(self.x[-1], self.y[-1])
		return ans


class DataArray:
	arr = []
	def __init__(self, array, eps=1e-4, delta=np.pi / 10):
		if type(array) != Data:
			self.arr = array
		else:
			self.arr = array.split(delta, eps)
	def __str__(self):
		return '\n'.join(list(map(str, self.arr)))

	def length(self):
		return len(self.arr)
	
	def interpolate(self):
		self.arr = list(map(Data.interpolate, self.arr))

	def get_data_arr(self):
		return self.arr.copy()