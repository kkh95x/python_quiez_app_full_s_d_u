import tkinter as tk
import data.repostory as pr
import views.home_page_view as vi
import views.alter_empty as alt



data = pr.RepostroyQuiez.getAllQuiez()
root=tk.Tk()
root.geometry("800x550")
root.title("Quiez")

    
    
if(data==[]):
   alt.ALterEmpty(root=root)
else:
     
    vi.HomePage(root=root,data=data)
    
    
    


root.mainloop()   