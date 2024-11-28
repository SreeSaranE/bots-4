import random
import json
import os

class ResponseGenerator:
    def __init__(self):
        self.responses = self._load_responses()
        
    def _load_responses(self):
        responses_path = os.path.join(os.path.dirname(__file__), '../data/responses.json')
        with open(responses_path, 'r') as f:
            return json.load(f)
    
    def generate(self, intent, message, visitor_data, sentiment):
        base_responses = self.responses.get(intent, self.responses['default'])
        
        # Personalize response with visitor name
        visitor_name = visitor_data.get('name', 'there')
        
        # Select appropriate response based on sentiment
        if sentiment['label'] == 'NEGATIVE' and sentiment['score'] > 0.7:
            response = random.choice(self.responses['empathy'])
        else:
            response = random.choice(base_responses)
        
        # Format response with visitor name and message context
        return response.format(
            name=visitor_name,
            message=message,
            department=visitor_data.get('department', 'support')
        )