
import random
def play():
    user_inp = input("Enter a choice (rock, paper, scissors): ")
    computer_sel = random.choice(["rock", "paper", "scissors"])

    print(f"\nUser chose {user_inp}, computer chose {computer_sel }.\n")

    if user_inp == computer_sel :
        print("It's a tie!")
    elif user_inp == "rock":
        if computer_sel  == "scissors":
            print("Rock beats scissors! User wins!")
        else:
            print("Paper beats rock! Computer wins!")
    elif user_inp == "paper":
        if computer_sel  == "rock":
            print("Paper beats rock! User wins!")
        else:
            print("Scissors beats paper! Computer wins!")
    elif user_inp == "scissors":
        if computer_sel  == "paper":
            print("Scissors beats paper! User wins!")
        else:
            print("Rock beats scissors! Computer wins!")

    play_again = input("\nPlay again? (yes/no): ")
    if play_again.lower() == "yes":
        play()
    else:
        print("Thanks for playing!")

play()

