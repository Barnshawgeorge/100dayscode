from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_bank.append(Question(questions['text'], questions['answer']))


quiz = QuizBrain(question_bank)
quiz.still_has_questions()
print(f"Quiz complete! Your final score was: {quiz.score}/{quiz.question_number}")