import random as r

table = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

def tablereplace(inpu) -> int :
    if inpu == 1 : return 0 , 0
    if inpu == 4 : return 1 , 0
    if inpu == 7 : return 2 , 0

    if inpu == 2 : return 0 , 1
    if inpu == 5 : return 1 , 1
    if inpu == 8 : return 2 , 1

    if inpu == 3 : return 0 , 2
    if inpu == 6 : return 1 , 2
    if inpu == 9 : return 2 , 2

def turnreplace(inpu) -> str :
    if inpu == 'X' : return 'O'
    if inpu == 'O' : return 'X'

def printtable() :
    print('    {}\n    {}\n    {}'.format(table[0],table[1],table[2]))

def game(turnin,roundein) :
    global table
    print('{} turn\n{})'.format(turnin,roundein))
    printtable()
    ip = int(input('{} ; Type in the number you want to put the chess into. : '.format(turnin)))
    row , column = tablereplace(ip)
    table[row[column]] = turnin
    return turnreplace(turnin) , roundein + 1

    

x = 0
o = 0
turn = None
rounde = 1

input('Press any key to randomize. : ')
turn = r.randint(
    1,
    2
)
if turn == 1 : turn = 'X'
if turn == 2 : turn = 'O'

turn,round = game(turn,rounde)

printtable() ; print(turn) ; print(round)