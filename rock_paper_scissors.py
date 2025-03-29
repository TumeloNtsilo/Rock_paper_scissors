import random

class GameOptions:
    game_options = ["rock", "paper", "scissors"]

    def get_game_options(self):
        print("These are your game options:")
        for index, option in enumerate(self.game_options):
            print(f"{index}: {option}")
        print()

class Play:
    def __init__(self):
        self.results = []

    def player_turn(self):
        while True:
            try:
                choice = int(input(f"Use index number to make a choice {list(enumerate(GameOptions.game_options))}: "))
                if 0 <= choice < len(GameOptions.game_options):
                    self.player_choice = GameOptions.game_options[choice]
                    self.results.append(self.player_choice)
                    break
                print("Invalid choice, try again.")
            except ValueError:
                print("Invalid input, enter a number.")

    def computer_turn(self):
        self.computer_choice = random.choice(GameOptions.game_options)
        self.results.append(self.computer_choice)

    def display_results(self):
        print(f"Round results: {tuple(self.results)}\n")

class Winner:
    def __init__(self):
        self.player_score = 0
        self.comp_score = 0

    def score_count(self, results):
        player, computer = results  # Unpack tuple
        if (player, computer) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
            print("You win this round.")
            self.player_score += 1
        elif player == computer:
            print("It's a tie this round.")
        else:
            print("You lost this round.")
            self.comp_score += 1

    def display_score(self):
        print(f"Score - Player: {self.player_score} | Computer: {self.comp_score}\n")

    def display_winner(self):
        if self.player_score > self.comp_score:
            print("Congratulations! You won!!")
        elif self.player_score == self.comp_score:
            print("It's a tie!")
        else:
            print("You lose!!")

if __name__ == "__main__":
    options = GameOptions()
    options.get_game_options()

    winner = Winner()
    game = Play()

    for _ in range(3):
        game.results = [] 
        game.player_turn()
        game.computer_turn()
        game.display_results()
        winner.score_count(game.results)
        winner.display_score()

    winner.display_winner()
