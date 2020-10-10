import math
import numpy as np

V = []
absval = 2
V.append((-absval, absval, absval))
V.append((absval, absval, absval))
V.append((absval, -absval, absval))
V.append((-absval, -absval, absval))
V.append((-absval, absval, -absval))
V.append((absval, absval, -absval))
V.append((absval, -absval, -absval))
V.append((-absval, -absval, -absval))

edges = []
edges.append((V[0], V[1]))
edges.append((V[1], V[2]))
edges.append((V[2], V[3]))
edges.append((V[3], V[0]))

edges.append((V[4], V[5]))
edges.append((V[5], V[6]))
edges.append((V[6], V[7]))
edges.append((V[7], V[4]))

edges.append((V[0], V[4]))
edges.append((V[1], V[5]))
edges.append((V[2], V[6]))
edges.append((V[3], V[7]))

surfaces = []
surfaces.append((edges[0], edges[1], edges[2], edges[3])) # front
surfaces.append((edges[4], edges[5], edges[6], edges[7])) # back
surfaces.append(((edges[8]), edges[4], (V[5], V[1]), (V[1], V[0]))) # top
surfaces.append((edges[11], (V[7], V[6]), (V[6], V[2]), edges[2])) # bottom
surfaces.append((edges[7], (V[4], V[0]), (V[0], V[3]), edges[11])) # left
surfaces.append(((V[2], V[1]), edges[10], edges[6], (V[6], V[2]))) # right

# Line yg mau di clip
P1 = (-3, -3, 3)
P2 = (3, 1, 1)

# N vector is (-dy, dx) for left and (dy, -dx) for right

# parametric line equation C = A + t * (B - A)
def parametriclineequation(A, B, t):
    Cx = A[0] + (t * (B[0] - A[0]))
    Cy = A[1] + (t * (B[1] - A[1]))
    C = (Cx, Cy)
    return C

# t
def findt(A, B, P, N):
    AP = np.subtract(P, A)
    AB = np.subtract(B, A)

    t = np.matmul(AP, N) / np.matmul(AB, N)
    return t

# front surface dulu deh
frontedges = surfaces[0]

entering = []
leaving = []

clippedA = None
clippedB = None

for i in range(len(frontedges)):
    e = frontedges[i]
    p1 = e[0]
    p1 = (p1[0], p1[1])
    p2 = e[1]
    p2 = (p2[0], p2[1])
    dy = p2[1] - p1[1]
    dx = p2[0] - p1[0]

    N = ([dy, -dx])

    A = ([P1[0], P1[1]])
    B = ([P2[0], P2[1]])
    P = p2

    f = np.matmul(np.subtract(A, p1), N)
    # if(f > 0): print('A is inside edge ' + str(i + 1))
    # elif(f < 0): print('A is outside edge ' + str(i + 1))
    # else: print('A is on edge ' + str(i + 1))

    f2 = np.matmul(np.subtract(B, p1), N)
    # if(f2 > 0): print('B is inside edge ' + str(i + 1))
    # elif(f2 < 0): print('B is outside edge ' + str(i + 1))
    # else: print('B is on edge ' + str(i + 1))

    if(f > 0 and f2 > 0):
        print('trivially accepted')
    elif(f < 0 and f2 < 0):
        print('trivially rejected')
    else:
        print('perform clipping')

        if(f < 0 and f2 > 0):
            print('entering')

            t = findt(A, B, P, N)

            print('t found at: ' + str(t))
            entering.append(t)

            C = parametriclineequation(A, B, t)
            A = C
            clippedA = A
            print(C)
        elif(f > 0 and f2 < 0):
            print('leaving')

            AP = np.subtract(A, P)
            AB = np.subtract(A, B)

            t = np.matmul(AP, N) / np.matmul(AB, N)

            print('t found at: ' + str(t))
            leaving.append(t)

            C = parametriclineequation(A, B, t)
            B = C
            clippedB = B
        elif(f == 0 or f2 == 0):
            print('on edge')
        else:
            print('none of the above')

# max t for entering = te
# min t for leaving = tl

te = max(entering)
tl = min(leaving)

if(te <= tl):
    print('AB accepted')
    print('A = ' + str(P1))
    print('B = ' + str(P2))
    print('A prime = ' + str(clippedA))
    print('B prime = ' + str(clippedB))
elif(te > tl):
    print('AB rejected')