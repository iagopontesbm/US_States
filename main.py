import turtle as tt
import pandas as pd

screen = tt.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tt.shape(image)
map_text = tt.Turtle()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name.").title()
print(answer_state)

data = pd.read_csv("50_states.csv")

us_state = data[data.state == answer_state]
print(us_state.x.at)
print(us_state.y.at)


# map_text.color("black")
# map_text.penup()
# map_text.goto(us_state.x, us_state.y)
# map_text.hideturtle()
#