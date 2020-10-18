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


def cyrusbeck3d(P1, P2, S, debug=True):
    # P1 & P2 are the points of the line we'd like to clip
    # S is the surfaces of the clipping object (counter-clockwise)
    Sref = ['front', 'back', 'left', 'right', 'top', 'bottom']

    planeNormals = ([0, 0, -1],  # front
                    [0, 0, 1],   # back
                    [1, 0, -1],  # left
                    [-1, 0, -1], # right
                    [0, -1, -1], # top
                    [0, 1, -1])  # bottom

    planeNormalsi = ([0, 0, 1],  # front
                    [0, 0, 1],   # back
                    [-1, 0, 1],  # left
                    [1, 0, 1], # right
                    [0, 1, 1], # top
                    [0, -1, 1])  # bottom

    res = []

    r = 0
    a = 0

    A = ([P1[0], P1[1], P1[2]])
    B = ([P2[0], P2[1], P2[2]])

    for idx, s in enumerate(S):
        # for every surface
        edges = s
        if(debug): print('surface: ' + Sref[idx])

        entering = []
        leaving = []
        
        
        
        N = planeNormals[idx]
        # print('N: ' + str(N))

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
    
        if(f > 0 and f2 > 0):
            # print('trivially accepted' + ' f: ' + str(f) + ' f2: ' + str(f2))
            if(debug): print('trivially accepted')
            
            
        elif(f < 0 and f2 < 0):
            # print('trivially rejected' + ' f: ' + str(f) + ' f2: ' + str(f2))
            if(debug): print('trivially rejected', f, f2)
            P1res = np.multiply(P1, 100)
            P2res = np.multiply(P2, 100)
            # P1res = P1
            # P2res = P2
            return P1res, P2res
            # print(ep1, ep2)
        else:
            # print('perform clipping' + ' f: ' + str(f) + ' f2: ' + str(f2))
            

            if(f < 0 and f2 > 0):
                # print('entering')

                t = findt(A, B, P, N)

                # print('t found at: ' + str(t))
                entering.append(t)

                C = parametriclineequation(A, B, t, '3d')
                # print('entering ' + str(C))
                # if(N[0] != 0):
                #     C = (A[0], C[1] )
                # elif(N[1] != 0):
                #     C = (C[0], A[1])
                
                Cv = ([C[0], C[1], C[2]])
                A = Cv
                # enteringC.append(C)
                # print(A)
                # print(B)
                if(debug): print('entering', t, Cv)
            elif(f > 0 and f2 < 0):
                # print('leaving')

                t = findt(A, B, P, N)

                # print('t found at: ' + str(t))
                leaving.append(t)

                C = parametriclineequation(A, B, t, '3d')
                # print('leaving ' + str(C))
                # if(N[0] != 0):
                #     C = (B[0], C[1])
                # elif(N[1] != 0):
                #     C = (C[0], B[1])

                Cv = ([C[0], C[1], C[2]])
                B = Cv
                # leavingC.append(C)
                # print(A)
                # print(B)
                if(debug): print('leaving', t, Cv)
            elif(f == 0):
                if(debug): print('A on plane')
                if(f2 == 0 or f2 > 0):
                    pass
                elif(f2 < 0):
                    t = findt(A, B, P, N)
                    C = parametriclineequation(A, B, t, '3d')
                    Cv = ([C[0], C[1], C[2]])
                    B = Cv
            elif(f2 == 0):
                if(debug): print('B on plane')
                if(f == 0 or f > 0):
                    pass
                elif(f < 0):
                    t = findt(A, B, P, N)
                    C = parametriclineequation(A, B, t, '3d')
                    Cv = ([C[0], C[1], C[2]])
                    A = Cv
            else:
                # print('none of the above')
                pass
        
        if(debug): print(f, f2)


    # max t for entering = te
    # min t for leaving = tl

    if(len(entering) < 1):
        P1res = A
        P2res = B
        if(debug): 
            print(f'P1: {P1}')
            print(f'P2: {P2}')
            print(f'P1 prime: {P1res}')
            print(f'P2 prime: {P2res}')
        return P1res, P2res

    elif(len(leaving) < 1):
        P1res = A
        P2res = B
        if(debug): 
            print(f'P1: {P1}')
            print(f'P2: {P2}')
            print(f'P1 prime: {P1res}')
            print(f'P2 prime: {P2res}')
        return P1res, P2res

    else:
        te = max(entering)
        tl = min(leaving)

        if(te <= tl):
            P1res = A
            P2res = B

        elif(te > tl):
            # print('AB rejected')
            P1res = P1
            P2res = P2
            # print('te: ' + str(te) + ' tl: ' + str(tl))
        else:
            # print('AB accepted no clipping')
            P1res = A
            P2res = B
        
        if(debug): 
            print(f'P1: {P1}')
            print(f'P2: {P2}')
            print(f'P1 prime: {P1res}')
            print(f'P2 prime: {P2res}')
        return P1res, P2res

    
    

    

