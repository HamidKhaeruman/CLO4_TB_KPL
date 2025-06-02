# src/state_machine.py

class QuizState:
    HOME = 'home'
    QUIZ = 'quiz'
    RESULT = 'result'
    ABOUT = 'about'

class StateMachine:
    """Simple state automata for page navigation."""
    def __init__(self):
        self.state = QuizState.HOME

    def transition(self, action):
        table = {
            (QuizState.HOME, 'start_quiz'): QuizState.QUIZ,
            (QuizState.QUIZ, 'finish'): QuizState.RESULT,
            (QuizState.RESULT, 'restart'): QuizState.HOME,
            (QuizState.HOME, 'about'): QuizState.ABOUT,
            (QuizState.ABOUT, 'home'): QuizState.HOME,
        }
        self.state = table.get((self.state, action), self.state)
        return self.state