from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in range(0, len(question_data)):
    new_ques = Question(question_data[x]["question"], question_data[x]["correct_answer"])
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
