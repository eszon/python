from datetime import date
from time import gmtime, strftime

def fhour():
    now = date.today()
    t = strftime("%a, %d %b %Y %H:%M:%S -0003", gmtime())
    print(t)

s = 'function hora'
print(s.split(' ')[1])

print(fhour())
