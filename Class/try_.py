from pprint import pprint

field = [[1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

current_a = 0
current_b =  0
    
def g_o():    
    print('***     Game over!       ***')

def change_field(a_incr, b_incr):
    try:
        global current_a, current_b, field
        field[current_a][current_b] = 0
        current_a += a_incr
        current_b += b_incr
        field[current_a][current_b] = 1
    except IndexError:
        print('Вы вышли за границы поля!')
        return -1
    else:
        return 0

while True:
    pprint(field)
    move = input('Введите направление (q for quit)')
    if move == 'q':
        g_o()
        break
    else:
        if move == 'd':
            result = change_field(1, 0)
        elif move == 'u':
            result = change_field(-1, 0)
        elif move == 'r':
            result = change_field(0, 1)
        elif move == 'l':
            result = change_field(0, -1)
        else:
            print('Нужно значение r, l, d или u')
            continue
        if result == -1:
            g_o()
            break
        if field[3][7] == 1:
            print('***       WIN     ***')
            pprint(field)
            break

    