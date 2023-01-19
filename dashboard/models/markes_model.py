

class MarkesModel:
    def __init__(self,id,name,avg):
        self.id=id
        self.name=name
        self.avg=avg
        
       
    def fromJson(data):
        #  print('data  --> ',data)
         
         return MarkesModel(id=data['id'],name=data['username'],avg=data['avg'])
    def toTuple(self):
        return(self.id,self.name,self.avg)
            
         
        