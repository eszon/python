#!/usr/bin/python
n1 = str(input('Digite o nome de uma cidade: ')).strip().upper()
separa = n1.split()
#print(separa.find('SANTO'))
print('SANTO' in separa[0])
print(separa)
