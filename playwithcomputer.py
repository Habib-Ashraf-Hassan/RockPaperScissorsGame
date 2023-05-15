
def main_play():
    import random
    series = input("Enter the number of rounds: ")

    computer_choices = "RSP"

    player_wins, computer_wins = 0, 0

    while series.isnumeric() is False:
        series = input("Enter the number of rounds: ")
    else:
        series = int(series)
        for i in range(series):
            print()
            print(f"Round {i + 1}".center(17, "-"))
            player = input("Enter your choice(R/S/P) R:rock S: scissors P:paper : ").upper()
            computer = random.choice(computer_choices)
            while player not in computer_choices:
                player = input(
                    "Invalid choice was entered!!enter your choice(R/S/P) R:rock S: scissors P:paper : ").upper()

            if player == computer:
                print(f"Its a DRAW!! Player:{player} Computer:{computer}")
            elif (player == "R" and computer == "S") or (player == "P" and computer == "R") or (
                    player == "S" and computer == "P"):
                player_wins += 1
                print(f"You WIN this round!! Player:{player} Computer:{computer}")
            else:
                computer_wins += 1
                print(f"You LOSE this round!! Player:{player} Computer:{computer}")

        print()

        if player_wins == computer_wins:
            print(f"IT was a TIE 🙂 You:{player_wins}-Computer:{computer_wins}")
        elif player_wins > computer_wins:
            print(f"You WON 🥳 You:{player_wins}-Computer:{computer_wins}")
        else:
            print(f"You LOST ☹️ You:{player_wins}-Computer:{computer_wins}")
