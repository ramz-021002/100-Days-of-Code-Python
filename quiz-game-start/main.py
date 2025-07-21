from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = [Question(question_data[i]["question"], question_data[i]["correct_answer"]) for i in range(0,len(question_data))]
# questions = []
# for i in range(0, len(question_data)-1):
#     questions.append(Question(question_data[i]["text"], question_data[i]["answer"]))

# question_bank = []
# for questions in question_data:
#     question_text = questions["text"]
#     question_answer = questions["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

quiz = QuizBrain(question_data)
quiz.next_question()
print(f"Your final score is {quiz.score}/{len(questions)}")