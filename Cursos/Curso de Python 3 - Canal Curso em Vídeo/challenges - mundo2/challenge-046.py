#/usr/bin/env python
from time import sleep
import emoji

print(10 * '=-=')
print('Contagem regressiva para estouro dos fogos de artificio.')
print(10 * '=-=')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('BUMMM! :confetti_ball:'))
print(emoji.emojize('BUMMM! :party_popper: '))


