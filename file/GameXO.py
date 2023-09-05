import random as r

try :
    table_row1 = ['1','2','3']
    table_row2 = ['4','5','6']
    table_row3 = ['7','8','9']

    def clearboard_and_rounde() :
        global table_row1 , table_row2 , table_row3 , rounde
        rounde = 1
        table_row1 = ['1','2','3']
        table_row2 = ['4','5','6']
        table_row3 = ['7','8','9']

    def tablereplace(inpu) -> int :
        if inpu == 1 : return 1 , 0
        if inpu == 4 : return 2 , 0
        if inpu == 7 : return 3 , 0

        if inpu == 2 : return 1 , 1
        if inpu == 5 : return 2 , 1
        if inpu == 8 : return 3 , 1

        if inpu == 3 : return 1 , 2
        if inpu == 6 : return 2 , 2
        if inpu == 9 : return 3 , 2

    def turnreplace(inpu) -> str :
        if inpu == 'X' : return 'O'
        if inpu == 'O' : return 'X'

    def printtable() :
        print('    {}\n    {}\n    {}'.format(table_row1,table_row2,table_row3))

    def game(turnin,roundein) :
        global table_row1 , table_row2 , table_row3
        print('\n{} turn\n{})'.format(turnin,roundein))
        printtable()
        ip = int(input('{} ; Type in the number you want to put the chess into. : '.format(turnin)))
        row , column = tablereplace(ip)

        if row == 1 : table_row1[column] = turnin
        elif row == 2 : table_row2[column] = turnin
        elif row == 3 : table_row3[column] = turnin
        roundein += 1

        return turnreplace(turnin) , roundein

    def checkgame() -> str:
        global table_row1 , table_row2 , table_row3

        '''    X    '''
        # --- [ -> ]
        if table_row1 == ['X','X','X'] : return True , 'X'
        elif table_row2 == ['X','X','X'] : return True , 'X'
        elif table_row3 == ['X','X','X'] : return True , 'X'
        
        # ||| [ ^ ]
        elif table_row1[0] == 'X' and table_row2[0] == 'X' and table_row3[0] == 'X': return True , 'X'
        elif table_row1[1] == 'X' and table_row2[1] == 'X' and table_row3[1] == 'X': return True , 'X'
        elif table_row1[2] == 'X' and table_row2[2] == 'X' and table_row3[2] == 'X': return True , 'X'

        # X [ X ]
        elif table_row1[0] == 'X' and table_row2[1] == 'X' and table_row3[2] == 'X': return True , 'X'
        elif table_row1[2] == 'X' and table_row2[1] == 'X' and table_row3[0] == 'X': return True , 'X'


        '''    O    '''
        # --- [ -> ]
        if table_row1 == ['O','O','O'] : return True , 'O'
        elif table_row2 == ['O','O','O'] : return True , 'O'
        elif table_row3 == ['O','O','O'] : return True , 'O'
        
        # ||| [ ^ ]
        elif table_row1[0] == 'O' and table_row2[0] == 'O' and table_row3[0] == 'O': return True , 'O'
        elif table_row1[1] == 'O' and table_row2[1] == 'O' and table_row3[1] == 'O': return True , 'O'
        elif table_row1[2] == 'O' and table_row2[2] == 'O' and table_row3[2] == 'O': return True , 'O'

        # X [ X ]
        elif table_row1[0] == 'O' and table_row2[1] == 'O' and table_row3[2] == 'O': return True , 'O'
        elif table_row1[2] == 'O' and table_row2[1] == 'O' and table_row3[0] == 'O': return True , 'O'

        else : return False , None

    x = 0
    o = 0
    turn = None
    rounde = 1

    while True :
        q = input('Press any key to randomize. [Q to exit] : ')
        if q == 'Q' or q == 'q' : break
        else :
            turn = r.randint(
                1,
                2
            )
            if turn == 1 : turn = 'X'
            if turn == 2 : turn = 'O'

            print('score : X = {} , O = {}'.format(x,o))
            while True :
                #check
                checker , who_wins = checkgame()

                if checker == True :
                    clearboard_and_rounde()
                    print('\n{} Win!!!!!\n'.format(who_wins))
                    if who_wins == 'X' : x += 1 ; break
                    if who_wins == 'O' : o += 1 ; break
                
                turn , rounde = game(turn,rounde)
except : print('\n\n\n\n\n\n\nERROR PLEASE TRY AGAIN') ; input('Press any key to exit : ')