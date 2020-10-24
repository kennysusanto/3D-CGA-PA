import math
import numpy as np

# N vector is (-dy, dx) for left and (dy, -dx) for right

# parametric line equation C = A + t * (B - A)
def parametriclineequation(A, B, t, mode='2d'):
    if(mode == '2d'):
        Cx = A[0] + (t * (B[0] - A[0]))
        Cy = A[1] + (t * (B[1] - A[1]))
        C = [Cx, Cy]
        return C
    elif(mode == '3d'):
        Cx = A[0] + (t * (B[0] - A[0]))
        Cy = A[1] + (t * (B[1] - A[1]))
        Cz = A[2] + (t * (B[2] - A[2]))
        C = [Cx, Cy, Cz]
        return C

# t
def findt(A, B, P, N):
    AP = np.subtract(P, A)
    AB = np.subtract(B, A)

    t = np.matmul(AP, N) / np.matmul(AB, N)
    return t


def cyrusbeck3d(P1, P2, S, debug=True, proj='perspective'):
    # P1 & P2 are the points of the line we'd like to clip
    # S is the surfaces of the clipping object (counter-clockwise)
    Sref = ['front', 'back', 'left', 'right', 'top', 'bottom']

    planeNormals = ([0, 0, -1],  # front
                    [0, 0, 1],   # back
                    [1, 0, -1],  # left
                    [-1, 0, -1], # right
                    [0, -1, -1], # top
                    [0, 1, -1])  # bottom

    planeNormalsC = ([0, 0, -1],  # front
                    [0, 0, 1],   # back
                    [1, 0, 0],  # left
                    [-1, 0, 0], # right
                    [0, -1, 0], # top
                    [0, 1, 0])  # bottom

    

    trim = []
    trimN = []
    

    A = ([P1[0], P1[1], P1[2]])
    B = ([P2[0], P2[1], P2[2]])

    for idx, s in enumerate(S):
        # for every surface
        edges = s
        
        if(proj == 'perspective'):
            N = planeNormals[idx]
        elif(proj == 'parallel'):
            N = planeNormalsC[idx]
        # if(debug): 
        #     print('N: ' + str(N))

        P = edges[0][1] # second vertex in first edge
        P = ([P[0], P[1], P[2]])

        f = np.matmul(np.subtract(A, P), N)
        # if(f > 0): print('A is inside edge ' + str(i + 1))
        # elif(f < 0): print('A is outside edge ' + str(i + 1))
        # else: print('A is on edge ' + str(i + 1))

        f2 = np.matmul(np.subtract(B, P), N)
        # if(f2 > 0): print('B is inside edge ' + str(i + 1))
        # elif(f2 < 0): print('B is outside edge ' + str(i + 1))
        # else: print('B is on edge ' + str(i + 1))

        # if(debug): print(f'f: {f}, f2: {f2}')
    
        if(f >= 0 and f2 >= 0):
            # print('trivially accepted' + ' f: ' + str(f) + ' f2: ' + str(f2))
            if(debug): print('trivially accepted')
            
            
        elif(f < 0 and f2 < 0):
            # print('trivially rejected' + ' f: ' + str(f) + ' f2: ' + str(f2))
            if(debug): 
                print(f'trivially rejected, f: {f}, f2: {f2}')
                print(f'A: {A}')
                print(f'B: {B}')
                print(f'P: {P}')

            return None
        else:
            trim.append(s)
            trimN.append(planeNormals[idx])
        
    
    maxE = 0
    minL = 1

    for idx, s in enumerate(trim):
        edges = s

        N = trimN[idx]

        P = edges[0][1] # second vertex in first edge
        P = ([P[0], P[1], P[2]])

        f = np.matmul(np.subtract(A, P), N)
        f2 = np.matmul(np.subtract(B, P), N)

        if(f < 0 and f2 >= 0):
            if(debug): print('entering')
            t = findt(A, B, P, N)
            if(t > maxE): maxE = t
        elif(f >= 0 and f2 < 0):
            if(debug): print('leaving')
            t = findt(A, B, P, N)
            if(t < minL): minL = t
        else:
            if(debug): print(f'f: {f}, f2: {f2}')

    if(maxE < minL):
        C1 = parametriclineequation(A, B, maxE, '3d')
        P1res = ([C1[0], C1[1], C1[2]])

        C2 = parametriclineequation(A, B, minL, '3d')
        P2res = ([C2[0], C2[1], C2[2]])

        if(debug): print(f'P1: {P1}, P1res: {P1res}\nP2: {P2}, P2res: {P2res}')
        return P1res, P2res
    else:
        return None
    

