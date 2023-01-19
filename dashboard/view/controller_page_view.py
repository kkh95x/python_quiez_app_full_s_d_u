from tkinter import * 
import view.home_page_view as hp
import view.show_markes_view as mk
class ControllerView:
    def __init__(self,root,markes,questions) :
        self.root=root
        self.showButton()
        self.markes=markes
        self.questions=questions
        
    def showAddPage(self):
        hp.AddQiuez(root=self.root)
   
    def showMarks(self):
        mk.ShowMarks(markes=self.markes) 
        
        
    def showButton(self):
        
        Button(self.root,text="أضف سؤال",bg="red",fg="white", width=20,command=self.showAddPage).pack(side=TOP,pady=10) 
        Button(self.root,text="عرض النتائج",bg="red",fg="white", width=20,command=self.showMarks).pack(side=TOP,pady=5) 