# src/question_loader.py
from .config import Config

class QuestionLoader:
    """Reusable component to load and filter questions."""
    def __init__(self):
        self._questions = Config().get_questions()

    def get_all_questions(self):
        return self._questions

    def get_by_category(self, category):
        return [q for q in self._questions if q['category'] == category]