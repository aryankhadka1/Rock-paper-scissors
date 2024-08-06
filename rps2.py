import random
while True:
#inputing number of rounds
    rounds_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    rounds = None
    
    while rounds not in rounds_choices:
        rounds = input("Enter the number of rounds(1-10): ")
    rounds_userinput = int(rounds)
    i = 0
    your_score = 0
    computer_score = 0

    while i < rounds_userinput:
#getting user choice
        choices = ["rock", "paper", "scissors"]
        n = None

        while n not in choices:
            n = input("Choose (rock/paper/scissors): ").lower()
        print("Your choice: " + n)
#getting computer choice
        game = ["rock", "paper", "scissors"]
        random_choice = random.choice(game)
        print("Computer's choice: " + random_choice)
#game logic
        if n == random_choice:
            print("Draw\n  ")
        elif (n == "rock" and random_choice == "scissors") or (n == "paper" and random_choice == "rock") or (n == "scissors" and random_choice == "paper"):
            print("Win\n  ")
            your_score += 1
        else:
            print("Loss\n  ")
            computer_score += 1
        i+=1
#finalizing the winner
    print("Your final score: ", your_score)
    print("Computer's final score: ", computer_score)
    if your_score > computer_score:
        print("\nCongratulations! YOU WON")
    elif your_score == computer_score:
        print("\nPretty good! GAME DRAW")
    else:
        print("\nBetter luck next time! YOU LOST")
#asking user to try again
    try_again = input("Do you want to try again?(yes/no): ").lower()
    if try_again != "yes":
        break