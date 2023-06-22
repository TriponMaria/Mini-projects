win = False
a = [['', '', ''],
     ['', '', ''],
     ['', '', '']]

winning_options = []
for i in range(3):
    o = []
    for j in range(3):
        v = [i, j]
        o.append(v)
    winning_options.append(o)
winning_options.append([[0, 0], [1, 1], [2, 2]])
winning_options.append([[2, 0], [1, 1], [1, 2]])


def check_option(a):
    for v in winning_options:
        if a[v[0][0]][v[0][1]] == 'O' and a[v[1][0]][v[1][1]] == 'O' and a[v[2][0]][v[2][1]] == 'O':
            return "User 1 win !!!"
        elif a[v[0][0]][v[0][1]] == 'X' and a[v[1][0]][v[1][1]] == 'X' and a[v[2][0]][v[2][1]] == 'X':
            return "User 2 win !!!"


def board_func(a):
    board = ''''''
    for i in a:
        board += '|'
        for j in i:
            if j == '':
                board += '___'
            else:
                board += ('_' + str(j) + '_')
            board += '|'
        board += '\n'
    print(board)


while not win:

    user_1 = input("User 1: ")
    u_1 = list(map(int, user_1.split()))
    if a[u_1[0]][u_1[1]] == '':
        a[u_1[0]][u_1[1]] = 'O'
    win = check_option(a)
    if win:
        board_func(a)
        print(win)
        break
    user_2 = input("User 2: ")
    u_2 = list(map(int, user_2.split()))
    if a[u_2[0]][u_2[1]] == '':
        a[u_2[0]][u_2[1]] = 'X'

    board_func(a)
    print(a)
    win = check_option(a)
    if win:
        board_func(a)
        print(win)
        break
