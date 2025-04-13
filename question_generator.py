import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class QuestionGenerator:
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.client = genai.Client(api_key=self.API_KEY)
        self.response = None

    def get_questions(self, syllabus, questions):
        self.response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Generate {questions} questions in json format with a correct answer and wrong answer from the syllabus:\n{syllabus}",
        )
        return self.response.text[7:-3]
