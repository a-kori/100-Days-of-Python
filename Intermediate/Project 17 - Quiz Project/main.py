import time
import data
import view
from question_model import Question
from quiz_brain import QuizBrain


view.print_info_message("Welcome to the quiz!")
time.sleep(3)

question_bank = []
for question in data.question_data:
    question_bank.append( Question(question["question"], question["correct_answer"]) )

quiz = QuizBrain(question_bank)

while quiz.any_questions_left():
    quiz.next_question()

view.print_info_message("You've completed the quz!\n\n" + 
    f"Your final score is: {quiz.score}/{len(quiz.question_list)}.")

print()