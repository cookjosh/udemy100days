import random
from data import question_data
from question_model import Question

question_bank = []
for q in question_data:
    new_question = Question(q["text"], q["answer"])
    question_dict = {new_question.text: new_question.answer}
    question_bank.append(question_dict)

print(question_bank)
