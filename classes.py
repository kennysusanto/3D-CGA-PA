import math
import numpy as np

class TPoint():
    def __init__(x, y, z):
        self.x = x
        self.y = y
        self.z = z


class TLine():
    def __init__(x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

# Orthographic Vt
# Pr1 (Projection 1)
fmat = ([1, 0, 0, 0],
	   [0, 1, 0, 0], 
	   [0, 0, 1, 0],
	   [0, 0, 0, 1]) # Front x'=x, y'=y, z'=z

rrmat = ([-1, 0, 0, 0],
		 [0, 1, 0, 0],
		 [0, 0, -1, 0],
		 [0, 0, 0, 1]) # Rear x'=-x, y'=y, z'=-z

lmat = ([0, 0, -1, 0],
	    [0, 1, 0, 0], 
	    [1, 0, 0, 0],
	    [0, 0, 0, 1]) # Left x'=z, y'=y, z'=-x

rmat = ([0, 0, 1, 0],
	    [0, 1, 0, 0], 
	    [-1, 0, 0, 0],
	    [0, 0, 0, 1]) # Right x'=-z, y'=y, z'=x

tmat = ([1, 0, 0, 0],
	    [0, 0, 1, 0], 
	    [0, -1, 0, 0],
	    [0, 0, 0, 1]) # Top x'=x, y'=-z, z'=y

bmat = ([1, 0, 0, 0],
	    [0, 0, -1, 0], 
	    [0, 1, 0, 0],
	    [0, 0, 0, 1]) # Bottom x'=x, y'=z, z'=-y

# Pr2 (Projection 2)
pr2mat = ([1, 0, 0, 0], 
		  [0, 1, 0, 0], 
		  [0, 0, 0, 0], 
		  [0, 0, 0, 1])

def pr1pr2(objmat, pr1):
    res = np.matmul(pr1, pr2mat)
    res = np.matmul(objmat, res)
    return res

def getVtort(objmat, side):
    res = []
    sides = ['front', 'rear', 'left', 'right', 'top', 'bottom']
    res[0] = pr1pr2(objmat, fmat)
    res[1] = pr1pr2(objmat, rrmat)
    res[2] = pr1pr2(objmat, lmat)
    res[3] = pr1pr2(objmat, rmat)
    res[4] = pr1pr2(objmat, tmat)
    res[5] = pr1pr2(objmat, bmat)
    
    idx = sides.index(side)
    return res[idx]

# Axonometric Vt
def getVtaxo(objmat, vi, teta):
    vt = ([math.cos(math.radians(vi)), math.sin(math.radians(alfa))*math.sin(math.radians(teta)), 0, 0],
          [0, math.cos(math.radians(teta)), 0, 0],
          [math.cos(math.radians(vi)), -(math.cos(math.radians(alfa))*math.sin(math.radians(teta))), 0, 0],
          [0, 0, 0, 1])
    res = np.matmul(objmat, pr2)
    return res

# Oblique Vt
def getVtobl(objmat, vi, alfa):
    vt = ([1, 0, 0, 0],
          [0, 1, 0, 0],
          [math.cot(math.radians(vi))*math.cos(math.radians(alfa)), math.cot(math.radians(vi))*math.sin(math.radians(alfa)), 0, 0],
          [0, 0, 0, 1])
    res = np.matmul(objmat, vt)
    return res

# Scale Transformation
def Scale(P, V):
    S = ([V[0], 0, 0, 0],
         [0, V[1], 0, 0],
         [0, 0, V[2], 0],
         [0, 0, 0, 1])
    Point = ([P[0]],
             [P[1]],
             [P[2]],
             [1])
    res = np.matmul(S, Point)
    return res
