
import requests
from model.quiez_model import QuiezModle
class RepostroyQuiez:
      def __init__(self):
        pass
      def getAllQuiez() :
        try:
          response = requests.get("http://localhost:3000/").json()
        except:
          return []
          
      
        # response_info = json.loads(response)
        l=[]
        for x in response['quiez']:
            l.append(QuiezModle.fromJson(x))
        return l
      def addMarks(marksModel):
        try:
           requests.post("http://localhost:3000/marks",marksModel.toJson())
        except:
          print("Error")
            


        