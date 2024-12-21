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
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high(h), too low (L), or correct(C)??')
        if feedback == 'h':
            high = guess -1 
        elif feedback == 'l':
            low = guess + 1
    print(f' Yay! The computer guessed your number, {guess}, correctly')
        
computer_guess(1000)