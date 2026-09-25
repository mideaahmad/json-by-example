import json
from email.message import EmailMessage
from ipaddress import IPv4Address
from urllib.parse import ParseResult

data = """{
    "sender": {
        "__class": "EmailMessage",
        "headers": {
            "From": "admin@example.com",
            "To": "user@client.com",
            "Subject": "Access Granted"
        },
        "body": "Welcome! Your access has been granted. Click the link below."
    },
    "client_ip": {
        "__class": "IPv4Address",
        "address": "192.168.1.42"
    },
    "link": {
        "__class": "ParseResult",
        "scheme": "https",
        "netloc": "portal.example.com",
        "path": "/welcome",
        "params": "",
        "query": "token=abc123",
        "fragment": ""
    }
}"""
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, EmailMessage):
            return {
                "__class__": "EmailMessage",
                "headers": obj.headers,
                "body": obj.body
            }
        elif isinstance(obj, (ipaddress.IPv4Address, ipaddress.IPv6Address)):
            return {
                "__class__": "IPv4Address", 
                "address": str(obj)
            }
        elif isinstance(obj, ParseResult):
            return {
                "__class__": "ParseResult",
                "scheme": obj.scheme,
                "netloc": obj.netloc,
                "path": obj.path,
                "params": obj.params,
                "query": obj.query,
                "fragment": obj.fragment
            }
        return super().default(obj)

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, EmailMessage):
            return {
                "__class__": "EmailMessage",
                "headers": obj.headers,
                "body": obj.body
            }
        elif isinstance(obj, (ipaddress.IPv4Address, ipaddress.IPv6Address)):
            return {
                "__class__": "IPv4Address",  # أو "IPv6Address" حسب نوع الكائن
                "address": str(obj)
            }
        elif isinstance(obj, ParseResult):
            return {
                "__class__": "ParseResult",
                "scheme": obj.scheme,
                "netloc": obj.netloc,
                "path": obj.path,
                "params": obj.params,
                "query": obj.query,
                "fragment": obj.fragment
            }
        return super().default(obj)
def custom_decoder(dct):
    if "__class__" in dct:
        cls_name = dct["__class__"]
        
        if cls_name == "EmailMessage":
            return EmailMessage(headers=dct["headers"], body=dct["body"])
            
        elif cls_name == "IPv4Address":
            return ipaddress.IPv4Address(dct["address"])
            
        elif cls_name == "ParseResult":
            return ParseResult(
                scheme=dct["scheme"],
                netloc=dct["netloc"],
                path=dct["path"],
                params=dct["params"],
                query=dct["query"],
                fragment=dct["fragment"]
            )
    return dct
    if __name__ == '__main__':
     x= json.loads(data, object_hook=custom_decoder)
     print(x)
     y= json.dumps(x, cls=CustomEncoder, indent=4)
     print(type(y))
     print(y)