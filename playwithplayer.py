
def main_play():
    series = input("Enter the number of rounds: ")

    choices = "RSP"

    player1_wins, player2_wins = 0, 0

    while series.isnumeric() is False:
        series = input("Enter the number of rounds: ")
    else:
        series = int(series)
        for i in range(series):
            print()
            print(f"Round {i+1}".center(17, "-"))
            player1 = input("      Player1     \nEnter your choice(R/S/P) R:rock S: scissors P:paper : ").upper()

            while player1 not in choices:
                player1 = input("Player1     \nInvalid choice was entered!!enter your choice(R/S/P) R:rock S: scissors "
                                "P:paper : ").upper()

            player2 = input("      Player2     \nEnter your choice(R/S/P) R:rock S: scissors P:paper : ").upper()

            while player2 not in choices:
                player2 = input("Player2     \nInvalid choice was entered!!enter your choice(R/S/P) R:rock S: scissors "
                                "P:paper : ").upper()

            if player1 == player2:
                print(f"Its a DRAW!! Player1:{player1} Player2:{player2}")
            elif (player1 == "R" and player2 == "S") or (player1 == "P" and player2 == "R") or (
                    player1 == "S" and player2 == "P"):
                player1_wins += 1
                print(f"Player1 WINS this round!! Player1:{player1} Player2:{player2}")
            else:
                player2_wins += 1
                print(f"Player2 WINS this round!! Player:{player1} Player2:{player2}")

        print()

        if player1_wins == player2_wins:
            print(f"IT was a TIE!! Player1:{player1_wins} - Player2:{player2_wins}")
        elif player1_wins > player2_wins:
            print(f"Player1 WINS!! Player1:{player1_wins} - Player2:{player2_wins}")
        else:
            print(f"Player2 WINS!! Player1:{player1_wins} - Player2:{player2_wins}")
