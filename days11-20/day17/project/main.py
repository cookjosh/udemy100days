# Day 17 Project - Quiz Game
# Day 17 focuses on OOP and creating custom classes
# Question set is predefined.
# Lesson shows using an API to get additional questions.

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    new_question = Question(q["text"], q["answer"])
    question_dict = {new_question.text: new_question.answer}
    question_bank.append(question_dict)

quiz_brain = QuizBrain(question_bank)

quiz_brain.questions_remaining()

