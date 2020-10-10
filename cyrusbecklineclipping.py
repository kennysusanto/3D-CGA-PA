import math
import numpy as np

V = []
absval = 2
# ikuti urutan vertex ini (kiri atas depan startnya, counter-clockwise)
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
# ikutin urutan edges ini
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


def cyrusbeck(P1, P2, V, E, S):
    # P1 & P2 are the points of the line we'd like to clip
    # V is the vertices of the object
    # E is the edges of the object
    # S is the surfaces of the object
    # urutan surface = front, back, top, bottom, left, right (dilihat dari z+)

    for s in range(len(S)):
        surfaceedges = S[s]

        entering = []
        leaving = []
        
        A = None
        B = None

        surfacedict = {0:'front', 1:'back', 2:'top', 3:'bottom', 4:'left', 5:'right'}

        print('\nsurface: ' + surfacedict[s])

        if(s == 0 or s == 1):
            A = ([P1[0], P1[1]])
            B = ([P2[0], P2[1]])
        elif(s == 2 or s == 3): 
            A = ([P1[0], P1[2]])
            B = ([P2[0], P2[2]])
        elif(s == 4 or s == 5):
            A = ([P1[2], P1[1]])
            B = ([P2[2], P2[1]])
        

        for i in range(len(surfaceedges)):
            e = surfaceedges[i]
            ep1 = e[0]
            ep1 = (ep1[0], ep1[1])
            ep2 = e[1]
            ep2 = (ep2[0], ep2[1])
            dy = ep2[1] - ep1[1]
            dx = ep2[0] - ep1[0]

            N = ([dy, -dx])
            # print('N: ' + str(N))

            P = ep2

            f = np.matmul(np.subtract(A, ep1), N)
            # if(f > 0): print('A is inside edge ' + str(i + 1))
            # elif(f < 0): print('A is outside edge ' + str(i + 1))
            # else: print('A is on edge ' + str(i + 1))

            f2 = np.matmul(np.subtract(B, ep1), N)
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
                    # print('entering')

                    t = findt(A, B, P, N)

                    # print('t found at: ' + str(t))
                    entering.append(t)

                    C = parametriclineequation(A, B, t)
                    
                    if(N[0] != 0):
                        C = (C[0], A[1] )
                    elif(N[1] != 0):
                        C = (A[0], C[1])
                    
                    Cv = ([C[0], C[1]])
                    A = Cv
                    # enteringC.append(C)
                    # print(A)
                    # print(B)
                elif(f > 0 and f2 < 0):
                    # print('leaving')

                    AP = np.subtract(A, P)
                    AB = np.subtract(A, B)

                    t = np.matmul(AP, N) / np.matmul(AB, N)

                    # print('t found at: ' + str(t))
                    leaving.append(t)

                    C = parametriclineequation(A, B, t)
                    
                    if(N[0] != 0):
                        C = (C[0], B[1])
                    elif(N[1] != 0):
                        C = (B[0], C[1])

                    Cv = ([C[0], C[1]])
                    B = Cv
                    # leavingC.append(C)
                    # print(A)
                    # print(B)
                elif(f == 0 or f2 == 0):
                    print('on edge')
                else:
                    print('none of the above')
            

        # max t for entering = te
        # min t for leaving = tl

        if(len(entering) < 1):
            te = 0
        elif(len(leaving) < 1):
            tl = 0
        else:
            te = max(entering)
            tl = min(leaving)

        # enteringdict = dict(zip(entering, enteringC))
        # leavingdict = dict(zip(leaving, leavingC))

        # print(enteringdict[te])
        # print(leavingdict[tl])

        if(te <= tl):
            print('AB accepted')
            print('A = ' + str(P1))
            print('B = ' + str(P2))
            print('A prime = ' + str(A))
            print('B prime = ' + str(B))
        elif(te > tl):
            print('AB rejected')
        else:
            print('AB accepted no clipping')

cyrusbeck(P1, P2, V, edges, surfaces)