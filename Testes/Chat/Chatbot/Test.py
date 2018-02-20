from datetime import date
from time import gmtime, strftime


def fslice(param1):
    s = param1.split(' ')[1]
    print(s + f'{()}')

def fhour():
    now = date.today()
    t = strftime("%a, %d %b %Y %H:%M:%S -0003", gmtime())
    print(t)

'''s = 'function hora'
print(s.split(' ')[1])
'''

response = 'function helloworld'

response2 =  response.split(' ')[0]
print(response2)
if response2 == 'function':
   fslice(response)
