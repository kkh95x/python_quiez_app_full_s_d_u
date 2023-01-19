from view.home_page_view import AddQiuez
import view.controller_page_view as ct
import tkinter as tk
import data.repository as rp

markes=rp.RepostroyQuiez.getAllMark()
root=tk.Tk()
root.geometry("400x400")
root.title("Quiez")


ct.ControllerView(root,markes=markes,questions=[])

root.mainloop()  