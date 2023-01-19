
from datetime import datetime

class MarkesModel:
    def __init__(self,id,name,avg):
        self.id=id
        self.name=name
        self.avg=avg
       
    def toJson(self):
         print("self",self.name)
         return {
             "id":self.id ,
             "username":self.name,
             "avg": self.avg,
             "dateTimeForSoultion":f"{datetime.now()}"
         }
        