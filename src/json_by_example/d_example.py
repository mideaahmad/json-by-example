'''
Not all Python datatype can be converted into JSON ; for example complex datatype 
we extends the class JSONEncoder . Encoding is a way to convert Python Object to JSON Object( string in this case); 
Decoder is opposite which is to convert JSON Object(String in our case) into Python Object (dictionary in case all types can be converted)
'''
import json


# we will represent a complex number (i+j) in JSON as  below
'''
  { 
    "__class":"complex",
    "real":123.55,
    "imag":-15.55
  }
'''

# below converting a complex datatype in python to JSON string object
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            # You see return your own dictionary which represent the class and the values as you wish
            return  { 
                     "__class":"complex",
                     "real": obj.real,
                     "imag": obj.imag
                    }
        
        # In case we don't have complex object; let the base c lass default method raise the TypeError
        return super().default(obj)
    

class ComplexDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=ComplexDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "complex":
            return complex(d.get("real"), d.get("imag"))

        return d
                     


if __name__ == '__main__':
    x = json.dumps(2 + 1j, cls= ComplexEncoder)
    print(x) 

    y = json.loads(x, cls=ComplexDecoder)
    print(type(y)) # <class, complex)
    print(y) # (2+1j)  the complex value

