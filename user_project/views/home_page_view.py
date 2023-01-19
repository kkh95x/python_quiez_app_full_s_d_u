import tkinter as tk
from tkinter import IntVar, StringVar, messagebox as mb
import views.form_name_view as fn
import data.repostory as pr
from model.marks_model import MarkesModel






class HomePage :
   
    def __init__(self,root,data) :
    
    
      self.i=0
      self.q_no=0
      self.opt_selected=IntVar()
      
      self.root=root
      self.data=data
      self.username = StringVar()
      self.userId = StringVar()
      fn.AddNameFormView(root=root,username=self.username,userId=self.userId,showNext=self.firstShow)
      
    #   self.initalHome()
    #   self.showButton()
    #   self.display_options()
    #   self.correct=0
    #   self.showNameAlter()
      
    
    def firstShow(self):
      self.opts=self.radio_buttons()
      self.initalHome()
      self.showButton()
      self.display_options()
      self.correct=0
    def showQuestion(self):
        q_no = tk.Label(self.root,text= f"Q {self.i+1} - {len(self.data)}: {self.data[self.i].question}", width=60,font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        q_no.place(x=70, y=100)  
        
    
    def initalHome(self):
        
        self.showQuestion()
    
    
    def showNext(self):
        print(self.username.get())
        if self.checkAnswer():
                self.correct+=1
        if self.checkIsFinishedQuestion():
         self.display()
        
         mb.showinfo('isFinished')
         self.root.destroy()
        else:
           
                
            self.i+=1
           
            self.initalHome()
            self.display_options()
    def checkIsFinishedQuestion(self):
        if self.i+1==len(self.data):
            return True
        else:
            return False
        
    def showButton(self):
        btn= tk.Button(self.root,text="أرسال الإجابة",width=30,bg='#16a085',fg='white',command=self.showNext,font=( 'ariel' ,14, 'bold' ))
        btn.pack(side=tk.BOTTOM,pady=50)
    
    def radio_buttons(self):
		
            q_list = []
            
            y_pos = 150
            
            while len(q_list) < 4:
                
                radio_btn = tk.Radiobutton(
                text=" "
                ,variable=self.opt_selected,
              
                value = len(q_list)+1,font = ("ariel",14)
                )
                q_list.append(radio_btn)
                radio_btn.place(x = 100, y = y_pos)
                y_pos += 40
                
            
            return q_list
        
        
    def display_options(self):
                val=0
            
                self.opt_selected.set(0)
            
            
                for option in self.data[self.i].answers:
                    self.opts[val]['text']=option
                    val+=1
            
    def checkAnswer(self):
       return self.opt_selected.get()==self.data[self.i].correct_index
    def display(self):
        model=MarkesModel(id=self.userId.get(),name=self.username.get(),avg=str(int(self.correct/len(self.data)*100)))
        pr.RepostroyQuiez.addMarks(model)
        q_no = tk.Label(self.root, text=f"عدد الأسئلة:{len(self.data)}  الإجابات الصحية : {self.correct}  معدل: {int(self.correct/len(self.data)*100)}",fg="red",font=( 'ariel' ,16, 'bold' ), justify='center', anchor= 'w' )
        q_no.pack(side=tk.BOTTOM)
        self.q_no=q_no
    