from Tkinter import *
from PIL import Image,ImageTk

def check(val):
    if val==1:
        opcode.append("1")

root = Tk()
img = ImageTk.PhotoImage(Image.open("/home/minjar-70/images.jpg"))
#panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
v = IntVar()

Label(root,
      text="""Choose a type of Use Case or Requirement:""").pack()
Radiobutton(root,
            text="General Purpose, such as Development environments, build servers, code repositories, low-traffic websites and web applications, micro services, early product experiments, small databases.",
            padx = 20,
            variable=v,
            value=1).pack(anchor=W)
Radiobutton(root,
            text="Compute Optimized, for high performance front-end fleets, web-servers, batch processing, distributed analytics, science and engineering applications, ad serving, MMO gaming, and video-encoding.",
            padx = 20,
            variable=v,
            value=2).pack(anchor=W)
Radiobutton(root,
            text="Memory Optimized,  for high performance databases, distributed memory caches, in-memory analytics, genome assembly and analysis, larger deployments of SAP, Microsoft SharePoint, etc.",
            padx = 20,
            variable=v,
            value=3).pack(anchor=W)
Radiobutton(root,
            text="Graphical use such as 3D application streaming, machine learning, video encoding, and other server-side graphics or GPU compute workloads.",
            padx = 20,
            variable=v,
            value=4).pack(anchor=W)
Radiobutton(root,
            text="Storage Optimized for storage in databases (both structured and unstuctured data",
            padx = 20,
            variable=v,
            value=5).pack(anchor=W)
b = Button(root, text="Submit", command=check(v))
b.pack()
root.mainloop()