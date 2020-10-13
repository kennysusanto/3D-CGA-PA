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
        # rval = self.sliderx.get()
        self.vpnx.delete(0, tk.END)
        rval = float(rval)
        if(rval.is_integer()):
            rval = int(rval)
            # print(rval)
        else:
            # print(rval)
            pass
        self.vpnx.insert(0, str(rval))
        self.perspectiveProj()
        self.parallelProj()

    def slidey(self, rval):
        # rval = self.sliderx.get()
        rval = float(rval)
        if(rval.is_integer()):
            rval = int(rval)
            # print(rval)
        else:
            # print(rval)
            pass
        self.vpny.delete(0, tk.END)
        self.vpny.insert(0, str(rval))
        self.perspectiveProj()
        self.parallelProj()

    def slidez(self, rval):
        # rval = self.sliderx.get()
        rval = float(rval)
        if(rval.is_integer()):
            rval = int(rval)
            # print(rval)
        else:
            # print(rval)
            pass
        self.vpnz.delete(0, tk.END)
        self.vpnz.insert(0, str(rval))
        self.perspectiveProj()
        self.parallelProj()

    def theboringhouse(self):
        # absval = 5
        # V = []
        # V[0] = [-absval, absval, absval]
        # V[1] = [absval, absval, absval]
        # V[2] = [absval, -absval, absval]
        # V[3] = [-absval, -absval, absval]
        # V[4] = [-absval, absval, -absval]
        # V[5] = [absval, absval, -absval]
        # V[6] = [absval, -absval, -absval]
        # V[7] = [-absval, -absval, -absval]

        H = []
        H.append([-1, -1, 1])  # A
        H.append([1, -1, 1])   # B 
        H.append([1, 0, 1])    # C
        H.append([0, 1, 1])    # D
        H.append([-1, 0, 1])   # E
        H.append([-1, -1, -1]) # F
        H.append([1, -1, -1])  # G
        H.append([1, 0, -1])   # H
        H.append([0, 1, -1])   # I
        H.append([-1, 0, -1])  # J

        return H

    def perspectiveProj(self):
        self.canvas.delete('all')
        H = self.theboringhouse()

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

        H2 = []

        for i in range(len(H)):
            P = H[i]
            Pv = ([P[0], P[1], P[2]])
            a = np.dot(np.subtract(Pv, VRP), u)
            b = np.dot(np.subtract(Pv, VRP), v)
            c = np.dot(np.subtract(Pv, VRP), N)
            P2 = (a, b, c)
            H2.append(P2)


        CW = ([(umax + umin)/2, (vmax + vmin)/2, 0])
        DOP = np.subtract(CW, COP)
        
        DOPx = DOP[0]
        DOPy = DOP[1]
        DOPz = DOP[2]
        shx = -(DOPx/DOPz)
        shy = -(DOPy/DOPz)
        
        H3 = []
        for i in range(len(H2)):
            P = H2[i]
            res = cs.Translate(P, COP)
            P3 = (res[0], res[1], res[2])
            H3.append(P3)

        T4 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [shx, shy, 1, 0],
              [0, 0, 0, 1])

        H4 = []
        for i in range(len(H3)):
            P = H3[i]
            Pv = ([P[0], P[1], P[2], 1])
            res = np.matmul(Pv, T4)
            P4 = (res[0], res[1], res[2])
            H4.append(P4)
            # print(P4)

        F = fp
        B = -bp

        COPz = COP[2]
        BP4 = B - COPz
        VP4 = -COPz

        h = ((COPz - B) * (vmax - vmin)) / (2 * COPz)
        w = ((B - COPz) * (umax - umin)) / (2 * COPz)

        T5 = ([1/w, 1/h, -(1/BP4)])

        H5 = []
        for i in range(len(H4)):
            res = cs.Scale(H4[i], T5)
            P5 = (res[0], res[1], res[2])
            H5.append(P5)
            # print(P5)

                
        # T6 clipping not yet implemented
        # print('\n')

        Hedges = []
        Hedges.append((H5[0], H5[1]))
        Hedges.append((H5[1], H5[2]))
        Hedges.append((H5[2], H5[3]))
        Hedges.append((H5[3], H5[4]))
        Hedges.append((H5[4], H5[0]))
        
        Hedges.append((H5[5], H5[6]))
        Hedges.append((H5[6], H5[7]))
        Hedges.append((H5[7], H5[8]))
        Hedges.append((H5[8], H5[9]))
        Hedges.append((H5[9], H5[5]))

        Hedges.append((H5[0], H5[5]))
        Hedges.append((H5[1], H5[6]))
        Hedges.append((H5[2], H5[7]))
        Hedges.append((H5[3], H5[8]))
        Hedges.append((H5[4], H5[9]))

        V = []
        V.append((fp, vmax))
        V.append((bp, vmax))
        V.append((bp, -vmin))
        V.append((fp, -vmin))
        # V.append((umin, vmax, F))
        # V.append((umax, vmax, F))
        # V.append((umax, vmin, F))
        # V.append((umin, vmin, F))
        # V.append((umin, vmax, B))
        # V.append((umax, vmax, B))
        # V.append((umax, vmin, B))
        # V.append((umin, vmin, B))

        edges = []
        edges.append((V[0], V[1]))
        edges.append((V[1], V[2]))
        edges.append((V[2], V[3]))
        edges.append((V[3], V[0]))
        # edges.append((V[0], V[1])) # edge 0
        # edges.append((V[1], V[2])) # edge 1
        # edges.append((V[2], V[3])) # edge 2
        # edges.append((V[3], V[0])) # edge 3

        # edges.append((V[4], V[5])) # edge 4
        # edges.append((V[5], V[6])) # edge 5
        # edges.append((V[6], V[7])) # edge 6
        # edges.append((V[7], V[4])) # edge 7

        # edges.append((V[0], V[4])) # edge 8
        # edges.append((V[1], V[5])) # edge 9
        # edges.append((V[2], V[6])) # edge 10
        # edges.append((V[3], V[7])) # edge 11

        # surfaces = []
        # surfaces.append((edges[0], edges[1], edges[2], edges[3])) # front
        # surfaces.append((edges[4], edges[5], edges[6], edges[7])) # back
        # surfaces.append((edges[4], (V[5], V[1]), (V[1], V[0]), edges[8])) # top
        # surfaces.append(((V[7], V[6]), (V[6], V[2]), edges[2], edges[11])) # bottom
        # surfaces.append(((V[4], V[0]), (V[0], V[3]), edges[11], edges[7])) # left
        # surfaces.append(((V[5], V[1]), edges[1], edges[10], (V[6], V[5]))) # right

        tmp = []
        H6 = []
        for i in range(len(Hedges)):
            housedge = Hedges[i]
            res = cb.cyrusbeckv2(housedge[0], housedge[1], V, edges)
            tmp.append(res)
            if(i < 10):
                H6.append(res[0])
            # print(res)
        
        VP5 = COPz / (B - COPz)
        T7 = ([0, 0, -VP5])

        H7 = []
        for i in range(len(H6)):
            P = H6[i]
            res = cs.Translate(P, T7)
            P7 = (res[0], res[1], res[2])
            H7.append(P7)
            # print(P7)

        
        vmax7 = COPz / (COPz - B)

        
        umax7 = COPz / (B - COPz)

        T8 = ([1/umax7, 0, 0, 0],
              [0, 1/vmax7, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1])
        
        H8 = []

        for i in range(len(H7)):
            P = H7[i]
            Pv = ([P[0], P[1], P[2], 1])
            res = np.matmul(Pv, T8)
            P8 = (res[0], res[1], res[2])
            H8.append(P8)
            # print(P8)

        COPz8 = COPz / (COPz - B)
        T9 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, -(1 / COPz8)],
              [0, 0, 0, 1])
        
        H9 = []

        for i in range(len(H8)):
            P = H8[i]
            Pv = ([P[0], P[1], P[2], 1])
            res = np.matmul(Pv, T9)
            P9 = (res[0], res[1], res[2])
            H9.append(P9)
            # print(P9)

        Htest = []
        
        for i in H9:
            p = list(i)
            p[0] = p[0]/p[2]
            p[1] = p[1]/p[2]
            Htest.append(p)
        
        
        H10 = []
        for i in range(len(Htest)):
            P = Htest[i]
            Pv = ([P[0], P[1], P[2], 1])
            res = np.matmul(Pv, cs.pr2mat)
            P10 = (res[0], res[1], res[2])
            H10.append(P10)
            # print(P10)
        
        # drawing

        H10b = []
        minusY = ([1, -1, 1])
        for i in range(len(H9)):
            P = H10[i]
            res = cs.Scale(P, minusY)
            P10b = (res[0], res[1], res[2])
            H10b.append(P10b)
        
        cwidth = self.canvas.winfo_width()
        cheight = self.canvas.winfo_height()
        coc = (cwidth / 2, cheight / 2)

        wwidth = 300
        wheight = 300
        w1 = (coc[0] - (wwidth / 2), coc[1] - (wheight / 2))
        w2 = (coc[0] + (wwidth / 2), coc[1] - (wheight / 2))
        w3 = (coc[0] + (wwidth / 2), coc[1] + (wheight / 2))
        w4 = (coc[0] - (wwidth / 2), coc[1] + (wheight / 2))

        self.canvas.create_line(w1[0], w1[1], w2[0], w2[1])
        self.canvas.create_line(w2[0], w2[1], w3[0], w3[1])
        self.canvas.create_line(w3[0], w3[1], w4[0], w4[1])
        self.canvas.create_line(w4[0], w4[1], w1[0], w1[1])

        H11 = []
        for p in H10b:
            P = list(p)
            P[0] *= coc[0] - 75
            P[1] *= coc[1] - 75
            P[0] += coc[0]
            P[1] += coc[1]
            H11.append(P)
            # print(P)
        
        Hedges11 = []
        Hedges11.append((H11[0], H11[1]))
        Hedges11.append((H11[1], H11[2]))
        Hedges11.append((H11[2], H11[3]))
        Hedges11.append((H11[3], H11[4]))
        Hedges11.append((H11[4], H11[0]))
        
        Hedges11.append((H11[5], H11[6]))
        Hedges11.append((H11[6], H11[7]))
        Hedges11.append((H11[7], H11[8]))
        Hedges11.append((H11[8], H11[9]))
        Hedges11.append((H11[9], H11[5]))

        Hedges11.append((H11[0], H11[5]))
        Hedges11.append((H11[1], H11[6]))
        Hedges11.append((H11[2], H11[7]))
        Hedges11.append((H11[3], H11[8]))
        Hedges11.append((H11[4], H11[9]))
        
        for i, e in enumerate(Hedges11):
            p1 = e[0]
            p2 = e[1]
            # print(p1, p2)
            if(i < 5):
                self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill='red', width=2.5)
            else:
                self.canvas.create_line(p1[0], p1[1], p2[0], p2[1],fill="black",width=2.5)

        # print('\n')
        # print(VRP)
        # print(N, v, u)
        # print('\nH1')
        # for i in H:
        #     print(i)
        
        # print('\nH2')
        # for i in H2:
        #     print(i)

        # print('\nH3')
        # for i in H3:
        #     print(i)

        # print('\n')
        # print(DOP)
        # print(shx, shy)
        # print('\nH4')
        # for i in H4:
        #     print(i)

        # print('\n')
        # print('w', w, 1/w)
        # print('h', h, 1/h)
        # print('bp4', BP4, -(1/BP4))
        # print('\nH5')
        # for i in H5:
        #     print(i)

        # print('\nH6')
        # for i in H6:
        #     print(i)

        # print('\nH7')
        # for i in H7:
        #     print(i)
        
        # print('\n')
        # print(B, COPz)
        # print(B-COPz, COPz-B)
        # print(umax7, vmax7)
        # print(1/umax7, 1/vmax7)
        # print('\nH8')
        # for i in H8:
        #     print(i)

        # print('\nH9')
        # for i in H9:
        #     print(i)
        
        # print('\nH10')
        # for i in H10:
        #     print(i)
        
        # print('\nH10b')
        # for i in H10b:
        #     print(i)
        
        # print('\nH11')
        # for i in H11:
        #     print(i)
        
        # print('\nHtest')
        # for i in Htest:
        #     print(i)
    
    def parallelProj(self):
        self.canvas2.delete('all') # ganti ini jadi canvas yg kedua
        H = self.theboringhouse()

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

        H2 = []

        for i in range(len(H)):
            P = H[i]
            Pv = ([P[0], P[1], P[2]])
            a = np.dot(np.subtract(Pv, VRP), u)
            b = np.dot(np.subtract(Pv, VRP), v)
            c = np.dot(np.subtract(Pv, VRP), N)
            P2 = (a, b, c)
            H2.append(P2)


        CW = ([(umax + umin)/2, (vmax + vmin)/2, 0])
        DOP = np.subtract(CW, COP)
        
        DOPx = DOP[0]
        DOPy = DOP[1]
        DOPz = DOP[2]
        shx = -(DOPx/DOPz)
        shy = -(DOPy/DOPz)
        
        H3 = []
        for i in range(len(H2)):
            P = H2[i]
            res = cs.Translate(P, COP)
            P3 = (res[0], res[1], res[2])
            H3.append(P3)

        T4 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [shx, shy, 1, 0],
              [0, 0, 0, 1])

        H4 = []
        for i in range(len(H3)):
            P = H3[i]
            Pv = ([P[0], P[1], P[2], 1])
            res = np.matmul(Pv, T4)
            P4 = (res[0], res[1], res[2])
            H4.append(P4)
            # print(P4)

        F = fp
        B = -bp

        COPz = COP[2]
        BP4 = B - COPz
        VP4 = -COPz

        h = ((COPz - B) * (vmax - vmin)) / (2 * COPz)
        w = ((B - COPz) * (umax - umin)) / (2 * COPz)

        T5 = ([1/w, 1/h, -(1/BP4)])

        H5 = []
        for i in range(len(H4)):
            res = cs.Scale(H4[i], T5)
            P5 = (res[0], res[1], res[2])
            H5.append(P5)
            # print(P5)

                
        # T6 clipping not yet implemented
        # print('\n')

        Hedges = []
        Hedges.append((H5[0], H5[1]))
        Hedges.append((H5[1], H5[2]))
        Hedges.append((H5[2], H5[3]))
        Hedges.append((H5[3], H5[4]))
        Hedges.append((H5[4], H5[0]))
        
        Hedges.append((H5[5], H5[6]))
        Hedges.append((H5[6], H5[7]))
        Hedges.append((H5[7], H5[8]))
        Hedges.append((H5[8], H5[9]))
        Hedges.append((H5[9], H5[5]))

        Hedges.append((H5[0], H5[5]))
        Hedges.append((H5[1], H5[6]))
        Hedges.append((H5[2], H5[7]))
        Hedges.append((H5[3], H5[8]))
        Hedges.append((H5[4], H5[9]))

        V = []
        V.append((fp, vmax))
        V.append((bp, vmax))
        V.append((bp, -vmin))
        V.append((fp, -vmin))
        # V.append((umin, vmax, F))
        # V.append((umax, vmax, F))
        # V.append((umax, vmin, F))
        # V.append((umin, vmin, F))
        # V.append((umin, vmax, B))
        # V.append((umax, vmax, B))
        # V.append((umax, vmin, B))
        # V.append((umin, vmin, B))

        edges = []
        edges.append((V[0], V[1]))
        edges.append((V[1], V[2]))
        edges.append((V[2], V[3]))
        edges.append((V[3], V[0]))
        # edges.append((V[0], V[1])) # edge 0
        # edges.append((V[1], V[2])) # edge 1
        # edges.append((V[2], V[3])) # edge 2
        # edges.append((V[3], V[0])) # edge 3

        # edges.append((V[4], V[5])) # edge 4
        # edges.append((V[5], V[6])) # edge 5
        # edges.append((V[6], V[7])) # edge 6
        # edges.append((V[7], V[4])) # edge 7

        # edges.append((V[0], V[4])) # edge 8
        # edges.append((V[1], V[5])) # edge 9
        # edges.append((V[2], V[6])) # edge 10
        # edges.append((V[3], V[7])) # edge 11

        # surfaces = []
        # surfaces.append((edges[0], edges[1], edges[2], edges[3])) # front
        # surfaces.append((edges[4], edges[5], edges[6], edges[7])) # back
        # surfaces.append((edges[4], (V[5], V[1]), (V[1], V[0]), edges[8])) # top
        # surfaces.append(((V[7], V[6]), (V[6], V[2]), edges[2], edges[11])) # bottom
        # surfaces.append(((V[4], V[0]), (V[0], V[3]), edges[11], edges[7])) # left
        # surfaces.append(((V[5], V[1]), edges[1], edges[10], (V[6], V[5]))) # right

        tmp = []
        H6 = []
        for i in range(len(Hedges)):
            housedge = Hedges[i]
            res = cb.cyrusbeckv2(housedge[0], housedge[1], V, edges)
            tmp.append(res)
            if(i < 10):
                H6.append(res[0])
            # print(res)
        
        VP5 = COPz / (B - COPz)
        T7 = ([0, 0, -VP5])

        H7 = []
        for i in range(len(H6)):
            P = H6[i]
            res = cs.Translate(P, T7)
            P7 = (res[0], res[1], res[2])
            H7.append(P7)
            # print(P7)

        
        vmax7 = COPz / (COPz - B)

        
        umax7 = COPz / (B - COPz)

        T8 = ([1/umax7, 0, 0, 0],
              [0, 1/vmax7, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1])
        
        H8 = []

        for i in range(len(H7)):
            P = H7[i]
            Pv = ([P[0], P[1], P[2], 1])
            res = np.matmul(Pv, T8)
            P8 = (res[0], res[1], res[2])
            H8.append(P8)
            # print(P8)

        COPz8 = COPz / (COPz - B)
        T9 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, -(1 / COPz8)],
              [0, 0, 0, 1])
        
        H9 = []

        for i in range(len(H8)):
            P = H8[i]
            Pv = ([P[0], P[1], P[2], 1])
            res = np.matmul(Pv, T9)
            P9 = (res[0], res[1], res[2])
            H9.append(P9)
            # print(P9)
        
        
        H10 = []
        for i in range(len(H9)):
            P = H9[i]
            Pv = ([P[0], P[1], P[2], 1])
            res = np.matmul(Pv, cs.pr2mat)
            P10 = (res[0], res[1], res[2])
            H10.append(P10)
            # print(P10)
        
        # drawing

        H10b = []
        minusY = ([1, -1, 1])
        for i in range(len(H9)):
            P = H10[i]
            res = cs.Scale(P, minusY)
            P10b = (res[0], res[1], res[2])
            H10b.append(P10b)
        
        cwidth = self.canvas.winfo_width()
        cheight = self.canvas.winfo_height()
        coc = (cwidth / 2, cheight / 2)

        wwidth = 300
        wheight = 300
        w1 = (coc[0] - (wwidth / 2), coc[1] - (wheight / 2))
        w2 = (coc[0] + (wwidth / 2), coc[1] - (wheight / 2))
        w3 = (coc[0] + (wwidth / 2), coc[1] + (wheight / 2))
        w4 = (coc[0] - (wwidth / 2), coc[1] + (wheight / 2))

        self.canvas2.create_line(w1[0], w1[1], w2[0], w2[1])
        self.canvas2.create_line(w2[0], w2[1], w3[0], w3[1])
        self.canvas2.create_line(w3[0], w3[1], w4[0], w4[1])
        self.canvas2.create_line(w4[0], w4[1], w1[0], w1[1])

        H11 = []
        for p in H10b:
            P = list(p)
            P[0] *= coc[0] - 100
            P[1] *= coc[1] - 100
            P[0] += coc[0]
            P[1] += coc[1]
            H11.append(P)
            # print(P)
        
        Hedges11 = []
        Hedges11.append((H11[0], H11[1]))
        Hedges11.append((H11[1], H11[2]))
        Hedges11.append((H11[2], H11[3]))
        Hedges11.append((H11[3], H11[4]))
        Hedges11.append((H11[4], H11[0]))
        
        Hedges11.append((H11[5], H11[6]))
        Hedges11.append((H11[6], H11[7]))
        Hedges11.append((H11[7], H11[8]))
        Hedges11.append((H11[8], H11[9]))
        Hedges11.append((H11[9], H11[5]))

        Hedges11.append((H11[0], H11[5]))
        Hedges11.append((H11[1], H11[6]))
        Hedges11.append((H11[2], H11[7]))
        Hedges11.append((H11[3], H11[8]))
        Hedges11.append((H11[4], H11[9]))
        
        for i, e in enumerate(Hedges11):
            p1 = e[0]
            p2 = e[1]
            # print(p1, p2)
            if(i < 5):
                self.canvas2.create_line(p1[0], p1[1], p2[0], p2[1], fill='red', width=5) # ganti ini jadi kanvas kedua
            else:
                self.canvas2.create_line(p1[0], p1[1], p2[0], p2[1]) # ganti ini jadi canvas kedua





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