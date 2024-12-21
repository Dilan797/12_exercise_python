#En este ejercicio creamos una función para manejar un número 
# que la maquina genere por medio de la iteracion random
# string concatenetion 
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    #Creamos un loop    
    while guess != random_number:
        #Creamos la entrada 
        guess = int(input(f'Guess a number between 1 and {x}: '))
        #Añadimos la lógica 
        if guess < random_number:
            print('Sorry, guess again, Too low.')
        elif guess > random_number:
            print('Sorry guess agaiin, To high.')
    print(f'Yay, congrats. You have guessed the number {random_number} congratulation!!!')

#Ahora crearemos el programa para que la maquina adivine el número que estamos pensando
def computer_guess(x):
    #Paramentro de los  limites de los núemros a a divinar 
    low = 1
    high = x
    #Creamos un loop para que la maquina adivine el número
    feedback = ''
    #Este ciclo se repite hasta que digitemos 'c'
    while feedback != 'c':
        #Creamos la lógica para que la maquina adivine el número
        guess = random.randint(low, high)
        # Input
        feedback = input(f'Is {guess} too high(h), too low (L), or correct(C)??: ')
        #Logica con la que toma la lógica la maquina
        if feedback == 'h':
            high = guess -1 
        elif feedback == 'l':
            low = guess + 1
    print(f' Yay! The computer guessed your number, {guess}, correctly')        
computer_guess(1000)    