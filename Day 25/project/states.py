import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("States of India")
screen.setup(width=800, height=700)
img = 'India-state.gif'
turtle.addshape(img)
turtle.shape(img)
word = turtle.Turtle()
word.hideturtle()


correct_answers = 0
isRight = True


# def nameState(answer):
#     answerCoords = state_data[state_data.state == answer]
#     stateX = int(answerCoords.x)
#     stateY = int(answerCoords.y)
#     word.penup()
#     word.goto(stateX, stateY)
#     word.write(answer, font=("Arial", 8, "normal"))
#     all_states.remove(answer)


state_data = pd.read_csv('29_states.csv')

all_states = state_data.state.to_list()

while isRight == True:
    answer = screen.textinput(
        title=f"{correct_answers}/29 Correct",
        prompt="What's the state's name?"
        )

    answer = answer.title()

    if answer == 'Exit':
        isRight = False
    elif answer in all_states:
        print(f"You are correct, {answer} is a state in India.")
        correct_answers += 1
        answerCoords = state_data[state_data.state == answer]
        stateX = int(answerCoords.x)
        stateY = int(answerCoords.y)
        word.penup()
        word.goto(stateX, stateY)
        word.write(answer, font=("Arial", 8, "normal"))
        all_states.remove(answer)
        if correct_answers == 29:
            isRight = False
    else:
        print(f"Sorry, {answer} is not a state in India.")

leftStates = {
    'state_name': all_states
}

lS = pd.DataFrame(leftStates)
lS.to_csv('missed_states.csv')

screen.exitonclick()
