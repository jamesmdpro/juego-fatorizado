import random


def choose_options():
    options = ("piedra" , "papel", "tijera")
    user_option =  input("""
Escribe tu selección, entre ( PIEDRA , PAPEL , TIJERA ):

 """)
    user_option = user_option.lower()
    
    if not user_option in options:
        print('esa opcion no es valida')
    # continue
    else:
        return None, None
    
    computer_option = random.choice(options)


def check_rules(user_option, computer_option, user_wins, computer_wins):
    
    if user_option == computer_option:
        print("Juego Empatado")
    elif user_option == "papel" and computer_option == "tijera":
        print("la computadora gana")
        computer_wins += 1 
    elif user_option == "papel" and computer_option == "piedra":
        print("le Ganaste a la computadora")
        user_wins += 1
    elif user_option == "tijera" and computer_option == "papel":
        print("le Ganaste a la computadora")
        user_wins += 1
    elif user_option == "tijera" and computer_option == "piedra":
        print("la computadora gana")
        computer_wins += 1 
    elif user_option == "piedra" and computer_option == "papel":
        print("la computadora gana")
        computer_wins += 1 
    elif user_option == "piedra" and computer_option == "tijera":
        print("le Ganaste a la computadora")
        user_wins += 1
    else:
        return None, None

def run_game():

    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        
        print("*" * 20)
        print("ROUND", rounds)
        print("*" * 20)
        print("WINS PC", computer_wins)
        print("WINS USER", user_wins)
        rounds += 1
# tienes un error el la 59 
        user_option, computer_option = choose_options()

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        check_winer(user_wins, computer_wins)
    

def check_winer(user_wins, computer_wins):
    if user_wins == 3:
        print("EL GANADOR ES EL USUARIO")
        exit()
    if computer_wins == 3:
        print("LA COMPURADORA GANA")
        exit()
        
run_game()


  
