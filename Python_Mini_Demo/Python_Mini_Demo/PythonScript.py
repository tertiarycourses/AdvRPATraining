def hello(name=None):
    if name is None:
	    name = 'stranger'
    print ('Hello ', name)
    return 'Hello ' + name

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
	
def arr(length, value=None):
    return [value] * length

from datetime import datetime
now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
data = mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss
import ctypes
ctypes.windll.user32.MessageBoxW(0, str(data), "DATA", 3)
