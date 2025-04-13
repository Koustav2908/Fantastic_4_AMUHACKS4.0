import json

from pptx import Presentation

from flash_cards import FlashCards
from question_generator import QuestionGenerator
from question_model import Question

syllabus = Presentation("syllabus/example_syllabus.pptx")

syllabus_text = ""
for slide in syllabus.slides:
    for shape in slide.shapes:
        if hasattr(shape, "text"):
            syllabus_text += shape.text + "\n"

question_generator = QuestionGenerator()
questions = question_generator.get_questions(syllabus_text, 10)

question_list = json.loads(questions)

question_list = [Question(question) for question in question_list]

FlashCards(question_list)
