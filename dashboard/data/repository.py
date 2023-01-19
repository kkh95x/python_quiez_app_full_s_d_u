
import requests
import models.markes_model as ma

class RepostroyQuiez:
      def __init__(self):
        pass
      def add(d) :
       
       requests.post("http://localhost:3000/add",d.toMap())
        # response_info = json.loads(response)
      def getAllMark():
        try:
          response = requests.get("http://localhost:3000/marks").json()
        except:
          return []
          
      
        # response_info = json.loads(response)
        l=[]
        for x in response['quiez']:
            l.append(ma.MarkesModel.fromJson(x))
        return l
       
            


        