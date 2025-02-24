
class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        while(self.question_number < len(self.questions_list)):
            self.get_question()
        

    def get_question(self):
        curr_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text}. (True./False)?: ")
        self.check_answer(user_answer, curr_question.answer)

    def check_answer(self, user_answer, curr_answer):
        if(user_answer.lower() == curr_answer.lower()):
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(f"The correct answer was: {curr_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    