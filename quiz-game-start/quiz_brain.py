class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!!!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number+1}")
        else:
            print(f"You got it wrong, answer is {correct_answer}")

    def next_question(self):
        while self.has_questions():
            current_question = self.question_list[self.question_number]
            user_answer = input(f"Q. {self.question_number + 1}: {current_question['question']} (True/ False)?")
            self.check_answer(user_answer, current_question['correct_answer'])
            self.question_number += 1

