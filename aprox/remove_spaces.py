import numpy as np

def rm(x, y, eps, delta):
	x = list(x)
	y = list(y)
	ans = [[(x.pop(0), y.pop(0)), (x.pop(0), y.pop(0))]]
	while len(x):
		x_pp, y_pp = ans[-1][-2]
		x_p, y_p = ans[-1][-1]
		x_now, y_now = x.pop(0), y.pop(0)
		if ( find_angle(y_p, y_pp) - (x_pp - x_p) + np.pi - find_angle(y_now, y_p) > eps) and (x_now - x_p < delta):
			ans[-1].append((x_now, y_now)) 
		else:
			ans.append([(x_now, y_now), (x.pop(0), y.pop(0))])
	return ans


def find_angle(r1, r2):
	return (1. - np.fabs(r2 - r1)) * np.pi / 2