MAX_GUESSES = 5


class GuessingGame:

    def __init__(self, max_guesses=MAX_GUESSES):
        self.guesses = []
        self.max_guesses = max_guesses
        ...

    def guess(self):
        ...

    def __call__(self):
        """Entry point to the game"""
        while len(self.guesses) < self.max_guesses:
            ...

if __name__ == '__main__':
    game = GuessingGame()
    game()  # __call__ is invoked