import random


class Client:
    def pick_random_puzzle(self, puzzles):
        return puzzles[random.randint(0, len(puzzles) - 1)]
