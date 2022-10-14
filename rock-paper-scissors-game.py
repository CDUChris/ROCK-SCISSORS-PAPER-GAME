# import random for computer use later
import random
#declare the initial status of  player,computer, tie situation, choices(including data of the choices) and quit game(boolean)
#class the whole program as a Game 
class Game:
    def __init__(self):
        self.player = 0
        self.computer=0
        self.tie=0
        self.choice=['rock','paper','scissors']
        self.is_quit = False
#define the game_end rules and tie situation
    def is_end(self):
        if self.player >=5:
            return True, 'player'
        elif self.computer >=5:
            return True, 'computer'
        return False,None
#point calculation method description
#tie situation
    def game_once(self,player,computer):
        if player == computer:
            self.tie+=1
            return 'tie'
#computer or player win situation 
        else:
            if self.judge(player,computer):
                self.player+=1
                return 'player'
            else:
                self.computer +=1
                return 'computer'
#function part, the rules of the game itself in each situation
    def judge(self,player,computer):
        if player=='rock':
            if computer=='scissors':
                return True
            if computer=='paper':
                return False
        elif player=='scissors':
            if computer=='paper':
                return True
            if computer=='rock':
                return False
        elif player=='paper':
            if computer=='rock':
                return True
            if computer=='scissors':
                return False
#wrong input feedback
    def is_legal(self,player):
        if player not in self.choice:
            return False
        return True

    def random_choice(self):
        return random.choice(self.choice)
#game display module
    def game(self):
        while True:
            print('-------------------')
#user input, upper and lower case are both accepted 
            player = input('rock, paper or scissors: ').lower()
#wrong input feedback
            if not self.is_legal(player):
                print('input is wrong')
                continue
            computer = self.random_choice()
#game win situation description, including 5 times tie
#calculate the points of player,computer, tie and times of game
            who_win = self.game_once(player,computer)
            if who_win != "tie":
                print(f'The winner of this round is {who_win},computer choice: {computer}, your choice: {player}')
            else:
                print(f"this turn is tie, computer choice: {computer}, your choice: {player} ")
            print(f'scores: player: {self.player},computer: {self.computer},tie: {self.tie},total game: {self.player + self.computer+self.tie}')
#output the final result
            is_game_end,winner=self.is_end()
            if is_game_end:
                print(f'the winner of the game is {winner} total game:{self.player+self.computer+self.tie}')
                break
#method to realise 'Player can also quit the game at any time.'                
            c = input("is single game continue?")
            if c == "no":
                self.is_quit = True
                break
        return
#restart the game when user does not choose 'no' after winner appeared
def main():
    while True:
        g = Game()
        g.game()
        if g.is_quit:
            break
        c = input("is continue?")
        if c == "no":
            break
    print("real end")
#excute the program
if __name__=='__main__':
    main()            