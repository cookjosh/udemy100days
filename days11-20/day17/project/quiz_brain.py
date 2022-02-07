class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        for k in current_question:
            question_text = k
            answer_text = current_question[k]
        user_answer = input(f"Q.{self.question_number}: {question_text} True or False? ")
        if user_answer == answer_text:
            print("Correct!")
            self.score += 1
        else:
            print("Sorry, that's not correct.")
        print(f"The correct answer was: {answer_text}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def questions_remaining(self):
        while self.question_number < len(self.question_list):
            self.next_question()
        print("That's all the questions.")
        print("Thanks for playing!")
        print(f"Your final score is: {self.score}/{len(self.question_list)}")
