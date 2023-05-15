import playwithplayer as pl
import playwithcomputer as cp

print("Rock Paper Scissors Game".center(36, "*"))
main_menu_choice = ""

while main_menu_choice != "3":
    print()
    print("Main menu".center(19, "*"))
    main_menu_choice = input("Enter your choice(choose 1/2/3 only)\n1. 1 Player(Vs Computer)\n2."
                             " 2 players\n3. Exit the game\n>>: ")
    if main_menu_choice == "1":
        print()
        print("Playing Vs Computer".center(32, "-"))
        sub_menu_choice = "1"
        while sub_menu_choice != "2":
            sub_menu_choice = input("Do you wish to continue(choose 1/2 only)\n1. Yes(Proceed to play)\n2."
                                    " No(Go back)>>: ")
            if sub_menu_choice == "1":
                print()
                cp.main_play()
            elif sub_menu_choice == "2":
                break
            else:
                print()
                print("Invalid Choice entered, Please try again !!")

    elif main_menu_choice == "2":
        print()
        print("2 player".center(17, "-"))
        sub_menu_choice = "1"
        while sub_menu_choice != "2":
            sub_menu_choice = input("Do you wish to continue(choose 1/2 only)\n1. Yes(Proceed to play)\n2."
                                    " No(Go back)>>: ")
            if sub_menu_choice == "1":
                print()
                pl.main_play()
            elif sub_menu_choice == "2":
                break
            else:
                print()
                print("Invalid Choice entered, Please try again !!")

    elif main_menu_choice == "3":
        print("You EXIT the game 👍")
        break
    else:
        print()
        print("Invalid Choice entered, Please try again !!")
