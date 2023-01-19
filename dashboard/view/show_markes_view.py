import view.home_page_view as hp
import tkinter as tk
from tkinter import ttk
class ShowMarks:
    def __init__(self,markes) :
        self.markes=markes
        self.tkWindow=tk.Tk()
        self.tkWindow.geometry("600x400")
        self.showLsitMarks()
        
    
    
        
        
        
    def showLsitMarks(self):
   
       
   
        columns = ('id', 'name', 'avarg')

        tree = ttk.Treeview(self.tkWindow, columns=columns, show='headings')
        tree.heading('id', text='رقم المعرف')
        tree.heading('name', text='الأسم')
        tree.heading('avarg', text='المعدل')
        for contact in self.markes:
            tree.insert('', tk.END, values=contact.toTuple())
           

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.tkWindow, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')


        
    
        
    