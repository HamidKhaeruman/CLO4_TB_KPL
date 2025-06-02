# src/quiz_manager.py

from .question_loader import QuestionLoader

class QuizManager:
    """Facade Pattern: Simplifies quiz operations."""
    def __init__(self):
        self.loader = QuestionLoader()
        self.current_index = 0
        self.score = 0
        self.user_answers = []

    def start_quiz(self):
        self.questions = self.loader.get_all_questions()
        self.current_index = 0
        self.score = 0
        self.user_answers = []

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def answer_current(self, answer):
        question = self.get_current_question()
        correct = question['answer'].strip().lower() == answer.strip().lower()
        self.user_answers.append({
            'question': question['question'],
            'your_answer': answer,
            'correct_answer': question['answer'],
            'is_correct': correct,
        })
        if correct:
            self.score += 1
        self.current_index += 1

    def is_finished(self):
        return self.current_index >= len(self.questions)

    def get_score(self):
        return self.score

    def get_result(self):
        return self.user_answers