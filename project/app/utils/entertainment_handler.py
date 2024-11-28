import random

class EntertainmentHandler:
    def __init__(self):
        self.jokes = [
            "Why don't programmers like nature? It has too many bugs!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why did the scarecrow win an award? He was outstanding in his field!"
        ]
        
        self.games = [
            {
                'name': 'Number Guess',
                'description': 'I\'m thinking of a number between 1 and 100!'
            },
            {
                'name': 'Word Chain',
                'description': 'I\'ll say a word, and you say a word that starts with the last letter of my word!'
            },
            {
                'name': 'Riddle',
                'description': 'Would you like to solve a riddle?'
            }
        ]
    
    def handle_request(self, message):
        message = message.lower()
        
        if 'joke' in message:
            return self._tell_joke()
        elif 'game' in message:
            return self._suggest_game()
        else:
            return self._default_entertainment()
    
    def _tell_joke(self):
        return random.choice(self.jokes)
    
    def _suggest_game(self):
        game = random.choice(self.games)
        return f"Let's play {game['name']}! {game['description']}"
    
    def _default_entertainment(self):
        return "I can tell you a joke or we can play a game! What would you prefer?"