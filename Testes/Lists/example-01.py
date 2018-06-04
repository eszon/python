mylist = ['Brazil', 'Python', 'Igor']

name = str(input('Type search string: '))

if name in mylist:
    print(f'Found string {name} at index: {mylist.index(name)} ')
else:
    print('Not Found!')

