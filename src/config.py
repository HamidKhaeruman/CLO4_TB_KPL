# src/config.py
import os
import json

class Config(metaclass=type):
    """Singleton Pattern: Config loader for runtime configuration."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'config', 'soal_config.json')
        with open(config_path, encoding='utf-8') as f:
            self.questions = json.load(f)

    def get_questions(self):
        return self.questions