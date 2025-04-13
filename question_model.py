class Question:
    def __init__(self, question: dict):
        self.question = question.get("question")
        self.correct_answer = question.get("correct_answer")
        self.wrong_answer = question.get("wrong_answer")
