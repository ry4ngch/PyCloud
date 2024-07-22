import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()



# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
no_of_state = len(data)
guess_state = []

while len(guess_state) <= no_of_state:
    answer_state = screen.textinput(title=f"{len(guess_state)}/{no_of_state} Guess the state", prompt="What's another state in US").title()
    answer_data = data[data.state == answer_state]

    if answer_state == "Exit":
        df = pandas.DataFrame(set(data.state).difference(set(guess_state)))
        df.to_csv("states_to_learn.csv")
        break

    if not answer_data.empty:
        st = turtle.Turtle()
        st.penup()
        st.hideturtle()
        st.setpos(int(answer_data.x), int(answer_data.y))
        st.write(f"{answer_state}", False, align="center", font=("Arial", 12, "normal"))
        guess_state.append(answer_state)


# Keep the screen open
turtle.mainloop()
