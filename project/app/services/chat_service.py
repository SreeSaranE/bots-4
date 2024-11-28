from ..models.intent_classifier import IntentClassifier
from ..models.sentiment_analyzer import SentimentAnalyzer
from ..utils.response_generator import ResponseGenerator
from ..utils.entertainment_handler import EntertainmentHandler
import logging

logger = logging.getLogger(__name__)

class ChatService:
    def __init__(self, config):
        self.config = config
        self.intent_classifier = IntentClassifier()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.response_generator = ResponseGenerator()
        self.entertainment_handler = EntertainmentHandler()
    
    def process_message(self, message, visitor_data):
        try:
            # Analyze intent and sentiment
            intent = self.intent_classifier.predict(message)
            sentiment = self.sentiment_analyzer.analyze(message)
            
            # Handle entertainment requests
            if intent == 'entertainment':
                response = self.entertainment_handler.handle_request(message)
            else:
                response = self.response_generator.generate(
                    intent=intent,
                    message=message,
                    visitor_data=visitor_data,
                    sentiment=sentiment
                )
            
            return {
                'response_text': response,
                'intent': intent,
                'sentiment': sentiment,
                'visitor_id': visitor_data['visitor_id'],
                'success': True
            }
            
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}", exc_info=True)
            return {
                'response_text': "I apologize, but I'm having trouble processing your request. Please try again.",
                'success': False,
                'error': str(e)
            }