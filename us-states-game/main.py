import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
# screen.bgpic("blank_states_img.gif")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

data = pandas.read_csv("U.S._states.csv")
count_states = 0
guessed_states = []

while count_states < 50:
    answer_state = screen.textinput(title=f"{count_states}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        not_guessed_states = [state for state in data.state if state not in guessed_states]
        break
    for state in data.state:
        if state == answer_state:
            count_states += 1
            info = data[data.state == answer_state]
            guessed_states.append(answer_state)
            # state = info.state.item()
            tim.goto((int(info.x), int(info.y)))
            tim.write(f"{answer_state}")
            if count_states == len(data.state)+1:
                game_is_on = False
        else:
            pass

#not_guessed_states = [state for state in data.state if state not in guessed_states]
print(not_guessed_states)
print(guessed_states)

df = pandas.DataFrame(not_guessed_states)
df.to_csv("states_to_learn.csv")



