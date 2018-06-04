# Testing Regex

import re

text = 'Olá, meu nome é Igor e meu telefone é: 98120 5951'
PhoneRegex = re.compile(r'/d{3}')
mo = re.search(PhoneRegex, text)

if mo == None:
    print('Not Found')
else:
    print('The Phone number is: ' + mo.group(0))
