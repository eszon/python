
mylist = []

while True:
    print('''Menu
            [1] Register Food
            [2] Search Food   
            [3] List All
            [4] Exit
    ''')

    option = int(input('Which option: '))

    if option == 1:
        register = str(input('Food: '))
        mylist.append(register)
        print(f'Food {register} is add with sucess.')

    if option == 2:
        searchfood = str(input('Search Food: '))
        if searchfood in mylist:
            print(f'Found food {searchfood} at index: {mylist.index(searchfood)}')
        else:
            print('Not Found!')

    if option == 3:
        print(mylist)

    if option == 4:
        print('Thank you.')
        break
