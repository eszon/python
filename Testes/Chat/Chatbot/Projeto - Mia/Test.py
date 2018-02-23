from datetime import date
from time import gmtime, strftime
from datetime import datetime
import Class_PreProcess
import ssh

server = ssh.Connection(host='172.16.0.39', username='confere', password='cf1234')
result = server.execute('ping 172.16.0.17')

'''
def fslice(param1):
    s = param1.split(' ')[1]
    exec(s + f'{()}')

def fhour():
    now = date.today()
    t = strftime("%a, %d %b %Y %H:%M:%S -0003", gmtime())
    print(t)

def helloworld():
    print('Fucking hello word.')

s = 'function hora'
print(s.split(' ')[1])

response = 'function helloworld'

response2 =  response.split(' ')[0]
print(response2)
if response2 == 'function':
   fslice(response)


def fhour(): # Return time.
    now = datetime.now()
    print(f'São {now.hour}:{now.minute}:{now.second}.')
fhour()


def logicfuc(self, param1):
    response2 = param1.text.split(' ')[0]
    if response2 == 'function':
        print('9Mia:', end=' ')
        PreProcessed.fslice(param1 + '.text')

    else:
        print(f'{ftime()}Mia: ', param1, )

logicfuc(response="function hello")

'''
