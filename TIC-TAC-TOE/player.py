import math
import random
# Construimos una clase Player
class Player:
    #Con un constructor que recibe un parametro letter
    def __init__(self, letter):
        #letteris x or o
        self.letter = letter
        
    #Creamos un metodo que recibe un parametro game
    def get_move(self, game):
        #Retornamos la letra
        pass
#Creamos una clase HumanPlayer que hereda de Player
class RandomComputerPlayer(Player):
    def __init__(self, letter):#Constructor
        super().__init__(letter)#Llamamos al constructor de la clase padre
    #Metodo que recibe un parametro game
    def get_move(self, game):
        square = random.choice(game.avaible_moves())
        return square
    
#Creamos una clase HumanPlayer que hereda de Player
class HumanPlayer(Player):
    def __init__(self, letter):#Constructor
        super().__init__(letter)#Llamamos al constructor de la clase padre
    #Metodo que recibe un parametro game
    def get_move(self, game):
        #Creamos una variable valid_square
        valid_square = False
        #Creamos una variable val
        val = None
        #Mientras no sea un cuadrado valido
        while not valid_square:
            #Pedimos un cuadrado el cual va de 0 a 8
            
            square = input(self.letter + '\'s turn. Input move (0-8): ')

            #Intentamos convertir el cuadrado en un entero
            try:                
                val = int(square)
                #Si el cuadrado no esta en los movimientos disponibles
                if val not in game.avaible_moves():
                    #Levantamos una excepcion
                    raise ValueError
                #Si el cuadrado esta en los movimientos disponibles
                valid_square = True
            #Si el cuadrado no es valido
            except ValueError:
                #Mostramos un mensaje
                print('Invalid square. Try again.')
        
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        if len(game.avaible_moves()) == 9:
            square = random.choice(game.avaible_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        
        
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        for possible_move in state.avaible_moves():
            state.make_move(possible_move, player)  
            sim_score = self.minimax(state, other_player)
            
            
            
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else: 
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best 