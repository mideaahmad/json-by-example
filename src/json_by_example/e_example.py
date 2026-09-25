'''
we will Encode and Decode datetime 
'''

'''
 {
  "__class":"datetime",
  "y": 2025,
  "month": 4,
  "d": 4,
  "h":23,
  "minute": 12,
  "s": 23
 }

'''
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
     
     def default(self, obj):
            if(isinstance(obj, datetime)):
                return {
                       "__class": "datetime",
                       "y": obj.year,
                       "month": obj.month,
                       "d":obj.day,
                       "h": obj.hour,
                       "minute": obj.minute,
                       "s": obj.second
                      }
          
            return json.JSONEncoder.default(self,obj) # if not datetime call the default implementation 
          
        
class DatetimeDecoder(json.JSONDecoder):
    
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=DatetimeDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "datetime":
            return datetime(d["y"],d["month"],d["d"],d["h"],d["minute"],d["s"])
                
        return d # defaulting if not datetime
          

                                    
if(__name__) == "__main__":
     stamp = datetime.now()
     print(stamp) # 2025-04-19 16:19:02.578592
     x  = json.dumps(stamp, cls=DateTimeEncoder)
     print(x)
     
     y = json.loads(x, cls=DatetimeDecoder)
     print(type(y)) # <class, 'datetime'>
     print(y) # 2025-04-19 16:19:02
     