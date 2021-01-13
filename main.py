from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for line in question_data:
    question_bank.append(Question(line["question"], line["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")