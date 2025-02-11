import random

class GameOptions:

    game_options = ["rock", "paper", "scissors"]

    def get_game_options(self):
        print("These are your game options:")
        for index,option in enumerate(self.game_options):
            print(f"{index}: {option}")

        print()

class Play():
    score = [0, 0]

    def __init__(self) -> None:
        self.results = []

    def playerturn(self):
        while True:
            try:
                self.player_turn = int(input(f"Use index number from to make a choice {list(enumerate(GameOptions.game_options))}: "))
                if 0 <= self.player_turn < len(GameOptions.game_options):
                    break
                print("Invalid choice, try again.")
            except ValueError:
                print("Invalid input, enter a number.")



        self.player_choice = GameOptions.game_options[self.player_turn]
        self.results.append(self.player_choice)

    def computerturn(self):
        self.computer_choice = random.choice(GameOptions.game_options)
        self.results.append(self.computer_choice)

    def display_results(self):
        print(f"round results: {tuple(self.results)}")
        print()

class Winner():

    def __init__(self) -> None:
        self.player_score = 0
        self.comp_score = 0

    def score_count(self, results):
        if results in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
            print("You win this round.")
            self.player_score += 1
        
        elif results[0] == results[1]:
            print("It's a tie on this round.")
            self.player_score += 1
            self.comp_score += 1

        else:
            print("You lost this round.")
            self.comp_score += 1

    def dispay_score(self):
        print(f"Player {self.player_score} : {self.comp_score} Computer")
        print()

    
    def display_winner(self):
        if self.player_score > self.comp_score:
            print("Congratulations you won!!")

        elif self.player_score == self.comp_score:
            print("It's a tie!")

        else:
            print("You lose!!")



if __name__ == "__main__":

    options = GameOptions()
    options.get_game_options()


    winner = Winner()

    for game in range(3):
        game = Play()
        game.playerturn()
        game.computerturn()
        game.display_results()
        winner.score_count(game.results)
        winner.dispay_score()
    
    
    winner.display_winner()