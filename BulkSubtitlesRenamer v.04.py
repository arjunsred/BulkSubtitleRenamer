# Bulk Subtitle Renamer
# Version 0.4

import os
import glob
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog, Text
from tkinter import *
from time import *

root = tk.Tk()
root.title('Bulk Renamer')

apps = []
name = []
txtfiles = []
txtfiles2 = []
method = []
o = []
j = []
vid_files = []
upd_vidfiles = []
sub_files = []
upd_subfiles = []
fileFormat1 = ["3g2","3gp","avi","flv","h264","m4v","mkv","mov","mp4","mpg","mpeg","rm","swf","vob","wmv"]
fileFormat2 = ["890","aqt","ass","cip","pjs","s2k","sbv","srt","ssa","sub","txt","zeg"]

ext1 = " "
ext2 = " "
ext3 = " "

n = 0
x = 0
e = 0
s = 0
ey = 0
sy = 0
es = 0
ss = 0
ev = 0
sv = 0 

def closeApp():
    root.withdraw()

def aboutApp():
    newWindow = tk.Toplevel(root)

def RadioButton():
    method.clear()
    x = int(var2.get())
    return x

def RightM():
    a = RadioButton()
    if a == 1:
        RenameF()    
    if a == 2:
        
        RenameN() 

def addApp():
    global name
    global folder_path
    global ext3

    filename = filedialog.askdirectory()
    apps.append(filename)
    os.chdir(filename)
    tk.Label(scrollable_frame, text=filename).grid(sticky = W) 
    tk.Label(scrollable_frame2).grid(sticky = W) 
  
    if int(var2.get()) == 1:
        txtfiles.clear()
        txtfiles2.clear()
        listoffiles = os.listdir()
        filelen = len(listoffiles)
        for z in range(0, filelen):  
            eachfilelen = len(listoffiles[z])
            b = listoffiles[z]
            a = eachfilelen-3
            ext = b[a:]
            if ext in fileFormat1 or ext in fileFormat2:
                if ext in fileFormat1:
                    txtfiles.append(listoffiles[z])
                    global ext1
                    ext1 = ext
                if ext in fileFormat2:
                    txtfiles2.append(listoffiles[z]) 
                    global ext2 
                    ext2 = ext 
                 

        if int(var3.get()) == 1:
            fileLength = len(txtfiles2)
            for h in range(0, fileLength):
                Length = len(txtfiles[h])
                Length = Length-4
                upd_txtfiles = txtfiles[h][:Length]
                txtfiles3 = txtfiles[h]

                tk.Label(scrollable_frame, text="\n" + txtfiles3 + " " + '——>' + " " + txtfiles2[h]).grid(sticky = W) 
                tk.Label(scrollable_frame2).grid(sticky = W) 
                

        if int(var3.get()) == 2:
            fileLength = len(txtfiles)
            for h in range(0, fileLength):
                Length = len(txtfiles2[h])
                Length = Length-4
                upd_txtfiles = txtfiles2[h][:Length]
            
                txtfiles3 = txtfiles2[h]
                tk.Label(scrollable_frame, text="\n" + txtfiles3 + " " + '——>' + " " + txtfiles[h]).grid(sticky = W) 
                tk.Label(scrollable_frame2).grid(sticky = W) 

        tk.Label(scrollable_frame, text="\n" + str(fileLength) + " files to be renamed.").grid(sticky = W) 
        tk.Label(scrollable_frame2).grid(sticky = W) 


        

    if int(var2.get()) == 2:
        

        listOfFiles = os.listdir()
        fileLen = len(listOfFiles)
        var = entry.get()
        var1 = entry2.get()
        itemLen = len(var)
        vid_files.clear()
        sub_files.clear()

        for v in range(0, len(fileFormat1)):
            for file in glob.glob("*." + fileFormat1[v]):
                vid_file,vid_ext = os.path.splitext(file)
                vid_files.append(file)
                upd_vidfiles.append(vid_file)

        for s in range(0, len(fileFormat2)):
            for file in glob.glob("*." + fileFormat2[s]):
                sub_file,sub_ext = os.path.splitext(file)
                sub_files.append(file)
                upd_subfiles.append(sub_file)

        for x in range(0, len(sub_files)):
            for u in range(0, len(sub_files[x])):   
                if var[0] == sub_files[x][u]:
                    o.append(u)   

            for t in range(0, len(o)):
                n = o[t] 
                for i in range(0, len(var)):
                    v = var[i]
                    if var[i] == "#":
                        b = sub_files[x][n]
                        if b.isdigit():
                            v = b
                            s = n 
  
                    if var[i] == "$":
                        b = sub_files[x][n]
                       
                        if b.isdigit():
                            v = b
                            e = n  
                    if sub_files[x][n] == v :
                       
                        n=n+1  
                    else:
                        print(sub_files[x])
                        print(var)
                        e = 0
                        s = 0
        
        for x in range(0, len(vid_files)):
            for u in range(0, len(vid_files[x])):   
                if var1[0] == vid_files[x][u]:
                    j.append(u)   

            for t in range(0, len(j)):
                n = j[t] 
                for i in range(0, len(var1)):
                    v = var1[i]
                    if var1[i] == "#":
                        b = vid_files[x][n]
                        if b.isdigit():
                            v = b
                            sy = n 

                    if var1[i] == "$":
                        b = vid_files[x][n]
                        if b.isdigit():
                            v = b
                            ey = n  

                    if vid_files[x][n] == v:
                        n=n+1                          
                      
                    else:
                        ey = 0
                        sy = 0

        name.clear() 

        for v in range(0, len(vid_files)):
            
            global renameName
            
            
            for t in range(0, len(sub_files)):
                global es
                global ss
                global ev
                global sv
                
                es = sub_files[t][e]
                ss = sub_files[t][s]
                ev = vid_files[v][ey]
                sv = vid_files[v][sy]

                
                if es == ev and ss == sv and sub_files[t] != vid_files[v]:

                    if int(var3.get()) == 1:
                        fileLength = len(vid_files)
                        

                        len_sub = len(sub_files[t])
                        n = len_sub-3
                        ext3 = sub_files[t][n:]


                        len_vid = len(vid_files[v])
                        n = len_vid-3
                        name.append(vid_files[v][:n])
                        renameName = vid_files[v]
                        
        
                        tk.Label(scrollable_frame, text="\n" + renameName + " " + '——>' + " " + sub_files[t]).grid(sticky = W) 
                        tk.Label(scrollable_frame2).grid(sticky = W) 

                    if int(var3.get()) == 2:
                        fileLength = len(sub_files)

                        len_vid = len(vid_files[v])
                        n = len_vid-3
                        ext3 = vid_files[v][n:]
                

                        len_sub = len(sub_files[t])
                        n = len_sub-3
                        name.append(sub_files[t][:n])
                        renameName = sub_files[t]

                        tk.Label(scrollable_frame, text="\n" + renameName + " " + '——>' + " " + vid_files[v]).grid(sticky = W) 
                        tk.Label(scrollable_frame2).grid(sticky = W) 

        tk.Label(scrollable_frame, text="\n" + str(fileLength) + " files to be renamed.").grid(sticky = W) 
        tk.Label(scrollable_frame2).grid(sticky = W) 
    
