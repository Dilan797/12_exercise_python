from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        #Creamos un tablero de 9 espacios
        self.board = [' ' for _ in range(9)]
        #Definimos al ganador
        self.current_winner = None
    #Creamos un metodo que recibe un parametro letter
    def print_board(self):
        #Mostramos el tablero
        #Este código crea la representación visual del tablero Tic-Tac-Toe. Analicemos cómo funciona:
        for row in [self.board[i*3:(i+1)*3]for i in range (3)]:
            print('| '+ ' |'.join(row) + ' |')
    
    #Creamos un metodo que recibe un parametro num y letter
    @staticmethod#Metodo estatico
    #Metodo que recibe un parametro num y letter
    def print_board_nums():
        #Mostramos el tablero con los numeros
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        #Mostramos el tablero con los numeros
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')    
    #Creamos un metodo que recibe un parametro square, letter
    def avaible_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    #Creamos un metodo que recibe un parametro square, letter
    def empty_squares(self):
        #Retornamos si hay espacios vacios
        return ' ' in self.board 
    #Creamos un metodo que recibe un parametro square, letter
    def num_empty_squares(self):
        #Retornamos el numero de espacios vacios
        return self.board.count(' ')
    #Creamos un metodo que recibe un parametro square, letter
    def make_move(self, square, letter):
        #Si el cuadrado es valido
        if self.board[square] == ' ':
            #Colocamos la letra en el cuadrado
            self.board[square] = letter
            if self.winner(square, letter):#Si hay un ganador
                #Definimos al ganador 
                self.current_winner = letter
            #Si hay un ganador
            return True
        #Si no hay un ganador
        return False

    #Creamos un metodo que recibe un parametro square, letter
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        #Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square % 2 == 0:
            #Diagonal de izuiqerda a derecha
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all ([spot == letter for spot in diagonal1]):
                return True
            #Diagonal de derecha a izquierda
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all ([spot == letter for spot in diagonal2]):
                return True 
        return False
    
#Creamos una funcion que recibe un parametro game, x_player, o_player y print_game
def play(game, x_player, o_player, print_game=True):
    #Si print_game es verdadero
    if print_game:
        #Mostramos los numeros del tablero 
        game.print_board_nums()
    
    letter = 'X' #Empezamos con la X
    #Mientras haya espacios vacios
    while game.empty_squares():
        #Si la letra es O
        if letter == 'O':
            #Si el jugador es O
            square = o_player.get_move(game)
            #Si el jugador es X
        else:
            #Si el jugador es X
            square = x_player.get_move(game)
        pass#Hacemos un movimiento
        #Si se hace un movimiento
        if game.make_move(square, letter):
            #Si print_game es verdadero
            if print_game:
                #Mostramos el tablero
                print(letter + f' makes a move to square {square}')
                game.print_board()#Mostramos el tablero
                #Mostramos una linea vacia
                print('')#just empty line
                #Si hay un ganador
                if game.current_winner:
                    #Si hay un ganador
                    if print_game:
                        #Mostramos el ganador
                        print(letter + ' wins!')
                    return letter#Retornamos la letra
            #Si hay un ganador
            letter = 'O' if letter == 'X' else 'X' 
    #Si print_game es verdadero
    if print_game:
        #Mostramos un mensaje
        print('It\'s a tie!')
            
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)