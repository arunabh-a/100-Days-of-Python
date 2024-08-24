class QuizBrain:
    def __init__(self, qlist):
        self.qnum = 0
        self.list = qlist
        self.score = 0

    def ques_left(self):
        return self.qnum < len(self.list)
    
    def next_ques(self):
        currentQues = self.list[self.qnum]
        self.qnum += 1
        user_ans = input(f"Q.{self.qnum}: {currentQues.text} (True/False): ")
        self.check_ans(user_ans, currentQues.answer)

    def check_ans(self, user_ans, correct_ans):
        if correct_ans == user_ans:
            print("You got it right!")
            self.score += 1
        else:
            print("Well, That's Wrong")
        print(f"The Correct Answer is: {correct_ans}")
        print(f"Your Score : {self.score}/{self.qnum}\n\n")
