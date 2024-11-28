from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline("sentiment-analysis")
        
    def analyze(self, text):
        return self.analyzer(text)[0]