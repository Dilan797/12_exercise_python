import random

def play():
    user = input("What is yout choice? 'r' for Rock, 'p' for papper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])
    #Logica para empate 
    if user == computer:
        return 'It is a tie'
    #r > s, s > p, p > r
    if is_win(user, computer):
        return 'You Won!'
    
    return 'You Lost!'
    
def is_win(player, opponent):
    #retrurn true if player wins
    #r > s, s > p, p > r
    if(player == 'r' and opponent == 's') or (player == "s" and opponent == "p")\
        or (player == "p" and opponent == "r"):
            return True
print(play())