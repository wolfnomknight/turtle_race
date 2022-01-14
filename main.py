from turtle import Turtle, Screen
import random

# Setting the screen and screen background color
screen = Screen()
screen.bgcolor("salmon4")

# List of colors to be used as turtles
list_of_colors = ["red", "blue", "green", "purple", "black", "white", "yellow"]
list_of_turtles = []

# Setting the finish line value
finish = 400
keep_playing = True

# The player starting points
points = 10

# Creating the 7 turtles... one for each color
for t in range(0, 7):
    lil_turtle = Turtle(shape="turtle")
    lil_turtle.color(list_of_colors[t])
    lil_turtle.speed(5)
    lil_turtle.penup()
    list_of_turtles.append(lil_turtle)

# The race
while keep_playing:

    end = False

# Turtles go to the starting line
    x = -400
    y = -150
    for t in list_of_turtles:
        t.goto(x, y)
        y += 50

# Player input
    guess = screen.textinput("Take a guess", "Which turtle will win?\nRed,\nBlue,\nGreen,\nPurple,\nBlack,\nWhite, or\nYellow?")
    guess = guess.lower()
    bet = screen.numinput(title="What is your bet?", prompt="Choose the value of your bet:", default=1, minval=0, maxval=points)
    winners = ["", "", ""]

# Racing, when the turtle has not reached the finish line, it'll continue 'running'
    while not end:
        for t in list_of_turtles:
            # Checks for first, second and third places
            if t.xcor() >= 400:
                t_color = (t.pencolor()).title()
                if winners[0] == "":
                    winners[0] = t_color
                elif winners[1] == "" and winners[0] != t_color:
                    winners[1] = t_color
                elif winners[2] == "" and winners[0] != t_color and winners[1] != t_color:
                    winners[2] = t_color
                    end = True
            else:
                # Turtles 'run' a random value between 2 and 5 pixels each step
                t.forward(random.randint(2, 5))

    # Showing results
    print(f"You guessed: {guess}")
    print(f"The winner is {winners[0]}! {winners[1]} is second place and {winners[2]} is third!")
    if guess.title() in winners:
        reward = int(bet * 2)
        points = int(points + reward)
        print("You guessed right!")
        print(f"You got {reward} points!")
    else:
        points = int(points - bet)
        print("Try again!")
    print(f"Now you have {points}!")

    again = screen.textinput(title="Play again?", prompt="Play again?").lower()
    if again == "y" or again == "yes":
        pass
    else:
        keep_playing = False


screen.exitonclick()
