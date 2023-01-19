from tkinter import *
from functools import partial
from models.qiuez_model import QuiezModle
from data.repository import RepostroyQuiez
import hashlib



class AddQiuez:
        def __init__(self,root) :
            self.tkWindow=root
            # self.tkWindow=Tk()
            self.tkWindow.geometry("500x800")
            self.qusetion = StringVar()
            self.qusetion = StringVar()
            self.answer1 = StringVar()
            self.answer2 = StringVar()
            self.answer3 = StringVar()
            self.answer4 = StringVar()
            self.correct = IntVar()
               
            self.showForm()
     
        def validateForm(self):
          print(self.answer1.get(),"   >------<")
          if self.checkAll():
                RepostroyQuiez.add(QuiezModle(
                answers=[self.answer1.get(),self.answer2.get(),self.answer3.get(),self.answer4.get()],
                correct_index=self.correct.get(),
                question=self.qusetion.get()
                ))
                self.removeALL()
          else:
              print(self.checkAll())
        def removeALL(self):
            self.answer1.set("")
            self.answer2.set("")
            self.answer3.set("")
            self.answer4.set("")
            self.qusetion.set("")
            self.correct.set(0)

    

        #username label and text entry box
        def showForm(self):
            Label(self.tkWindow, text="السؤال").pack(side=TOP,pady=5)
            
            Entry(self.tkWindow, textvariable=self.qusetion,justify="center").pack(side=TOP,pady=5) 

            #password label and password entry box
            Label(self.tkWindow,text="الإجابة 1").pack(side=TOP,pady=5)  
            
            Entry(self.tkWindow, textvariable=self.answer1,justify="center" ).pack(side=TOP,pady=5)
            Label(self.tkWindow,text="الإجابة 2").pack(side=TOP,pady=5) 
            
            Entry(self.tkWindow, textvariable=self.answer2, justify="center").pack(side=TOP,pady=5)    
            Label(self.tkWindow,text="الإجابة 3").pack(side=TOP,pady=5)  
            
            Entry(self.tkWindow, textvariable=self.answer3,justify="center"  ).pack(side=TOP,pady=5)  
            Label(self.tkWindow,text="الإجابة 4").pack(side=TOP,pady=5)  
            
            Entry(self.tkWindow, textvariable=self.answer4,justify="center"  ).pack(side=TOP,pady=5)
            Label(self.tkWindow,text=" رقم الإجابة الصحيحة").pack(side=TOP,pady=5)  
            
            Entry(self.tkWindow, textvariable=self.correct,justify="center"  ).pack(side=TOP,pady=5)

            validateForm = partial(self.validateForm)

            #login button
            loginButton = Button(self.tkWindow, text="إضافة", command=validateForm).pack(side=TOP,pady=50)  

        def checkAll(self):
            return self.answer1.get!="" and self.answer2.get!="" and self.answer3.get!="" and self.answer4.get!="" and self.qusetion.get!=""
        