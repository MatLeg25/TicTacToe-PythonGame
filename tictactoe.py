
import os
import sys
import string
os.system("cls || clear")
##FUNKCJE:

board = [['.','.','.'], ['.','.','.'], ['.','.','.'],]
count=0


def init_board(): #wyświetlanie tablicy
   # for row in range(3):
   #     for columne in range(3):
   #         board[row][columne] = '.'

    board = [['.','.','.'], ['.','.','.'], ['.','.','.'],]
    return board

def check_move(player_move):
    if (len(player_move) == 2):
        pass
        
        ##SPRAWDZANIE CZY podane wartości poprawnie określają pozycję
        status=0
        for i in range(0,1):
            if (player_move[i].upper()=="A") or (player_move[i].upper()=="B") or (player_move[i].upper()=="C"):
                status+=1
            if (player_move[i+1].upper()=="1") or (player_move[i+1].upper()=="2") or (player_move[i+1].upper()=="3"):
                status+=1

        #if (player_move[0].upper()=="A") or (player_move[0].upper()=="B") or (player_move[0].upper()=="C") or (player_move.upper()=="1") or (player_move.upper()=="2") or (player_move.upper()=="3"):
        if (status ==2):
            pass
            return True

        else:
            print("\nWrong position, try again! \n Type format XY, where: X-row, Y-column or 'quit' to exit the program.")
            #print("ERROR:",player_move)
            input("\nEnter to accept")
            print("\n")
            return False

    else:
        print("\nWrong position, try again! \n Type format XY, where: X-row, Y-column or 'quit' to exit the program.")
        #print("ERROR:",player_move)
        input("\nEnter to accept")
        print("\n")
        return False

def convert(player_move):  ## KONWERTOWANIE tego co podał użytkownik na pozycje w tabeli
    player_move = player_move.upper() # konwersja na duże litery
    row = string.ascii_uppercase.index(player_move[0])
    column = int(player_move[1]) -1

    if (board[row][column] == "."):
        #print("Your move: R-", row,"|C-",column)
        #input("ENTER to accept")
        position = True
        return position,row,column
    else:
        print("\n Position",player_move," is not empty! Try again:\n")
        position = False
        return position,row,column

def get_move(): #input + ruch
    global count
    input_check=False
    position = False

    if (count%2==0):
        player="Player X"
    else:
        player="Player O"

    while (input_check == False or position==False):
        player_move= input(" {}, move: ".format(player))
        if (player_move=="quit"):
            sys.exit()
        input_check= check_move(player_move)
        if input_check:
            position,row,column=convert(player_move)

    count+=1

    return row,column,count

def check_position(row,column): #sprawdzanie cyz na danej pozycji mozna wpisac
    global board
    if not (board[row][column] == "O") or (board[row][column] == "X"):
        return True
    else:
         return False

def mark(row,column,count): # wpisywanie do tablicy na podanąpozycję
    global board

    if (count%2 ==0): #Player2
        board[row][column] = "O"
    if (count%2 !=0): #Player1
        board[row][column] = "X"

    return None

def check_win(horizontal,vertical): ##funkcja pomocnicza do funkcji has_won
    if horizontal == 3 or vertical == 3:
        #print("X wygrywa")
        winner = "X"
        return True,winner
    elif horizontal == -3 or vertical ==-3:
        #print("O wygrywa")
        winner = "O"
        return True,winner
    else:
        winner = "Żodyn"
        return False,winner


def check_diagonal(diagonal1,diagonal2):
    licznik1 = 0
    licznik2 = 0
    for i in range(0,3):
        if (diagonal1[i]== "X"):
            licznik1+=1
        elif(diagonal1[i]=="O"):
            licznik1-=1

        if (diagonal2[i]== "X"):
            licznik2+=1
        elif(diagonal2[i]=="O"):
            licznik2-=1

    if (licznik1 ==3 ) or (licznik2 ==3):
        #print("X wygrywa")
        winner = "X"
        return True,winner
    elif (licznik1 ==-3 ) or (licznik2 ==-3):
        #print("O wygrywa")
        winner = "O"
        return True,winner
    else:
        winner = "Żodyn"
        return False,winner

def check_HV(table):
     #HORIZONTAL and VERTICAL
    licznik=0
    for i in range(0,3):
        win = False
        horizontal = 0
        vertical = 0
        for j in range(0,3):
            licznik+=1
            if table[i][j] == "X":
                horizontal += 1
            elif table[i][j] =="O":
                horizontal -= 1
    
            if table[j][i] == "X":
                vertical += 1
            elif table[j][i] =="O":
                vertical -= 1

            isWIN,whoWIN = check_win(horizontal,vertical)
            if isWIN==True:
                win = True
                return isWIN,whoWIN
    return None,None

