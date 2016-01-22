from Tkinter import *
import ttk
from PIL import Image
from PIL import ImageTk

class Menu_Initial_Requirement:

    class General_Purpose:
        def __init__(self,master):
            return
    class Compute_Optimized:
        def __init__(self,master):
            return
    class Memory_Optimized:
        def __init__(self,master):
            return
    class GPU_Optimized:
        def __init__(self,master):
            return
    class Storage_Optimized:
            def __init__(self,master):
                return


    def __init__(self,master):

        fnew = Frame(master)
        fnew.pack()
        v = IntVar()
        w = Label(master, text="Choose a Use Case or Requirement:")
        w.pack()
        MODES = [
        ("General Purpose, such as Development environments, build servers, code repositories, low-traffic websites and web applications, micro services, early product experiments, small databases.", 1),
        ("Compute Optimized, for high performance front-end fleets, web-servers, batch processing, distributed analytics, science and engineering applications, ad serving, MMO gaming, and video-encoding.", 2),
        ("Memory Optimized,  for high performance databases, distributed memory caches, in-memory analytics, genome assembly and analysis, larger deployments of SAP, Microsoft SharePoint, etc.", 3),
        ("Graphical use such as 3D application streaming, machine learning, video encoding, and other server-side graphics or GPU compute workloads.", 4),
        ("Storage Optimized for high optimized IOPS and storage in databases (both structured and unstuctured data)",5)]
        for text, mode in MODES:
            b = Radiobutton(master, text=text,
                        variable=v, value=mode)
            b.pack(anchor=W)
        b1 = Button(master, text="Submit", command=check(v))
        b1.pack(anchor=S)

#Ignore this for now
def check(val):
    opcode = ""
    if val==1:
        opcode.append("1")
    elif val==2:
        opcode.append("2")

root = Tk()
men = Menu_Initial_Requirement(root)
root.mainloop()
