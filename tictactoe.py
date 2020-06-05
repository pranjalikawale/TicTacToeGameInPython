import os 
import random
import time

class TicTacToe:
    #board   
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
    player={'HUMAN':'O','COMPUTER':'O'}
    game_on=True
    counter=0
    game_win=0
    list=[1,2,3,4,5,6,7,8,9]
    current_player=''

    #This Function Draws Game Board    
    def draw_board(self):    
        print(self.board[1]+" |"+self.board[2]+" |"+self.board[3])   
        print("__+__+__")    
        print(self.board[4]+" |"+self.board[5]+" |"+self.board[6])    
        print("__+__+__")   
        print(self.board[7]+" |"+self.board[8]+" |"+self.board[9])   
         

    # assign symbol to player
    def assign_symbol(self):
        if random.random()<0.5:
            self.player['HUMAN']='X'
        else:
            self.player['COMPUTER']='X'

    # display symbol to player
    def display_symbol(self):
        for current_players in self.player : 
            print("\n"+self.player[current_players]+" : "+current_players) 

    # toss 
    def toss(self):
        if random.random()<0.5:
            self.current_player='HUMAN'
        else:
            self.current_player='COMPUTER'
        print(self.current_player+" "+self.player.get(self.current_player)+" won toss and play first")

    # switch player turn
    def switch_player(self):
        if self.current_player =='HUMAN':
            self.current_player='COMPUTER'
        else:
            self.current_player='HUMAN'

        if self.game_on == True :
            print(self.current_player +" turn:")
    
    #This Function Checks position is empty or not    
    def is_empty(self,position):    
        if(self.board[position] == ' '):    
            return True    
        else:    
            return False    
    
    #This Function Checks player has won or not    
    def check_win(self):        
        
        if self.game_win==0:
            #Horizontal winning condition   
            self.check_row()
        if self.game_win==0:
            #Vertical Winning Condition    
            self.check_col()
        if self.game_win==0:
            #Diagonal Winning Condition    
            self.check_diagonal()       

    #Horizontal winning condition 
    def check_row(self):   
        if(self.board[1] == self.board[2] and self.board[2] == self.board[3] and self.board[1] != ' '):    
            self.game_win = 1   
        elif(self.board[4] == self.board[5] and self.board[5] == self.board[6] and self.board[4] != ' '):    
            self.game_win = 1    
        elif(self.board[7] == self.board[8] and self.board[8] == self.board[9] and self.board[7] != ' '):    
            self.game_win = 1    

    #Vertical Winning Condition
    def check_col(self):  
        if(self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != ' '):    
            self.game_win = 1    
        elif(self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != ' '):    
            self.game_win = 1    
        elif(self.board[3] == self.board[6] and self.board[6] == self.board[9] and self.board[3] != ' '):    
            self.game_win = 1    

    #Diagonal Winning Condition
    def check_diagonal(self):
        if(self.board[1] == self.board[5] and self.board[5] == self.board[9] and self.board[5] != ' '):    
            self.game_win = 1    
        elif(self.board[3] == self.board[5] and self.board[5] == self.board[7] and self.board[5] != ' '):    
            self.game_win = 1    

    #Check for tie
    def ckeck_tie(self):
            print("-----------Game is tie-----------")
            self.game_on=False

    #Insert symbol in board
    def placed_mark_in_board(self,choice):
            self.board[choice] = self.player.get(self.current_player) 
            self.counter+=1  
            self.check_win()
            if self.counter>=9 and self.game_win==0: 
                self.ckeck_tie() 

    def get_input(self):
        choice=-1
        while True:
            if self.current_player=='HUMAN':
                try:
                    choice = int(input("Enter the position between [1-9] where you want to mark : "))
                    if choice in self.list and self.is_empty(choice):
                        break
                    else:
                        print("Spot is taken/invalid")
                except ValueError:
                    print("Plz enter valid number") 
            else:
                choice=random.randint(1,10)
                if self.is_empty(choice):
                    time.sleep(3)
                    break
        self.placed_mark_in_board(choice)

    def tic_tac_toe(self):
        os.system('cls')    
        self.draw_board()   
        self.assign_symbol()
        self.display_symbol()
        self.toss()
        while self.game_on == True:
            self.get_input()
            self.draw_board()
            if self.game_win==1:
                print("------------"+self.current_player+" is won ------------")
                self.game_on=False    
            if self.game_on==True:
                self.switch_player()
        

game=TicTacToe()
game.tic_tac_toe()                
  