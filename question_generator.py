import os

from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()


class QuestionGenerator:
    """
    A class to generate quiz questions using the Google Gemini API.
    """

    def __init__(self):
        """
        Initializes the QuestionGenerator with an API key from the environment
        and creates a Gemini client instance.
        """

        self.API_KEY = os.getenv("API_KEY")
        self.client = genai.Client(api_key=self.API_KEY)
        self.response = None

    def get_questions(self, syllabus, questions):
        """
        Generates a specified number of quiz questions based on a syllabus.

        Args:
            syllabus (str): The syllabus or content to generate questions from.
            questions (int): Number of questions to generate.

        Returns:
            str: A JSON-like string containing the generated questions,
                 each with a correct and wrong answer.
        """

        # Use Gemini model to generate content in JSON format
        self.response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Generate {questions} questions in json format with a correct answer and wrong answer from the syllabus:\n{syllabus}",
        )

        # Gemini responses sometimes contain prefixes/suffixes like ```json ... ```
        # This trims out markdown-style formatting if present
        return self.response.text[7:-3]
