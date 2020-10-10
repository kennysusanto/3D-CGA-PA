import tkinter as tk
import classes as cs
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Perspective Viewing 2020')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.frame1 = tk.Frame(self, bg='gray', padx=8, pady= 6)
        self.frame1.pack(side='left', fill='both')
        self.frame2 = tk.Frame(self)
        self.frame2.pack(side='right', fill='both', expand=True)
        pad20 = 20
        self.frame3 = tk.Frame(self.frame2, padx=pad20, pady=pad20)
        self.frame3.pack(side='top', fill='both')
        self.frame4 = tk.Frame(self.frame2, padx=pad20, pady=pad20)
        self.frame4.pack(side='bottom', fill='both')

        self.canvas = tk.Canvas(self.frame1, height=480, width=580)
        coord = 10, 10, 300, 300
        arc = self.canvas.create_arc(coord, start=0, extent=150, fill="red")
        arv2 = self.canvas.create_arc(coord, start=150, extent=215, fill="green")
        self.canvas.place(relx=0.5, rely=0.5, anchor='center')
        self.canvas.pack()

        self.vrplbl = tk.Label(self.frame3, text="VRP:").grid(sticky='e', row=0, column=0)
        self.vpnlbl = tk.Label(self.frame3, text="VPN:").grid(sticky='e', row=1, column=0)
        self.vpnlbl = tk.Label(self.frame3, text="VPN:").grid(sticky='e', row=2, column=0)
        self.vpnlbl = tk.Label(self.frame3, text="VPN:").grid(sticky='e', row=3, column=0)
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
        self.refreshbtn.grid(row=8, column=0, sticky='nesw', columnspan=2)

        self.resetbtn = tk.Button(self.frame3, text='Reset', command=self.resetView)
        self.resetbtn.grid(row=9, column=0, sticky='nesw')

        self.quit = tk.Button(self.frame3, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=9, column=1, sticky='nesw')

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

    def parallelProj(self, h):
        H = h

        VRP = ([self.vrpx.get(), self.vrpy.get(), self.vrpz.get()])
        VPN = ([self.vpnx.get(), self.vpny.get(), self.vpnz.get()])
        VUP = ([self.vupx.get(), self.vupy.get(), self.vupz.get()])
        COP = ([self.copx.get(), self.copy.get(), self.copz.get()])
        umin = self.umin.get()
        vmin = self.vmin.get()
        umax = self.umax.get()
        vmax = self.vmax.get()
        fp = self.fp.get()
        bp = self.bp.get()

        A = ([ux, vx, Nx, 0],
             [uy, vy, Ny, 0],
             [uz, vz, Nz, 0],
             [rpx, rpy, rpz, 1])

        DOP = [DOPx, DOPy, DOPz]
        
        shx = -DOPx/DOPz
        shy = -DOPy/DOPz

        T3 = ([1, 0, 0, 0],
              [0, 1, 0, 0],
              [shx, shy, 1, 0],
              [0, 0, 0, 1])

        T4 = ([-(umin+umax)/2, -(vmin+vmax)/2, -F])

        T5 = ([2/(umax-umin), 2/(vmax-vmin), 1/(F-B)])

        pr2 = cs.pr2mat


    
    def refreshView(self):
        print("refresh!")
        H = self.theboringhouse()

        self.parallelProj(H)


    
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
        
        return


root = tk.Tk()
root.geometry('1024x480+200+200')
root.resizable(False, False)
app = Application(master=root)
app.mainloop()