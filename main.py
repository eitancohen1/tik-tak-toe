import os

def print_board(board):   
    cut=1

    print('-----------------')
    for k in board:
        print ('|',end=" ")
        print (k,end=" ")
        print ('|',end=" ")
        cut=cut+1
        if cut>3:               
            print()
            print('-----------------')
            cut=1   

def check_position(p):
    if not p.isdigit():
        return 1
    else:
        return 0
# b- index in board
# y- the player mark
def fill_board(b,y):
    board[b-1]=y
    
    
def chack_game():
    if  chek_rull(board)==1:
        print('x player won')
        
        restart()
        
        
    elif chek_rull(board)==2:
        print('o player won')
        
        restart()
    
    elif chek_rull(board)==3:
        print('tiko')
        
        restart()
        
def restart():
    r=input("do you wont play again y/n: ")
    if r=="n":
        exit()
    else:
        os.system('cls')
        main("y")
        

    

        
        
    
    
def chek_rull(r):
    
    if board[0]=="x" and  board[1]=="x" and  board[2]=="x":
        return 1
    elif board[0]=="o" and  board[1]=="o" and  board[2]=="o":
        return 2   

    if board[3]=="x" and  board[4]=="x" and  board[5]=="x":
        return 1
    elif board[3]=="o" and  board[4]=="o" and  board[5]=="o":
        return 2   
    
    if board[6]=="x" and  board[7]=="x" and  board[8]=="x":
        return 1
    elif board[6]=="o" and  board[7]=="o" and  board[8]=="o":
        return 2    

    if board[0]=="x" and  board[3]=="x" and  board[6]=="x":
        return 1
    elif board[0]=="o" and  board[3]=="o" and  board[6]=="o":
        return 2    

    if  board[1]=="x" and  board[4]=="x" and  board[7]=="x":
        return 1
    elif board[1]=="o" and  board[4]=="o" and  board[7]=="o":
        return 2    
    if  board[2]=="x" and  board[5]=="x" and  board[8]=="x":
        return 1    
    elif board[2]=="o" and  board[5]=="o" and  board[8]=="o":
        return 2   
    if  board[0]=="x" and  board[4]=="x" and  board[8]=="x":
        return 1
    elif  board[0]=="o" and  board[4]=="o" and  board[8]=="o":
        return 2    
    if  board[2]=="x" and  board[4]=="x" and  board[6]=="x":
        return 1  
    elif board[2]=="o" and  board[4]=="o" and  board[6]=="o":
        return 2
    
    if board[0]!=1 and  board[1]!=2 and  board[2]!=3 and  board[3]!=4 and  board[4]!=5 and  board[5]!=6 and  board[6]!=7 and  board[7]!=8 and  board[8]!=9  :
       return 3



def main(a):
    
    print("Welcome to x and o game")
    global board
    board=[1,2,3,4,5,6,7,8,9]
    
    print_board(board)
    
    while a=="y":
        #xp - x position
        xp=input("Enter position for x: ")
        
        while  check_position(xp):
            xp=input('wrong input choose please location you want to mark x player: ')
        xp=int(xp)
        
        while board[xp-1]=='x'or board[xp-1]=='o':
            xp=int(input('The place is already occupied try x again: '))
        
        fill_board(xp,'x')
        os.system('cls')
        print_board(board)
        chack_game()
    
        
        op=input("Enter position for o: ")
        
        while  check_position(op):
            op=input('wrong input choose please location you want to mark o player: ')
        op=int(op)
        
        while board[op-1]=='x'or board[op-1]=='o':
            op=int(input('The place is already occupied try o again: '))
            
        fill_board(op,'o')
        os.system('cls')
        print_board(board)
        chack_game()

main("y")


#op - o position
#p -position


