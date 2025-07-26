def introduction():
    print("""
        Welcome to my game engine.
        Good to have you here.
            😃😃😃
        Enter the word help for more details.
    """)
def game_engine():
    command = ""
    started = False # The car is initially stopped
    while True:
        command = input(":>>: ")
        if command == "start":
            if started:
                print("Car has already started")
            else:
                started = True
                print("Car started successfully.")
        elif command == "stop":
            if not started:
                print("Car has not started")
            else:
                started = False
                print("Car has stopped.")
        elif command == "help":
            print("""
        start - Start's the car.
        stop - Stop's the car.
        help - Gives the instructions.
        """)
        elif command == "quit":
            option = input("You sure you want to quit the game🙂[Yes/No] :>>: ").lower()
            if option == "yes":
                print("""
                See you next time
                😉🙂🙂🙂🙂😉
                """)
                break
            else:
                game_engine()
        else:
            print("Sorry☹, I do not understand that.")

introduction()
game_engine()
