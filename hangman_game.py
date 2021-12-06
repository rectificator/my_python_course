import os
import random as rn


def print_welcome_message():
    os.system("clear")    
    welcome_message = """ 
    #  *___**___***________***________****________***_____*______****________***________***********________***________***_____*______****_______******
    #  |\**\|\**\*|\***__**\*|\***___**\*|\***____\*|\***_*\**_***\*|\***__**\*|\***___**\********|\***____\*|\***__**\*|\***_*\**_***\*|\**___*\*****
    #  \*\**\\\**\\*\**\|\**\\*\**\\*\**\\*\**\___|*\*\**\\\__\*\**\\*\**\|\**\\*\**\\*\**\*******\*\**\___|*\*\**\|\**\\*\**\\\__\*\**\\*\***__/|****
    #  *\*\***__**\\*\***__**\\*\**\\*\**\\*\**\**___\*\**\\|__|*\**\\*\***__**\\*\**\\*\**\*******\*\**\**___\*\***__**\\*\**\\|__|*\**\\*\**\_|/__**
    #  **\*\**\*\**\\*\**\*\**\\*\**\\*\**\\*\**\|\**\\*\**\****\*\**\\*\**\*\**\\*\**\\*\**\*******\*\**\|\**\\*\**\*\**\\*\**\****\*\**\\*\**\_|\*\*
    #  ***\*\__\*\__\\*\__\*\__\\*\__\\*\__\\*\_______\\*\__\****\*\__\\*\__\*\__\\*\__\\*\__\*******\*\_______\\*\__\*\__\\*\__\****\*\__\\*\_______\\
    #  ****\|__|\|__|*\|__|\|__|*\|__|*\|__|*\|_______|*\|__|*****\|__|*\|__|\|__|*\|__|*\|__|********\|_______|*\|__|\|__|*\|__|*****\|__|*\|_______|
    #  ***********************************************************************************************************************************************
    #  ***********************************************************************************************************************************************
    #  ***********************************************************************************************************************************************
    """
    print(welcome_message)


def verify_victory(victory, lives, secret_word_mask):
    os.system("clear")
    
    if victory:
        print("\n\n///////////////////////",secret_word_mask,"///////////////////////")
        input("""
                        ¡VICTORIA!
        Introduce cualquier otro valor para continuar 
        """)
    elif victory == False and lives == 0:
        draw_hangman(lives)
        input("""
        Has Perdido (┬┬﹏┬┬)
        Introduce cualquier otro valor para continuar 
        """)




def search_in_list(item_to_search,my_list):
    for item in my_list:
        if item == item_to_search:
            return True
    return False



def replace_letter_mask(user_input, secret_word, secret_word_mask):
    mask = []
    for index in range(len(secret_word)):
        if user_input == secret_word[index]:
            mask.append(user_input)
        else:
            mask.append(secret_word_mask[index*2])
    return " ".join(mask)

def print_char_instruction(attempt):
    if attempt != 0:
        return """ 
            Prueba con otra letra
             """
    else:
        return """ 
            Prueba con una letra
             """

def draw_hangman(number):
    assert number >= 0 and number < 8, ValueError("Introduce un valor númerico válido")
    hangman = """ 
       _________
       ||-------     
       ||     ||
       ||     ||
       ||    (°°)
       ||   __TT__
       ||  //.  .\\\\
       || // |  | \\\\
       ||   //  \\\\
       ||  //    \\\\
       || //      \\\\
     """
    hangman_1 = """ 
       _________
       ||-------     
       ||     ||
       ||     ||
       ||    (°°)
       ||   __TT__
       ||  //.  .\\\\
       || // |  | \\\\
       ||   //  
       ||  //   
       || //    
     """

    hangman_2 = """ 
       _________
       ||-------     
       ||     ||
       ||     ||
       ||    (°°)
       ||   __TT__
       ||  //.  .\\\\
       || // |  | \\\\
       ||   
       ||  
    ___||___  
    ________       
          
          
     """

    hangman_3 = """ 
       _________
       ||-------     
       ||     ||
       ||     ||
       ||    (°°)
       ||   __TT__
       ||  //.  .
       || // |  |
       ||   
       ||  
    ___||___  
    ________    
         
         
     """

    hangman_4 = """ 
       _________
       ||-------     
       ||     ||
       ||     ||
       ||    (°°)
       ||   __TT__
       ||    .  .
       ||    |  |
       ||   
       ||  
    ___||___  
    ________   
        
        
     """

    hangman_5 = """ 
       _________
       ||-------     
       ||     ||
       ||     ||
       ||    (°°)
       ||   __TT__
       || 
       || 
       ||   
       ||  
    ___||___  
    ________     
          
          
     """

    hangman_6 = """ 
       _________
       ||-------     
       ||     ||
       ||     ||
       ||    (°°)
       || 
       || 
       || 
       ||   
       ||  
    ___||___  
    ________  
     """

    hangman_7 = """ 
       _________
       ||-------     
       ||     ||
       ||     ||
       || 
       || 
       || 
       || 
       ||   
       ||  
    ___||___  
    ________      
          
     """

    if number == 0:
        return hangman
    elif number == 1:
        return hangman_1
    elif number == 2:
        return hangman_2
    elif number == 3:
        return hangman_3
    elif number == 4:
        return hangman_4
    elif number == 5:
        return hangman_5
    elif number == 6:
        return hangman_6
    elif number == 7:
        return hangman_7
    else:
        pass


def word_mask(word):
    mask = []
    assert word.isalpha(), TypeError("Solo puedes introducir caracteres alfabéticos")
    for char in word:
        mask.append("_")
    return " ".join(mask)


def random_word():
    w = words()
    assert w != [], IndexError("No hay palabras disponibles")
    num = rn.randint(0, len(w))
    return w[num].strip()



def words():
    words = []
    try:
        with open("./hangman_game/data.txt", "r", encoding="utf-8") as f:
            
            for line in f:
                words.append(line)
    except FileNotFoundError:
        print("No se pudo localizar el archivo")
    return words

def run():
    
    while True:
        lives = 7;
        victory = False
        attempts = 0

        instruction_1 = """ 
    Adivina la palabra
        """

        secret_word = random_word()
        secret_word_mask = word_mask(secret_word)
        print_welcome_message()
        

        start = input("""
                
                "S" comenzar a jugar 
                
                
                "E" para salir 
                
                 """)
        if start == "S" or start == "s":
            while lives > 0 and victory == False:
                os.system("clear")
                print(instruction_1)
                try:
                    print(draw_hangman(lives),secret_word_mask)
                except AssertionError:
                    print("Has Perdido (┬┬﹏┬┬)")
                    

                user_attempt = input(print_char_instruction(attempts))
                attempts+=1

                letter_exist = search_in_list(user_attempt, secret_word)
                if letter_exist:
                    secret_word_mask = replace_letter_mask(user_attempt, secret_word, secret_word_mask)
                else:
                    lives-=1

                victory = secret_word_mask.replace(" ","") == secret_word

                verify_victory(victory,lives, secret_word_mask)
                

        elif start == "E" or start == "e":
            break
        else:
            print("Introduce un opción válida")


if __name__ == '__main__':
    run()