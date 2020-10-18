import numpy as np

class TVertex():
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    
    def getPoints(self):
        return [self.x, self.y, self.z]

    def updateVertex(self, x: int, y: int, z:int):
        self.x = x
        self.y = y
        self.z = z


class TEdge():
    def __init__(self, v1: TVertex, v2: TVertex):
        self.v1 = v1
        self.v2 = v2
    
    def getVertices(self):
        return [self.v1, self.v2]

    def updateEdge(self, v1: TVertex, v2: TVertex):
        self.v1 = v1
        self.v2 = v2


class TSurface():
    def __init__(self, e1: TEdge, e2: TEdge, e3: TEdge, e4: TEdge):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.e4 = e4
    
    def getSurface(self):
        return [self.e1, self.e2, self.e3, self.e4]

class TVertexList():
    def __init__(self):
        self.vertices = []
    
    def addVertex(self, v: TVertex):
        self.vertices.append(v)

    def getVList(self):
        return self.vertices
    

class TEdgeList():
    def __init__(self):
        self.edges = []
    
    def addEdge(self, e: TEdge):
        self.edges.append(e)

    def getEList(self):
        return self.edges

class TSurfaceList():
    def __init__(self):
        self.surfaces = []
    
    def addEdge(self, s: TSurface):
        self.surfaces.append(s)

    def getSList(self):
        return self.surfaces

# Scaling Transformation
def Scale(P, V):
    sx = V[0]
    sy = V[1]
    sz = V[2]
    S = ([sx, 0, 0, 0],
         [0, sy, 0, 0],
         [0, 0, sz, 0],
         [0, 0, 0, 1])
    Point = ([P[0], P[1], P[2], 1])
    res = np.matmul(Point, S)
    return res

# Translation Transformation
def Translate(P, V):
    dx = V[0]
    dy = V[1]
    dz = V[2]
    T = ([1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [-dx, -dy, -dz, 1])
    Point = ([P[0], P[1], P[2], 1])
    res = np.matmul(Point, T)
    return res