from Tkinter import *
import os
import shutil as st

class Window(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("copy_service")
		self.pack(fill=BOTH,expand=1)
		global e1,e2
		e1=Entry(self,bd=1)
		e1.place(x=100,y=100)
		e2= Entry(self,bd=1)
		e2.place(x=100,y=200)
		b1 = Button(self,text="copy",command = cvt_callback)
		b1.place(x=100,y=300)

	def return_source_and_dest(self):
		return e1.get(),e2.get()
def cvt_callback():
	s,d = app.return_source_and_dest()
	source = os.listdir(s)
	for file in source:
		st.copy(s+file,d)


root = Tk()
root.geometry("600x400")
app = Window(root)
root.mainloop()