def cyrusbeckv2(P1, P2, V, E, dir='right', debug=True):
    # P1 & P2 are the points of the line we'd like to clip
    # V is the vertices of the object
    # E is the edges of the object

    entering = []
    leaving = []

    a = 0
    r = 0

    if(dir == 'right'):
        A = ([P1[2], P1[1]])
        B = ([P2[2], P2[1]])    
    elif(dir == 'front'):
        A = ([P1[0], P1[1]])
        B = ([P2[0], P2[1]])    

    for e in E:

        ep1 = e[0]
        ep2 = e[1]

        ep1 = (ep1[0], ep1[1])
        ep2 = (ep2[0], ep2[1])
        
        dy = ep2[1] - ep1[1]
        dx = ep2[0] - ep1[0]

        
        if(dir == 'right'):
            N = ([dy, -dx])
        elif(dir == 'front'):
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
            a += 1
            pass
        elif(f < 0 and f2 < 0):
            # print('trivially rejected' + ' f: ' + str(f) + ' f2: ' + str(f2))
            r += 1
            pass
            # print(ep1, ep2)
        else:
            # print('perform clipping' + ' f: ' + str(f) + ' f2: ' + str(f2))
            pass

            if(f < 0 and f2 > 0):
                # print('entering')

                t = findt(A, B, P, N)

                # print('t found at: ' + str(t))
                entering.append(t)

                C = parametriclineequation(A, B, t)
                # print('entering ' + str(C))
                # if(N[0] != 0):
                #     C = (A[0], C[1] )
                # elif(N[1] != 0):
                #     C = (C[0], A[1])
                
                Cv = ([C[0], C[1]])
                A = Cv
                # enteringC.append(C)
                # print(A)
                # print(B)
            elif(f > 0 and f2 < 0):
                # print('leaving')

                t = findt(A, B, P, N)

                # print('t found at: ' + str(t))
                leaving.append(t)

                C = parametriclineequation(A, B, t)
                # print('leaving ' + str(C))
                # if(N[0] != 0):
                #     C = (B[0], C[1])
                # elif(N[1] != 0):
                #     C = (C[0], B[1])

                Cv = ([C[0], C[1]])
                B = Cv
                # leavingC.append(C)
                # print(A)
                # print(B)
            elif(f == 0 or f2 == 0):
                # print('on edge')
                pass
            else:
                # print('none of the above')
                pass
        if(debug == True):
            print(f, f2)
        
        

    # max t for entering = te
    # min t for leaving = tl
    if(debug): print(r, a)
    if(a == 4):
        P1res = P1
        P2res = P2
    else:
        if(r > 0):
            if(debug): print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr', r)
            entering.append(1)
            leaving.append(0)

    

        if(len(entering) < 1):
            te = 0
            tl = 1
        elif(len(leaving) < 1):
            te = 0
            tl = 1
        else:
            te = max(entering)
            tl = min(leaving)

        if(te <= tl):
            # print('AB accepted')
            pass
            # print('A = ' + str(P1))
            # print('B = ' + str(P2))
            # print('A prime = ' + str(A))
            # print('B prime = ' + str(B))
            if(dir == 'right'):
                P1res = (P1[0], A[1], A[0])
                P2res = (P2[0], B[1], B[0])
            elif(dir == 'front'):
                P1res = (A[0], A[1], P1[2])
                P2res = (B[0], B[1], P2[2])

            
        elif(te > tl):
            
            P1res = P1
            P2res = P1
            if(debug): print('not drawn')
            # print('AB rejected')
            pass
            # print('te: ' + str(te) + ' tl: ' + str(tl))
        else:
            # print('AB accepted no clipping')
            pass

    
        
    if(debug): print(P1res, P2res)
    
    return P1res, P2res

# P3 = (0, 0, -math.sqrt(2))
# P4 = (0, 0, ((9 * math.sqrt(2))/5))
# V2 = []
# V2.append((0, 2))
# V2.append((5, 2))
# V2.append((5, -2))
# V2.append((0, -2))
# E2 = []
# E2.append((V2[0], V2[1]))
# E2.append((V2[1], V2[2]))
# E2.append((V2[2], V2[3]))
# E2.append((V2[3], V2[0]))
# print(cyrusbeckv2(P3, P4, V2, E2))