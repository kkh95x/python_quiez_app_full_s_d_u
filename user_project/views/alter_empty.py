import tkinter as tk
class ALterEmpty:
    def __init__(self,root):
        self.root=root
        frame= tk.Frame(root, relief= 'sunken')
        frame.place(relx=0.5,rely=0.5, anchor=tk.CENTER)
        self.frame=frame
        self.ShowLabel()
        self.showButton()
        
    def ShowLabel(self):
        q_no = tk.Label(self.frame, text=f"لا يوجد بيانات حاليا على السيرفر ",fg="red", width=60,font=( 'ariel' ,16, 'bold' ), justify='center',pady=50)
        q_no.grid(column=0,row=0,sticky=tk.N+tk.W)
    def showButton(self):
        btn= tk.Button(self.frame,text="close",width=20,command=self.root.destroy,)
        btn.grid(column=0,row=5)

        
        