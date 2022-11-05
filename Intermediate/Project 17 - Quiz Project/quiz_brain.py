from question_model import Question
import view

class QuizBrain:

    def __init__(self, question_list : list) -> None:
        '''Initializes a new QuizBrain object.'''
        self.score = 0
        self.question_number = 0
        self.question_list = question_list


    def any_questions_left(self) -> bool:
        '''Checks if there are any questions left in the question list.'''
        return self.question_number < len(self.question_list)


    def check_answer(self, question : Question, user_answer : str):
        '''Checks if the user's answer to the question was right and increases their score if so.'''

        if user_answer == question.answer:
            view.print_info_message(f"You got it right! The correct answer is: {question.answer}")
            self.score += 1       
        else:
            view.print_info_message(f"That's wrong. The correct answer is: {question.answer}")

        view.print_info_message(f"Your current score is: {self.score}/{self.question_number}", new_screen=False)
        view.trigger_continuation()


    def next_question(self):
        '''Displays the next question and evaluates the user's answer to it.'''

        if not self.any_questions_left():
            raise Exception(f"There are no questions left in the question list!")

        current_question = self.question_list[self.question_number]
        self.question_number += 1

        while True:
            view.print_info_message(f"Q.{self.question_number}: {current_question.text}")
            user_answer = input("\n(True/False)?: ").strip().capitalize()

            if user_answer != "True" and user_answer != "False":
                view.print_error_message("Invalid answer!")
            else: break
        
        self.check_answer(current_question, user_answer)