def check_DIAG(table):
 ####DIAGONAL
    diagonal1=[]
    diagonal2=[]
    matrix_size=(len(table))

    ####DIAGONAL1
    licznik1 = 0
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            licznik1+=1
            if i==j:
                pass
                diagonal1.append(table[i][j])

    #DIAGONAL2
    licznik2=0
    matrix_size=(len(table)-1)
    for i in range(matrix_size,-1,-1):
        licznik2 -=1
        for j in range(matrix_size,-1,-1):
            if matrix_size-i==j:
                #print(test[i][j])
                diagonal2.append(table[i][j])

    isWIN,whoWIN = check_diagonal(diagonal1,diagonal2)
    if isWIN==True:
                win = True
                #print("The winner is:",whoWIN)
                return isWIN,whoWIN

    return None,None

def has_won(table): #sprawdza stan gry

    isWIN,whoWIN = check_HV(table)
    if isWIN==True:
        return isWIN,whoWIN

    isWIN,whoWIN = check_DIAG(table)
    if isWIN==True:
        return isWIN,whoWIN


    return None,None

def is_full(table): #sprawdza czy tablica jest pełna
    fill=0
    for i in range(0,3):
        for j in range(0,3):
            if (table[i][j]=="O") or (table[i][j]=="X"):
                fill+=1
    
    if (fill==9):
        return True
    else:
        return False

def print_board(table): #wyświetlanie tablicy
    '''pierwsza wersja
    for i in range(0,3):
         for j in range(0,3):
             print(table[i][j],end=' ')
         print("\n")
    '''
    #nowe
    Color_O = '\x1b[1;34;40m'
    Color_X = '\x1b[2;32;40m'
    Color_empty = '\x1b[2;37;47m' 
    Color_end = '\x1b[0m'

    tablica =[[' ','1','2','3'], ['A','.','.','X'], ['B','.','.','.'],['C','.','.','.']]

    for i in range(0,3):
        for j in range(0,3):
            tablica[i+1][j+1] = table[i][j]

    for i in range(0,4):
         for j in range(0,4):
            if tablica[i][j]=="O":
                print("\t",Color_O,tablica[i][j],end=Color_end+" ")
            elif tablica[i][j]=="X":
                print("\t",Color_X,tablica[i][j],end=Color_end+" ")
            elif tablica[i][j]==".":
                print("\t",Color_empty,tablica[i][j],end=Color_end+" ")
            else:
                print("\t",tablica[i][j],end=' ')
         print("\n")
    print(Color_end)
        
'''
print-result(): # wyświetla rezultat końcowy
'''

def tictactoe_game(): #głowna funkcje z grą

    print_board(board)

    row,column,player = get_move()

    mark(row,column,player)

    isWIN,winner = has_won(board)
    
    if isWIN:
        return True, winner
    elif is_full(board):
        return False, "Full table"
    else:
        return None, None


result = None
while (result==None): #count<9

    os.system("cls || clear")
    result,result2 = tictactoe_game()

    #print("Count ",count)
    #input("")

os.system("cls || clear")
print_board(board)
print("\n")

Color_win = '\x1b[4;33;40m'
Color_draw = '\x1b[4;37;40m'  
Color_end = '\x1b[0m'

if result:
    print(Color_win,"The winner is Player",result2,Color_end)
    print("\n\n\n")
elif result==False:
    print(Color_draw,"The game is over - draw",Color_end)
    print("\n\n\n") 


############# TABELe DO TESTÓw

#horizontal
tab1 = [['O','O','O'], ['.','.','.'], ['.','.','.'],]
tab2 = [['.','.','.'], ['O','O','O'], ['.','.','.'],]
tab3 = [['.','.','.'], ['.','.','.'], ['O','O','O'],]
#vertical
tab4 = [['O','.','.'], ['O','.','.'], ['O','.','.'],]
tab5 = [['.','O','.'], ['.','O','.'], ['.','O','.'],]
tab6 = [['.','.','O'], ['.','.','O'], ['.','.','O'],]
#diagonal
tab7 = [['O','.','.'], ['.','O','.'], ['.','.','O'],]
tab8 = [['.','.','O'], ['.','O','.'], ['O','.','.'],]

#horizontal
tab1X = [['X','X','X'], ['.','.','.'], ['.','.','.'],]
tab2X = [['.','.','.'], ['X','X','X'], ['.','.','.'],]
tab3X = [['.','.','.'], ['.','.','.'], ['X','X','X'],]
#vertical
tab4X = [['X','.','.'], ['X','.','.'], ['X','.','.'],]
tab5X = [['.','X','.'], ['.','X','.'], ['.','X','.'],]
tab6X = [['.','.','X'], ['.','.','X'], ['.','.','X'],]
#diagonal
tab7X = [['X','.','.'], ['.','X','.'], ['.','.','X'],]
tab8X = [['.','.','X'], ['.','X','.'], ['X','.','.'],]


###############################TABELE DO TESTÓW end
#print(has_won(tab8X))

