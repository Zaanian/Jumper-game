
class jumper:
    """The person wearing the parachute. 
    
    The jumper class keeps track of wrong guesses and cuts part of the parachute. 
    
    Attributes:
        _wrong_guess (int): Number of wrong guesses.
        _parachute (List[string]): Each part of the parachute.
    """
    def __init__(self):
        """Constructs a new jumper.
        Args:
            self (jumper): An instance of jumper.
        """
        self._parachute = [" ___ ","/___\\", "\   /"," \ / ","  o  "," /|\ "," / \ "]
        self._wrong_guess = 0

    def update_parachute(self):
        """Adds a wrong guess and removes part of the parachute.
        Args:
            self (jumper): An instance of jumper.
        """
        self._wrong_guess = self._wrong_guess + 1

        self._parachute[self._wrong_guess - 1] = "     "

    def get_parachute(self):
        """Gets the parts of the parachute.
        Args:
            self (jumper): An instance of jumper.
        
        Returns:
            List[string]: Parts of the parachute.
        """
        return self._parachute

    def reach_wrong_guess(self):
        """Says if the number of wrong guesses is enought to kill the jumper.
        Args:
            self (jumper): An instance of jumper.
        
        Returns:
            boolean: False, informing the jumper still has a parachute.
        """
        return self._wrong_guess < 4
    
    
    
