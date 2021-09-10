def functial2 (list_): 
    i=0
    while i<len(list_):
        print(list_[i])

import string
s=string.ascii_lowercase
def show(func):
    def new_func(s):
        print (func.__name__)
        print (func.__doc__)  
        result = new_func(list[s])
        print ("Result:",result)
        return result
    return new_func

