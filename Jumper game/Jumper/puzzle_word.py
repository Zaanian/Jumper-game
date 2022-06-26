import random

class puzzle_word:
    """The person managing services related to the secret word. 
    
    The puzzle_word class will randomly choose a secret word from a list. It will let the user
    know if the letter guessed is in the secret word. It also alerts once the secret word is guessed.
    
    Attributes:
        _secret_word (List[int]): The randomly chosen word.
        _word_display (List[int]): The display of the guessed letters.
        _last_hint (boolean): Informs if the last guess was successful or not.
    """
    def __init__(self):
        """Constructs a new puzzle_word.
        Args:
            self (puzzle_word): An instance of puzzle_word.
        """
        self._secret_word = []
        self._word_display = []
        self._last_guess = True

    def random_word(self):
        """Randomly chooses a word from the _words list and separates it in letters.
         Prepares the display to give orientation to the player.
        
        Args:
            self (puzzle_word): An instance of puzzle_word.
        """
        _words = ["happy", "jupiter", "person", "dragon", "marine"]
        self._secret_word = list(random.choice(_words))
        
        for i in range(len(self._secret_word)):
            self._word_display.append(" _ ")
    
    def last_hint_correct(self, letter):
        """Compares the secret word letter with the guessed letter. If the guessed letter
            is found, last guess was true. Otherwise, it was false.
        
        Args:
            self (puzzle_word): An instance of puzzle_word.
        """
        count = self._secret_word.count(letter)

        if (count == 0):
            self._last_guess = False
        else:
            self._last_guess = True
            self._update_word_display(letter)

    def _update_word_display(self, letter):
        """Reveals the position of the letter.
        
        Args:
            self (puzzle_word): An instance of puzzle_word.
            letter (string): The last guessed letter.
        """
        for i in range(len(self._secret_word)):
            if self._secret_word[i] == letter:
                self._word_display[i] = letter

    def get_word_display(self):
        """Gets the word to be displayed to the player, with the revealed letters.
        
        Args:
            self (puzzle_word): An instance of puzzle_word.
        Returns:
            string: The word display.
        """
        return " ".join(self._word_display)

    def get_secret_word(self):
        """Gets the secret word.
        
        Args:
            self (puzzle_word): An instance of puzzle_word.
            
        Returns:
            string: The secret word joined.
        """
        return "".join(self._secret_word)

    def get_last_guess(self):
        """Gets the last guess.
        
        Args:
            self (puzzle_word): An instance of puzzle_word.
            
        Returns:
            boolean: If the last guess was successful.
        """
        return self._last_guess

    def correct_word_guess(self):
        """Compares the displayed word and the secret word to inform if the game is over.
        
        Args:
            self (puzzle_word): An instance of puzzle_word.
            
        Returns:
            boolean: The secret word equals to the displayed word.
        """
        secret = "".join(self._secret_word)
        word = "".join(self._word_display)

        return secret == word