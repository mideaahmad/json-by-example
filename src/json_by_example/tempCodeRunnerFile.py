if __name__ == '__main__':
     x=json.loads(data, object_hook=custom_decoder)
     pint(x) 
     y= json.dumps(x, cls=CustomEncoder, indent=4)
     pint(type(y))
     