import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
guessed_state = []
missing_state = []

while len(guessed_state) < 50:
    guess = screen.textinput(title=f"{len(guessed_state)}/50 state correct", prompt="What's another state name?").title()
    data_state = data.state.to_list()
    if guess == "Exit":
        # for state in data_state:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        # new_data = pandas.DataFrame(missing_state)
        missing_states = [state for state in data_state if state not in guessed_state]
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if guess in data_state:
        guessed_state.append(guess)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == guess]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(guess)

()