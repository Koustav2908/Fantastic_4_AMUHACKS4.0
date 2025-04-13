class Question:
    """
    A class to represent a single quiz question with one correct and one wrong answer.
    """

    def __init__(self, question: dict):
        """
        Initializes a Question instance from a dictionary.

        Args:
            question (dict): A dictionary containing:
                - 'question' (str): The text of the question
                - 'correct_answer' (str): The correct answer
                - 'wrong_answer' (str): The incorrect answer
        """

        self.question = question.get("question")
        self.correct_answer = question.get("correct_answer")
        self.wrong_answer = question.get("wrong_answer")
