abc = {'A': ' ', 'B': ' ', 'C': ' ',
       'D': ' ', 'E': ' ', 'F': ' ',
       'G': ' ', 'H': ' ', 'I': ' '}

player1 = 1
total_moves = 0
end = 0


# MOHNISH KHANNA

def yup():
    if abc['A'] == 'X' and abc['B'] == 'X' and abc['C'] == 'X':
        print("'X' WON THE GAME!!!")
        return 1
    if abc['D'] == 'X' and abc['E'] == 'X' and abc['F'] == 'X':  # HORIZONTAL X
        print("'X' WON THE GAME!!!")
        return 1
    if abc['G'] == 'X' and abc['H'] == 'X' and abc['I'] == 'X':
        print("'X' WON THE GAME!!!")
        return 1
    if abc['A'] == 'O' and abc['B'] == 'O' and abc['C'] == 'O':
        print("'O' WON THE GAME!!!")
        return 1
    if abc['D'] == 'O' and abc['E'] == 'O' and abc['F'] == 'O':  # HORIZONTAL O
        print("'O' WON THE GAME!!!")
        return 1
    if abc['G'] == 'O' and abc['H'] == 'O' and abc['I'] == 'O':
        print("'O' WON THE GAME!!!")
        return 1
    if abc['A'] == 'X' and abc['D'] == 'X' and abc['G'] == 'X':
        print("'X' WON THE GAME!!!")
        return 1
    if abc['B'] == 'X' and abc['E'] == 'X' and abc['F'] == 'X':  # VERTICAL X
        print("'X' WON THE GAME!!!")
        return 1
    if abc['C'] == 'X' and abc['F'] == 'X' and abc['I'] == 'X':
        print("'X' WON THE GAME!!!")
        return 1
    if abc['A'] == 'O' and abc['D'] == 'O' and abc['G'] == 'O':
        print("'O' WON THE GAME!!!")
        return 1
    if abc['B'] == 'O' and abc['E'] == 'O' and abc['F'] == 'O':  # VERTICAL O
        print("'O' WON THE GAME!!!")
        return 1
    if abc['C'] == 'O' and abc['F'] == 'O' and abc['I'] == 'O':
        print("'O' WON THE GAME!!!")
        return 1
    if abc['A'] == 'X' and abc['E'] == 'X' and abc['I'] == 'X':  # CROSS X
        print("'X' WON THE GAME!!!")
        return 1
    if abc['C'] == 'X' and abc['E'] == 'X' and abc['G'] == 'X':
        print("'X' WON THE GAME!!!")
        return 1
    if abc['A'] == 'O' and abc['E'] == 'O' and abc['I'] == 'O':  # CROSS O
        print("'O' WON THE GAME!!!")
        return 1
    if abc['C'] == 'O' and abc['E'] == 'O' and abc['G'] == 'O':
        print("'O' WON THE GAME!!!")
        return 1
    return 0


while True:
    print('_A_|_B_|_C_')
    print('_D_|_E_|_F_')
    print('_G_|_H_|_I_')
    print('__' + abc['A'] + '__' + '|' + '__' + abc['B'] + '__' + '|' + '__' + abc['C'] + '__')
    print('__' + abc['D'] + '__' + '|' + '__' + abc['E'] + '__' + '|' + '__' + abc['F'] + '__')
    print('__' + abc['G'] + '__' + '|' + '__' + abc['H'] + '__' + '|' + '__' + abc['I'] + '__')
    end = yup()
    if total_moves == 9 or end == 1:
        break
    while True:
        if player1 == 1:
            p1 = input("Enter wich place e.g 'A'")
            if p1.upper() in abc and abc[p1.upper()] == ' ':
                abc[p1.upper()] = 'X'
                player1 = 0
                break
            else:
                print('You enter wrong input')
                continue
        else:
            p2 = input("Enter wich place e.g  'F'")
            if p2.upper() in abc and abc[p2.upper()] == ' ':
                abc[p2.upper()] = 'O'
                player1 = 1
                break
            else:
                print("you input wrong")
                continue

    total_moves += 1
    print("******************************")
