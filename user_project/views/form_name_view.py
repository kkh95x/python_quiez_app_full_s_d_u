from tkinter import *
from functools import partial

import hashlib



class AddNameFormView:
        def __init__(self,root,username,userId,showNext) :
            self.tkWindow=root
            self.username = username
            self.userID = userId
            self.showNext=showNext
           
               
            self.showForm()
     
        def validateForm(self):
           
          if self.checkAll():
               self.destroyAll()
               print("csak;",self.userID.get(),self.username.get())
               self.showNext()
               
          else:
              print(self.checkAll())
           

    

        #username label and text entry box
        def showForm(self):
            self.labelID= Label(self.tkWindow, text="id")
            self.labelID.pack(side=TOP,pady=5)
            
            self.textID=Entry(self.tkWindow, textvariable=self.userID,width=35,justify="center") 
            self.textID.pack(side=TOP,pady=5)

            #password label and password entry box
            self.labelname=Label(self.tkWindow,text="name")  
            self.labelname.pack(side=TOP,pady=5)
            self.textname=Entry(self.tkWindow, textvariable=self.username,width=35,justify="center" )
            self.textname.pack(side=TOP,pady=5)
            

            validateForm = partial(self.validateForm)

            #login button
            self.saveButton = Button(self.tkWindow, text="إضافة",width=20, command=validateForm,bg="blue",fg="white")
            self.saveButton.pack(side=TOP,pady=100)  

        def checkAll(self):
            return self.username.get()!="" and self.userID.get()!=""
        def destroyAll(self):
            self.labelID.destroy()
            self.labelname.destroy()
            self.textID.destroy()
            self.textname.destroy()
            self.saveButton.destroy()
        
        