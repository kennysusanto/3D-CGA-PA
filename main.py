import tkinter as tk
import classes as cs
import numpy as np
import math
from PIL import Image, ImageTk
import cyrusbecklineclipping as cb

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Perspective Viewing 2020')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.frame1 = tk.Frame(self, bg='gray', padx=8, pady=6)
        self.frame1.pack(side='left', fill='both')
        self.frame2 = tk.Frame(self)
        self.frame2.pack(side='left', fill='both', expand=True)
        self.frame5 = tk.Frame(self, bg='gray', padx=8, pady=6)
        self.frame5.pack(side='left', fill='both')
        pad20 = 20
        self.frame3 = tk.Frame(self.frame2, padx=pad20, pady=pad20)
        self.frame3.pack(side='top', fill='both')
        self.frame4 = tk.Frame(self.frame2, padx=pad20, pady=pad20)
        self.frame4.pack(side='bottom', fill='both')

        self.canvas = tk.Canvas(self.frame1, height=480, width=480)
        # coord = 10, 10, 300, 300
        # arc = self.canvas.create_arc(coord, start=0, extent=150, fill="red")
        # arv2 = self.canvas.create_arc(coord, start=150, extent=215, fill="green")
        self.canvas.place(relx=0.5, rely=0.5, anchor='center')
        self.canvas.pack()

        # tambah canvas 2 disini di self.frame5
        self.canvas2 = tk.Canvas(self.frame5, height=480, width=480)
        self.canvas2.place(relx=0.5, rely=0.5, anchor='center')
        self.canvas2.pack()

        self.vrplbl = tk.Label(self.frame3, text="VRP:").grid(sticky='e', row=0, column=0)
        self.vpnlbl = tk.Label(self.frame3, text="VPN:").grid(sticky='e', row=1, column=0)
        self.vpnlbl = tk.Label(self.frame3, text="VUP:").grid(sticky='e', row=2, column=0)
        self.vpnlbl = tk.Label(self.frame3, text="COP:").grid(sticky='e', row=3, column=0)
        self.wminlbl = tk.Label(self.frame3, text="Window min:").grid(sticky='e', row=4, column=0)
        self.wmaxlbl = tk.Label(self.frame3, text="Window max:").grid(sticky='e', row=5, column=0)
        self.fplbl = tk.Label(self.frame3, text="FP:").grid(sticky='e', row=6, column=0)
        self.bplbl = tk.Label(self.frame3, text="BP:").grid(sticky='e', row=7, column=0)

        pad10 = 10
        pad5 = 5

        self.vrpx = tk.Entry(self.frame3, width=pad10)
        self.vrpx.grid(row=0, column=1, padx=pad10, pady=pad5)
        self.vrpx.insert(0, '0')
        self.vrpy = tk.Entry(self.frame3, width=pad10)
        self.vrpy.grid(row=0, column=2, padx=pad10)
        self.vrpy.insert(0, '0')
        self.vrpz = tk.Entry(self.frame3, width=pad10)
        self.vrpz.grid(row=0, column=3, padx=pad10)
        self.vrpz.insert(0, '0')

        self.vpnx = tk.Entry(self.frame3, width=pad10)
        self.vpnx.grid(row=1, column=1, padx=pad10, pady=pad5)
        self.vpnx.insert(0, '0')
        self.vpny = tk.Entry(self.frame3, width=pad10)
        self.vpny.grid(row=1, column=2, padx=pad10)
        self.vpny.insert(0, '0')
        self.vpnz = tk.Entry(self.frame3, width=pad10)
        self.vpnz.grid(row=1, column=3, padx=pad10)
        self.vpnz.insert(0, '1')

        self.vupx = tk.Entry(self.frame3, width=pad10)
        self.vupx.grid(row=2, column=1, padx=pad10, pady=pad5)
        self.vupx.insert(0, '0')
        self.vupy = tk.Entry(self.frame3, width=pad10)
        self.vupy.grid(row=2, column=2, padx=pad10)
        self.vupy.insert(0, '1')
        self.vupz = tk.Entry(self.frame3, width=pad10)
        self.vupz.grid(row=2, column=3, padx=pad10)
        self.vupz.insert(0, '0')

        self.copx = tk.Entry(self.frame3, width=pad10)
        self.copx.grid(row=3, column=1, padx=pad10, pady=pad5)
        self.copx.insert(0, '0')
        self.copy = tk.Entry(self.frame3, width=pad10)
        self.copy.grid(row=3, column=2, padx=pad10)
        self.copy.insert(0, '0')
        self.copz = tk.Entry(self.frame3, width=pad10)
        self.copz.grid(row=3, column=3, padx=pad10)
        self.copz.insert(0, '4')

        self.umin = tk.Entry(self.frame3, width=pad10)
        self.umin.grid(row=4, column=1, padx=pad10, pady=pad5)
        self.umin.insert(0, '-2')
        self.vmin = tk.Entry(self.frame3, width=pad10)
        self.vmin.grid(row=4, column=2, padx=pad10)
        self.vmin.insert(0, '-2')

        self.umax = tk.Entry(self.frame3, width=pad10)
        self.umax.grid(row=5, column=1, padx=pad10, pady=pad5)
        self.umax.insert(0, '2')
        self.vmax = tk.Entry(self.frame3, width=pad10)
        self.vmax.grid(row=5, column=2, padx=pad10)
        self.vmax.insert(0, '2')

        self.fp = tk.Entry(self.frame3, width=pad10)
        self.fp.grid(row=6, column=1, padx=pad10, pady=pad5)
        self.fp.insert(0, '2')
        self.bp = tk.Entry(self.frame3, width=pad10)
        self.bp.grid(row=7, column=1, padx=pad10, pady=pad5)
        self.bp.insert(0, '-10')

        self.refreshbtn = tk.Button(self.frame3, text='Refresh', command=self.refreshView)
        self.refreshbtn.grid(row=8, column=0, sticky='nesw', columnspan=4)

        self.resetbtn = tk.Button(self.frame3, text='Reset', command=self.resetView)
        self.resetbtn.grid(row=9, column=0, sticky='nesw', columnspan=2)

        self.quit = tk.Button(self.frame3, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=9, column=2, sticky='nesw', columnspan=2)

        self.sVPNxlbl = tk.Label(self.frame3, text='VPNx slider:')
        self.sVPNxlbl.grid(row=10, column=0)
        
        self.sVPNx = tk.Scale(self.frame3, from_=-1, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.slidex)
        self.sVPNx.set(0)
        self.sVPNx.grid(row=10, column=1, columnspan=3, sticky='nesw')

        self.sVPNylbl = tk.Label(self.frame3, text='VPNy slider:')
        self.sVPNylbl.grid(row=11, column=0)
        
        self.sVPNy = tk.Scale(self.frame3, from_=-1, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.slidey)
        self.sVPNy.set(0)
        self.sVPNy.grid(row=11, column=1, columnspan=3, sticky='nesw')

        self.sVPNzlbl = tk.Label(self.frame3, text='VPNz slider:')
        self.sVPNzlbl.grid(row=12, column=0)
        
        self.sVPNz = tk.Scale(self.frame3, from_=-1, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.slidez)
        self.sVPNz.set(1)
        self.sVPNz.grid(row=12, column=1, columnspan=3, sticky='nesw')


    def slidex(self, rval):
        self.vpnx.delete(0, tk.END)
        rval = float(rval)
        if(rval.is_integer()):
            rval = int(rval)
        else:
            pass
        self.vpnx.insert(0, str(rval))
        self.perspectiveProj()
        self.parallelProj()

    def slidey(self, rval):
        rval = float(rval)
        if(rval.is_integer()):
            rval = int(rval)
        else:
            pass
        self.vpny.delete(0, tk.END)
        self.vpny.insert(0, str(rval))
        self.perspectiveProj()
        self.parallelProj()

    def slidez(self, rval):
        rval = float(rval)
        if(rval.is_integer()):
            rval = int(rval)
        else:
            pass
        self.vpnz.delete(0, tk.END)
        self.vpnz.insert(0, str(rval))
        self.perspectiveProj()
        self.parallelProj()

    def theboringhouse(self):
        val = 1
        HouseV = cs.TVertexList()
        A = cs.TVertex(-val, -val, val)
        B = cs.TVertex(val, -val, val)
        C = cs.TVertex(val, 0, val)
        D = cs.TVertex(0, val, val)
        E = cs.TVertex(-val, 0, val)
        F = cs.TVertex(-val, -val, -val)
        G = cs.TVertex(val, -val, -val)
        H = cs.TVertex(val, 0, -val)
        I = cs.TVertex(0, val, -val)
        J = cs.TVertex(-val, 0, -val)

        HouseV.addVertex(A)
        HouseV.addVertex(B)
        HouseV.addVertex(C)
        HouseV.addVertex(D)
        HouseV.addVertex(E)
        HouseV.addVertex(F)
        HouseV.addVertex(G)
        HouseV.addVertex(H)
        HouseV.addVertex(I)
        HouseV.addVertex(J)

        HouseVList = HouseV.getVList()
        HouseE = cs.TEdgeList()
        E0 = cs.TEdge(HouseVList[0], HouseVList[1])   # edge 0
        E1 = cs.TEdge(HouseVList[1], HouseVList[2])   # edge 1
        E2 = cs.TEdge(HouseVList[2], HouseVList[3])   # edge 2
        E3 = cs.TEdge(HouseVList[3], HouseVList[4])   # edge 3
        E4 = cs.TEdge(HouseVList[4], HouseVList[0])   # edge 4
        
        E5 = cs.TEdge(HouseVList[5], HouseVList[6])   # edge 5
        E6 = cs.TEdge(HouseVList[6], HouseVList[7])   # edge 6
        E7 = cs.TEdge(HouseVList[7], HouseVList[8])   # edge 7
        E8 = cs.TEdge(HouseVList[8], HouseVList[9])   # edge 8
        E9 = cs.TEdge(HouseVList[9], HouseVList[5])   # edge 9

        E10 = cs.TEdge(HouseVList[0], HouseVList[5])   # edge 10
        E11 = cs.TEdge(HouseVList[1], HouseVList[6])   # edge 11
        E12 = cs.TEdge(HouseVList[2], HouseVList[7])   # edge 12
        E13 = cs.TEdge(HouseVList[3], HouseVList[8])   # edge 13
        E14 = cs.TEdge(HouseVList[4], HouseVList[9])   # edge 14

        HouseE.addEdge(E0)
        HouseE.addEdge(E1)
        HouseE.addEdge(E2)
        HouseE.addEdge(E3)
        HouseE.addEdge(E4)
        HouseE.addEdge(E5)
        HouseE.addEdge(E6)
        HouseE.addEdge(E7)
        HouseE.addEdge(E8)
        HouseE.addEdge(E9)
        HouseE.addEdge(E10)
        HouseE.addEdge(E11)
        HouseE.addEdge(E12)
        HouseE.addEdge(E13)
        HouseE.addEdge(E14)

        return HouseE.getEList()

    def perspectiveProj(self):
        self.canvas.delete('all')
        Hedges = self.theboringhouse()

        VRP = ([float(self.vrpx.get()), float(self.vrpy.get()), float(self.vrpz.get())])
        VPN = ([float(self.vpnx.get()), float(self.vpny.get()), float(self.vpnz.get())])
        VUP = ([float(self.vupx.get()), float(self.vupy.get()), float(self.vupz.get())])
        COP = ([float(self.copx.get()), float(self.copy.get()), float(self.copz.get())])
        umin = float(self.umin.get())
        vmin = float(self.vmin.get())
        umax = float(self.umax.get())
        vmax = float(self.vmax.get())
        fp = float(self.fp.get())
        bp = float(self.bp.get())

        VPN_mag = math.sqrt(math.pow(VPN[0], 2) + math.pow(VPN[1], 2) + math.pow(VPN[2], 2))
        N = np.divide(VPN, VPN_mag)

        VUP_mag = math.sqrt(math.pow(VUP[0], 2) + math.pow(VUP[1], 2) + math.pow(VUP[2], 2))
        up = np.divide(VUP, VUP_mag)

        upp = np.subtract(up, np.multiply(N, np.dot(up, N)))
        
        upp_mag = math.sqrt(math.pow(upp[0], 2) + math.pow(upp[1], 2) + math.pow(upp[2], 2))

        v = np.divide(upp, upp_mag)

        u = np.cross(v, N)

        r = ([VRP[0], VRP[1], VRP[2]])

        rp = ([np.dot(np.negative(r), u), np.dot(np.negative(r), v), np.dot(np.negative(r), N)])

        A = ([u[0], v[0], N[0], 0],
             [u[1], v[1], N[1], 0],
             [u[2], v[2], N[2], 0],
             [rp[0], rp[1], rp[2], 1])

        COPz = COP[2]
        F = fp
        B = -bp

        CW = ([(umax + umin)/2, (vmax + vmin)/2, 0])
        DOP = np.subtract(CW, COP)
        
        DOPx = DOP[0]
        DOPy = DOP[1]
        DOPz = DOP[2]
        shx = -(DOPx/DOPz)
        shy = -(DOPy/DOPz)

        T3 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [-COP[0], -COP[1], -COP[2], 1])

        F3 = F - COPz
        B3 = B - COPz

        T4 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [shx, shy, 1, 0],
              [0, 0, 0, 1])

        BP4 = B - COPz
        VP4 = -COPz

        h = ((COPz - B) * (vmax - vmin)) / (2 * COPz)
        w = ((COPz - B) * (umax - umin)) / (2 * COPz)

        T5 = ([-1/w, 0, 0, 0],      # beda
              [0, 1/h, 0, 0],
              [0, 0, -(1/BP4), 0],
              [0, 0, 0, 1])

        Pr1a = np.matmul(np.matmul(np.matmul(A, T3), T4), T5)
        Hedges1 = []
        for e in Hedges:
            tmpe = []
            e = e.getVertices()
            for p in e:
                p = p.getPoints()
                pv = ([p[0], p[1], p[2], 1])
                res = np.matmul(pv, Pr1a)
                tmpe.append(res)
            Hedges1.append(tmpe)
        
        # T6 clipping

        ViewVolumeV = cs.TVertexList() # view volume vertices
        F5 = (F - COPz) / (COPz - B)
        # print('F5:', F5)
        v0 = cs.TVertex(0, 0, F5)         # vertex 0
        v1 = cs.TVertex(0, 0, F5)         # vertex 1
        v2 = cs.TVertex(0, 0, F5)         # vertex 2
        v3 = cs.TVertex(0, 0, F5)         # vertex 3
        v4 = cs.TVertex(-1, 1, -1)       # vertex 4
        v5 = cs.TVertex(1, 1, -1)        # vertex 5
        v6 = cs.TVertex(1, -1, -1)       # vertex 6
        v7 = cs.TVertex(-1, -1, -1)      # vertex 7

        ViewVolumeV.addVertex(v0)
        ViewVolumeV.addVertex(v1)
        ViewVolumeV.addVertex(v2)
        ViewVolumeV.addVertex(v3)
        ViewVolumeV.addVertex(v4)
        ViewVolumeV.addVertex(v5)
        ViewVolumeV.addVertex(v6)
        ViewVolumeV.addVertex(v7)

        ViewVolumeVList = ViewVolumeV.getVList()
        ViewVolumeE = cs.TEdgeList() # view volume edges (counter-clockwise based on the axis of the surface)
        E0 = cs.TEdge(ViewVolumeVList[3], ViewVolumeVList[2])  # edge 0
        E1 = cs.TEdge(ViewVolumeVList[2], ViewVolumeVList[1])  # edge 1
        E2 = cs.TEdge(ViewVolumeVList[1], ViewVolumeVList[0])  # edge 2
        E3 = cs.TEdge(ViewVolumeVList[0], ViewVolumeVList[3])  # edge 3

        E4 = cs.TEdge(ViewVolumeVList[6], ViewVolumeVList[7])  # edge 4
        E5 = cs.TEdge(ViewVolumeVList[7], ViewVolumeVList[4])  # edge 5
        E6 = cs.TEdge(ViewVolumeVList[4], ViewVolumeVList[5])  # edge 6
        E7 = cs.TEdge(ViewVolumeVList[5], ViewVolumeVList[6])  # edge 7

        E8 = cs.TEdge(ViewVolumeVList[0], ViewVolumeVList[4])  # edge 8
        E9 = cs.TEdge(ViewVolumeVList[1], ViewVolumeVList[5])  # edge 9
        E10 = cs.TEdge(ViewVolumeVList[2], ViewVolumeVList[6])  # edge 10
        E11 = cs.TEdge(ViewVolumeVList[3], ViewVolumeVList[7])  # edge 11

        ViewVolumeE.addEdge(E0)
        ViewVolumeE.addEdge(E1)
        ViewVolumeE.addEdge(E2)
        ViewVolumeE.addEdge(E3)
        ViewVolumeE.addEdge(E4)
        ViewVolumeE.addEdge(E5)
        ViewVolumeE.addEdge(E6)
        ViewVolumeE.addEdge(E7)
        ViewVolumeE.addEdge(E8)
        ViewVolumeE.addEdge(E9)
        ViewVolumeE.addEdge(E10)
        ViewVolumeE.addEdge(E11)

        ViewVolumeEList = ViewVolumeE.getEList()
        ViewVolumeS = cs.TSurfaceList() # view volume surfaces (counter-clockwise based on the axis of the surface)
        S0 = cs.TSurface(ViewVolumeEList[0], ViewVolumeEList[1], ViewVolumeEList[2], ViewVolumeEList[3])               # front
        S1 = cs.TSurface(ViewVolumeEList[4], ViewVolumeEList[5], ViewVolumeEList[6], ViewVolumeEList[7])               # back
        S2 = cs.TSurface((ViewVolumeVList[7], ViewVolumeVList[3]), (ViewVolumeVList[3], ViewVolumeVList[0]), ViewVolumeEList[8], (ViewVolumeVList[4], ViewVolumeVList[7]))   # left
        S3 = cs.TSurface(ViewVolumeEList[10], (ViewVolumeVList[6], ViewVolumeVList[5]), (ViewVolumeVList[5], ViewVolumeVList[1]), (ViewVolumeVList[1], ViewVolumeVList[2]))  # right
        S4 = cs.TSurface((ViewVolumeVList[0], ViewVolumeVList[1]), ViewVolumeEList[9], (ViewVolumeVList[5], ViewVolumeVList[4]), (ViewVolumeVList[4], ViewVolumeVList[0]))   # top
        S5 = cs.TSurface((ViewVolumeVList[7], ViewVolumeVList[6]), (ViewVolumeVList[6], ViewVolumeVList[2]), (ViewVolumeVList[2], ViewVolumeVList[3]), ViewVolumeEList[11])  # bottom
        
        ViewVolumeS.addEdge(S0)
        ViewVolumeS.addEdge(S1)
        ViewVolumeS.addEdge(S2)
        ViewVolumeS.addEdge(S3)
        ViewVolumeS.addEdge(S4)
        ViewVolumeS.addEdge(S5)

        ViewVolumeSList = ViewVolumeS.getSList()
        surfaces = []

        for s in ViewVolumeSList:
            s = s.getSurface()
            tmps = []
            for e in s:
                tmpe = []
                if(isinstance(e, cs.TEdge)):
                    e = e.getVertices()
                else:
                    pass
                for v in e:
                    v = v.getPoints()
                    tmpe.append(v)
                tmps.append(tmpe)
            surfaces.append(tmps)

        Hedges2 = []
        for i, edge in enumerate(Hedges1):
            # print(f'\nedge: {i}')
            res = cb.cyrusbeck3d(edge[0], edge[1], surfaces, debug=False)
            if(res is not None):
                Hedges2.append(res)
            else:
                pass
            
            # print(res)
        
        
        VP5 = COPz / (B - COPz)
        T7t = ([0, 0, VP5]) # beda
        T7 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, -VP5, 1])

        vmax7 = COPz / (B - COPz)

        umax7 = COPz / (COPz - B)

        T8 = ([1/vmax7, 0, 0, 0], # beda
              [0, 1/vmax7, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1])
        
        COPz8 = COPz / (COPz - B)
        T9 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, -(1 / COPz8)],
              [0, 0, 0, 1])
        
        Hedges3 = []
        Pr1b = np.matmul(np.matmul(T7, T8), T9)
        for e in Hedges2:
            tmpe = []
            for p in e:
                p = list(p)
                pv = ([p[0], p[1], p[2], 1])
                res = np.matmul(pv, Pr1b)
                p = res
                if(p[3] == 0):
                    pass
                else:
                    p[0] = p[0]/p[3]
                    p[1] = p[1]/p[3]
                tmpe.append(p)
            Hedges3.append(tmpe)
        
        # drawing
        
        cwidth = self.canvas.winfo_width()
        cheight = self.canvas.winfo_height()
        coc = (cwidth / 2, cheight / 2)

        wwidth = 300
        wheight = 300
        w1 = (coc[0] - (wwidth / 2), coc[1] - (wheight / 2))
        w2 = (coc[0] + (wwidth / 2), coc[1] - (wheight / 2))
        w3 = (coc[0] + (wwidth / 2), coc[1] + (wheight / 2))
        w4 = (coc[0] - (wwidth / 2), coc[1] + (wheight / 2))

        wvertices = []
        wvertices.append(w1)
        wvertices.append(w2)
        wvertices.append(w3)
        wvertices.append(w4)

        wedges = []
        wedges.append((wvertices[0], wvertices[1]))
        wedges.append((wvertices[1], wvertices[2]))
        wedges.append((wvertices[2], wvertices[3]))
        wedges.append((wvertices[3], wvertices[0]))

        self.canvas.create_line(w1[0], w1[1], w2[0], w2[1])
        self.canvas.create_line(w2[0], w2[1], w3[0], w3[1])
        self.canvas.create_line(w3[0], w3[1], w4[0], w4[1])
        self.canvas.create_line(w4[0], w4[1], w1[0], w1[1])

        Hedges4 = []
        for e in Hedges3:
            tmpe = []
            for p in e:
                p = list(p)
                p[0] *= (wwidth / 2)
                p[1] *= (wheight / 2) 
                p[0] += coc[0]
                p[1] += coc[1]
                tmpe.append(p)
            Hedges4.append(tmpe)
        
        for i, e in enumerate(reversed(Hedges4)):
            
            p1 = e[0]
            p2 = e[1]
            # clip outside window
            newP1P2 = cb.cyrusbeckv2(p1, p2, wvertices, wedges, 'front', debug=False)
            p1, p2 = newP1P2        
            if(i > 9):
                self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill='red', width=2.5)
            else:
                self.canvas.create_line(p1[0], p1[1], p2[0], p2[1],fill="black",width=2.5)
    
    def parallelProj(self):
        self.canvas2.delete('all')
        Hedges = self.theboringhouse()

        VRP = ([float(self.vrpx.get()), float(self.vrpy.get()), float(self.vrpz.get())])
        VPN = ([float(self.vpnx.get()), float(self.vpny.get()), float(self.vpnz.get())])
        VUP = ([float(self.vupx.get()), float(self.vupy.get()), float(self.vupz.get())])
        COP = ([float(self.copx.get()), float(self.copy.get()), float(self.copz.get())])
        umin = float(self.umin.get())
        vmin = float(self.vmin.get())
        umax = float(self.umax.get())
        vmax = float(self.vmax.get())
        fp = float(self.fp.get())
        bp = float(self.bp.get())

        VPN_mag = math.sqrt(math.pow(VPN[0], 2) + math.pow(VPN[1], 2) + math.pow(VPN[2], 2))
        N = np.divide(VPN, VPN_mag)

        VUP_mag = math.sqrt(math.pow(VUP[0], 2) + math.pow(VUP[1], 2) + math.pow(VUP[2], 2))
        up = np.divide(VUP, VUP_mag)

        upp = np.subtract(up, np.multiply(N, np.dot(up, N)))
        
        upp_mag = math.sqrt(math.pow(upp[0], 2) + math.pow(upp[1], 2) + math.pow(upp[2], 2))

        v = np.divide(upp, upp_mag)

        u = np.cross(v, N)

        r = ([VRP[0], VRP[1], VRP[2]])

        rp = ([np.dot(np.negative(r), u), np.dot(np.negative(r), v), np.dot(np.negative(r), N)])

        A = ([u[0], v[0], N[0], 0],
             [u[1], v[1], N[1], 0],
             [u[2], v[2], N[2], 0],
             [rp[0], rp[1], rp[2], 1])

        COPz = COP[2]
        F = fp
        B = -bp

        CW = ([(umax + umin)/2, (vmax + vmin)/2, 0])
        DOP = np.subtract(CW, COP)
        
        DOPx = DOP[0]
        DOPy = DOP[1]
        DOPz = DOP[2]
        shx = -(DOPx/DOPz)
        shy = -(DOPy/DOPz)

        T3 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [shx, shy, 1, 0],
              [0, 0, 0, 1])

        T4 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [-(umin+umax)/2, -(vmin+vmax)/2, -F, 1])


        T5 = ([2/(umax-umin), 0, 0, 0],
              [0, -2/(vmax-vmin), 0, 0],
              [0, 0, 1/(F-B), 0],
              [0, 0, 0, 1])

        Pr1a = np.matmul(np.matmul(np.matmul(A, T3), T4), T5)
        Hedges1 = []
        for e in Hedges:
            tmpe = []
            e = e.getVertices()
            for p in e:
                p = p.getPoints()
                pv = ([p[0], p[1], p[2], 1])
                res = np.matmul(pv, Pr1a)
                tmpe.append(res)
            Hedges1.append(tmpe)

        cwidth = self.canvas.winfo_width()
        cheight = self.canvas.winfo_height()
        coc = (cwidth / 2, cheight / 2)

        wwidth = 300
        wheight = 300
        w1 = (coc[0] - (wwidth / 2), coc[1] - (wheight / 2))
        w2 = (coc[0] + (wwidth / 2), coc[1] - (wheight / 2))
        w3 = (coc[0] + (wwidth / 2), coc[1] + (wheight / 2))
        w4 = (coc[0] - (wwidth / 2), coc[1] + (wheight / 2))

        wvertices = []
        wvertices.append(w1)
        wvertices.append(w2)
        wvertices.append(w3)
        wvertices.append(w4)

        wedges = []
        wedges.append((wvertices[0], wvertices[1]))
        wedges.append((wvertices[1], wvertices[2]))
        wedges.append((wvertices[2], wvertices[3]))
        wedges.append((wvertices[3], wvertices[0]))

        self.canvas2.create_line(w1[0], w1[1], w2[0], w2[1])
        self.canvas2.create_line(w2[0], w2[1], w3[0], w3[1])
        self.canvas2.create_line(w3[0], w3[1], w4[0], w4[1])
        self.canvas2.create_line(w4[0], w4[1], w1[0], w1[1])

        Hedges2 = []
        for e in Hedges1:
            tmpe = []
            for p in e:
                p = list(p)
                p[0] *= (wwidth / 2)
                p[1] *= (wheight / 2) 
                p[0] += coc[0]
                p[1] += coc[1]
                tmpe.append(p)
            Hedges2.append(tmpe)
        
        for i, e in enumerate(reversed(Hedges2)):
            p1 = e[0]
            p2 = e[1]
            # clip outside window
            newP1P2 = cb.cyrusbeckv2(p1, p2, wvertices, wedges, 'front', debug=False)
            p1, p2 = newP1P2   
            if(i > 9):
                self.canvas2.create_line(p1[0], p1[1], p2[0], p2[1], fill='red', width=2.5)
            else:
                self.canvas2.create_line(p1[0], p1[1], p2[0], p2[1])

    def refreshView(self):

        print("refresh!")

        self.perspectiveProj()
        self.parallelProj()

        VPN = ([float(self.vpnx.get()), float(self.vpny.get()), float(self.vpnz.get())])
        self.sVPNx.set(str(VPN[0]))
        self.sVPNy.set(str(VPN[1]))
        self.sVPNz.set(str(VPN[2]))


    
    def resetView(self):
        print("resetting view...")

        self.vrpx.delete(0, tk.END)
        self.vrpx.insert(0, '0')
        self.vrpy.delete(0, tk.END)
        self.vrpy.insert(0, '0')
        self.vrpz.delete(0, tk.END)
        self.vrpz.insert(0, '0')

        self.vpnx.delete(0, tk.END)
        self.vpnx.insert(0, '0')
        self.vpny.delete(0, tk.END)
        self.vpny.insert(0, '0')
        self.vpnz.delete(0, tk.END)
        self.vpnz.insert(0, '1')

        self.vupx.delete(0, tk.END)
        self.vupx.insert(0, '0')
        self.vupy.delete(0, tk.END)
        self.vupy.insert(0, '1')
        self.vupz.delete(0, tk.END)
        self.vupz.insert(0, '0')

        self.copx.delete(0, tk.END)
        self.copx.insert(0, '0')
        self.copy.delete(0, tk.END)
        self.copy.insert(0, '0')
        self.copz.delete(0, tk.END)
        self.copz.insert(0, '4')

        self.umin.delete(0, tk.END)
        self.umin.insert(0, '-2')
        self.vmin.delete(0, tk.END)
        self.vmin.insert(0, '-2')

        self.umax.delete(0, tk.END)
        self.umax.insert(0, '2')
        self.vmax.delete(0, tk.END)
        self.vmax.insert(0, '2')

        self.fp.delete(0, tk.END)
        self.fp.insert(0, '2')
        self.bp.delete(0, tk.END)
        self.bp.insert(0, '-10')

        self.sVPNx.set(0)
        self.sVPNy.set(0)
        self.sVPNz.set(1)
        
        self.perspectiveProj()
        self.parallelProj()
        # tambah function parallelproj
        return


root = tk.Tk()

root.geometry('1350x480+200+200') # ganti ukuran window disini
root.resizable(False, False)

# Setting icon of master window 
image = Image.open("logo.jpg")
photo = ImageTk.PhotoImage(image)
root.iconphoto(False, photo) 

app = Application(master=root)

#def motion(event):
 #   x, y = event.x, event.y
  #  print('{}, {}'.format(x, y))

#root.bind('<Motion>', motion)

perpectivelbl = tk.Label(app, text='Perspective Projection',bg="#23252a",fg="yellowgreen")
perpectivelbl.place(x = 180,y=26,width=130,height=30)

parallellbl = tk.Label(app, text='Parallel Projection',bg="#23252a",fg="yellowgreen")
parallellbl.place(x = 1050,y=26,width=130,height=30)

app.mainloop()