def cyrusbeckv2(P1, P2, E, debug=True):
    # P1 & P2 are the points of the line we'd like to clip
    # V is the vertices of the object
    # E is the edges of the object

    

    trim = []
    trimN = []

    A = ([P1[0], P1[1]])
    B = ([P2[0], P2[1]])    

    for e in E:

        ep1 = e[0]
        ep2 = e[1]

        ep1 = (ep1[0], ep1[1])
        ep2 = (ep2[0], ep2[1])
        
        dy = ep2[1] - ep1[1]
        dx = ep2[0] - ep1[0]

        
        N = ([-dy, dx])
        
        # print('N: ' + str(N))

        P = ep2
        # print(P)

        f = np.matmul(np.subtract(A, P), N)
        # if(f > 0): print('A is inside edge ' + str(i + 1))
        # elif(f < 0): print('A is outside edge ' + str(i + 1))
        # else: print('A is on edge ' + str(i + 1))

        f2 = np.matmul(np.subtract(B, P), N)
        # if(f2 > 0): print('B is inside edge ' + str(i + 1))
        # elif(f2 < 0): print('B is outside edge ' + str(i + 1))
        # else: print('B is on edge ' + str(i + 1))
        
    
        if(f > 0 and f2 > 0):
            # print('trivially accepted' + ' f: ' + str(f) + ' f2: ' + str(f2))
            if(debug): print('trivially accepted')

        elif(f < 0 and f2 < 0):
            # print('trivially rejected' + ' f: ' + str(f) + ' f2: ' + str(f2))
            if(debug): print(f'trivially rejected, f: {f}, f2: {f2}')
            return None
            # print(ep1, ep2)
        else:
            trim.append(e)
            trimN.append(N)
    
    maxE = 0
    minL = 1

    for idx, e in enumerate(trim):
        ep1 = e[0]
        ep2 = e[1]

        ep1 = (ep1[0], ep1[1])
        ep2 = (ep2[0], ep2[1])

        N = trimN[idx]

        P = ep2
        # print(P)

        f = np.matmul(np.subtract(A, P), N)
        # if(f > 0): print('A is inside edge ' + str(i + 1))
        # elif(f < 0): print('A is outside edge ' + str(i + 1))
        # else: print('A is on edge ' + str(i + 1))

        f2 = np.matmul(np.subtract(B, P), N)
        # if(f2 > 0): print('B is inside edge ' + str(i + 1))
        # elif(f2 < 0): print('B is outside edge ' + str(i + 1))
        # else: print('B is on edge ' + str(i + 1))

        if(f < 0 and f2 >= 0):
            if(debug): print('entering')
            t = findt(A, B, P, N)
            if(t > maxE): maxE = t
        elif(f >= 0 and f2 < 0):
            if(debug): print('leaving')
            t = findt(A, B, P, N)
            if(t < minL): minL = t
        else:
            if(debug): print(f'f: {f}, f2: {f2}')

    if(maxE < minL):
        C1 = parametriclineequation(A, B, maxE)
        P1res = ([C1[0], C1[1]])

        C2 = parametriclineequation(A, B, minL)
        P2res = ([C2[0], C2[1]])

        if(debug): print(f'P1: {P1}, P1res: {P1res}\nP2: {P2}, P2res: {P2res}')
        return P1res, P2res
    else:
        return None