from Jumper.jumper import jumper
from Jumper.puzzle_word import puzzle_word
from Jumper.terminal import terminal


class Director:
    """A person who directs the game. 
    
    The Director class controls the sequence of play.
    Attributes:
        word (puzzle_word): The object responsible for any service related to the word.
        jumper (Jumper): The game's jumper.
        terminal: For getting and displaying information on the terminal.
        is_playing (boolean): Whether or not to keep playing.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self._word = puzzle_word()
        self._jumper = jumper()
        self._terminal_service = terminal()
        self._is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        self._word.random_word()
        self._terminal_service.write_text("\n------------------------------------------------------------------\n"
                                            "\nWelcome to the jumper game! Help the jumper stay safe. \n"
                                            "A word was randomly chosen. Guess a letter and good luck! \n")

        self._terminal_service.write_text(self._word.get_word_display())
        self._terminal_service.draw(self._jumper.get_parachute())

        while(self._is_playing):

            if self._word.correct_word_guess() or not self._jumper.reach_wrong_guess():
                self._is_playing = False

            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        if not self._jumper.reach_wrong_guess():
            self._terminal_service.write_text("\n------------------------------------------------------------------\n"
                                                "\nSorry, the game is over. See you next time! \n")
        else:
            self._terminal_service.write_text("\n------------------------------------------------------------------\n"
                                                f"\nCongratulations! The word is *{self._word.get_secret_word()}*. Our jumper is safe now!\n")
    
    def _get_inputs(self):
        """Reads the players guess and say if it can be found in the secret word.
        Args:
            self (Director): An instance of Director.
        """
        letter = self._terminal_service.read_text("\nEnter a letter [a-z]: ")
        self._word.last_hint_correct(letter)

    def _do_updates(self):
        """Cuts part of the parachute if the last guess was wrong, or reveals
        the letter correctly guessed.
        Args:
            self (Director): An instance of Director.
        """
        if (not self._word.get_last_guess()):
            self._jumper.update_parachute()

        if self._word.correct_word_guess() or not self._jumper.reach_wrong_guess():
            self._is_playing = False

    def _do_outputs(self):
        """Displays guessed letter in the word and the state of the jumper's parachute.
            Informs if the guess was correct or not.
        Args:
            self (Director): An instance of Director.
        """
        
        self._terminal_service.write_text(self._word.get_word_display())
        self._terminal_service.draw(self._jumper.get_parachute())

        if(self._word.get_last_guess()):
            self._terminal_service.write_text("\nCorrect!")
        else:
            self._terminal_service.write_text("\nOops, incorrect! You lost part of the parachute!")