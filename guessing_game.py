import random

def start_game():
    attempts = 0
    #magic_number = 2
    magic_number = random.randint(1, 10)
    high_score = 100
    lines = ("-" * 34)
    print(lines+"\nWelcome to Number Guessing Game!!!\n"+lines+"\n")
    while True:  
        pg = 100
        player_guess = input("Pick a number between 1 and 10: ")
        try:
            pg = int(player_guess)
            if (pg > 10) or (pg < 1):
                print("Invalid input. Please choose a number between 1 and 10\n")
                continue
        except ValueError:
            print("Invalide input. Please use a numaric value.\n")
            continue
        attempts += 1
        if pg > magic_number:
            print("The Number is lower\n")
            
        if pg <  magic_number:
            print("The Number is Higher\n")
            
        if pg == magic_number:
            print("You did it! It took you {} attempt(s).".format(attempts))
            if high_score > attempts:
                print("You have the High Score:{} attempt(s)\n".format(attempts))     
                high_score = attempts
            if high_score < attempts:
                print("You didn't beat the current High Score of {} attempt(s)\n".format(high_score))       
            while True:            
                play_again = input("\nWould you like to play again? Yes/No: ")
                answer = play_again.lower()
                if answer == "yes":
                    print("\n\n\n"+lines+"\n           New Game")
                    print("The current High Score is {} attempt(s).\n".format(high_score)+lines)
                    start_game()
                if answer == "no":
                    break
                else:
                    print("Please enter Yes or No.")

            print("Well thank you for playing")
            break
            
start_game()