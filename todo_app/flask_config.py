import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
        self.TRELLO_API_TOKEN = os.environ.get('TRELLO_API_TOKEN')
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
