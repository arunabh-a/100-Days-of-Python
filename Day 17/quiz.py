from data import question_data
from qmodel import Question
from qbrain import QuizBrain

question_bank = []

for question in question_data:
    qtext = question["text"]
    qans = question["answer"]
    newques = Question(qtext, qans)
    question_bank.append(newques)

quiz = QuizBrain(question_bank)
while quiz.ques_left():
    quiz.next_ques()


print(f"You've Completed the Quiz \nYour Score: {quiz.score}/{quiz.qnum}")
