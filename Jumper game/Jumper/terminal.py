
class terminal:
    """terminal class deals with what appears on the terminal console.
    
    """
    def read_text(self, prompt):
        """Gets text input from the terminal and turns it to lowercase.
             Directs the user with the given prompt.
        Args: 
            self (Terminal): An instance of terminal.
            prompt (string): The prompt to display on the terminal.
        Returns:
            string: The user's input as text.
        """
      
        return input(prompt).lower()
        
    def write_text(self, text, list=[]):
        """Displays the given text or list on the terminal or turns a list into a string
            before displaying it. 
        Args: 
            self (Terminal): An instance of terminal.
            text (string): The text to display.
            list (List[string]): The list to be joined and displayed.
        """
        if (len(list) > 0):
            print("".join(list))
        else:
            print(text)

    def draw(self, list):
        """Displays one item of a list at a time. 
        Args: 
            self (Terminal): An instance of terminal.
            list (List[string]): The list to have its items displayed one at a time.
        """
      
        for pict in list:
            print(pict)