def RenameF():

    if int(var3.get()) == 1:
        fileLength = len(txtfiles2)
        for h in range(0, fileLength):
            Length = len(txtfiles[h])
            Length = Length-4
            upd_txtfiles = txtfiles[h][:Length]
            txtfiles3 = txtfiles[h]
            print(ext2)
            os.rename(txtfiles2[h], upd_txtfiles + '.' + ext2)

    if int(var3.get()) == 2:
        fileLength = len(txtfiles)
        for h in range(0, fileLength):
            Length = len(txtfiles2[h])
            Length = Length-4
            upd_txtfiles = txtfiles2[h][:Length]

            txtfiles3 = txtfiles2[h]
            os.rename(txtfiles[h], upd_txtfiles + '.' + ext1)
   
def RenameN():
   
    if int(var3.get()) == 1:
        for v in range(0, len(vid_files)):
            os.rename(sub_files[v], name[v] + ext3)

    if int(var3.get()) == 2:
        for t in range(0, len(vid_files)):    
            os.rename(vid_files[t], name[t] + ext3) 

class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        width = self.widget.winfo_width()
        height = self.widget.winfo_height()
        x += self.widget.winfo_rootx() + width-25
        y += self.widget.winfo_rooty() + height-5
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                        background='yellow', relief='solid', borderwidth=1,
                        font=("Arial", "8", "normal"))
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()

def hide_me(event):
    event.widget.pack_forget()
    sleep(2)
    event.widget.pack()

menubar = Menu(root)   
canvas = tk.Canvas(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Open",command = addApp)
filemenu.add_command(label="Close",command = closeApp)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...",command=aboutApp)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollbar2 = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
scrollable_frame2 = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
scrollable_frame2.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.configure(xscrollcommand=scrollbar2.set)

var2 = IntVar()
var3 = IntVar()

label2 = tk.Label(root, text="Rename")
label2.pack(anchor = W)       

R3 = Radiobutton(root, text="Video files", variable=var3, value=1, command = RadioButton)
R3.pack(anchor = W)

R4 = Radiobutton(root, text="Subtitle files", variable=var3, value=2, command = RadioButton)
R4.pack(anchor = W)

label1 = tk.Label(root, text="Rename based on")
label1.pack(anchor = W)  

R1 = Radiobutton(root, text="File order", variable=var2, value=1, command = lambda:[RadioButton, entry.config(state = 'disabled'), entry2.config(state = 'disabled')])
R1.pack(anchor = W)

R2 = Radiobutton(root, text="Matching phrase", variable=var2, value=2, command = lambda:[RadioButton, entry.config(state = 'normal'), entry2.config(state = 'normal')])
R2.pack(anchor = W)

label3 = tk.Label(root, text="Series-episode identifier phrase in subtitle files")
label3.pack(anchor = W)  

entry = tk.Entry(root, bd = 5, state = 'disabled')
entry.pack(side = TOP, fill=X, pady = 5, padx = 5) 

entry_ttp = CreateToolTip(entry, "Eg. if the series-episode identifier is S01E01 enter S##E$$")

label4 = tk.Label(root, text="Series-episode identifier phrase in video files")
label4.pack(anchor = W)  

entry2 = tk.Entry(root, bd = 5, state = 'disabled')
entry2.pack(side = TOP, fill=X, pady = 5, padx = 5) 

entry2_ttp = CreateToolTip(entry2, "Eg. if the series-episode identifier is S01E01 enter S##E$$")

openFolder = tk.Button(root, text='Browse folder',bg ='gray',fg = 'white', command = addApp)
openFolder.pack(side = TOP, fill=X, pady = 5, padx = 5) 

rename = tk.Button(root, text='Rename',bg ='brown',fg = 'white', command = RightM)
rename.pack(side = BOTTOM, fill=X, pady = 5, padx = 5) 

scrollbar2.pack(side=BOTTOM, fill="x", padx=5)  

for app in apps:
   label = tk.Label(root, text=app)
   label.pack(side = TOP, fill=X, pady = 5, padx = 5)       

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y", pady=5)  

root.mainloop()
