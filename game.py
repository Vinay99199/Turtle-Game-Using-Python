from turtle import *
from random import randint

screen = Screen()
screen.title("Turtle Racing Game")
screen.setup(width=800, height=500)
screen.bgcolor("lightgreen")


track_start_x = -300
track_length = 500

penup()
goto(track_start_x, 200)
speed(10)

for x in range(10):
    write(x, align="center", font=("Arial", 12, "normal"))
    right(90)
    forward(10)
    pendown()
    forward(200)
    penup()
    backward(210)
    left(90)
    forward(50)

finish_x = track_start_x + track_length
penup()
goto(finish_x, 230)
write("🏁 Finish Line", align="center", font=("Arial", 16, "bold"))

for i in range(10):
    goto(finish_x, 200 - (i * 20))
    pendown()
    forward(20)
    penup()

turtles = []
colors = ['red', 'black', 'green', 'blue', 'purple']
names = ['Red Racer', 'Black Bomber', 'Green Lightning', 'Blue Thunder', 'Purple Speedster']
start_x, start_y = track_start_x - 30, 180

for i, color in enumerate(colors):
    t = Turtle()
    t.penup()
    t.goto(start_x, start_y - (i * 50))
    t.color(color)
    t.shape('turtle')
    t.pendown()
    turtles.append(t)
    
    name_tag = Turtle()
    name_tag.penup()
    name_tag.goto(start_x + 10, start_y - (i * 50) + 10)
    name_tag.write(names[i], align="left", font=("Arial", 12, "normal"))
    name_tag.hideturtle()

leaderboard = Turtle()
leaderboard.hideturtle()
leaderboard.penup()
leaderboard.goto(250, 150)

def start_race():
    leaderboard.clear()
    leaderboard.goto(250, 150)
    leaderboard.write("🏆 Leaderboard 🏆", align="center", font=("Arial", 16, "bold"))

    race_on = True
    while race_on:
        for t in turtles:
            t.forward(randint(1, 10))  
            screen.update()  

            if t.xcor() >= finish_x:
                race_on = False
                winner = t.color()[0]  
                leaderboard.goto(250, 100)
                leaderboard.write(f"🥇 {winner.upper()} WINS!", align="center", font=("Arial", 20, "bold"))
                return 

def restart():
    for t in turtles:
        t.goto(start_x, start_y - (colors.index(t.color()[0]) * 50))
    leaderboard.clear()
    screen.update()

def draw_button(x, y, text):
    """Draws a visible button with a blue background and white text."""
    button = Turtle()
    button.penup()
    button.goto(x, y)
    button.color("blue")  
    button.begin_fill()
    for _ in range(2):
        button.forward(140)
        button.right(90)
        button.forward(40)
        button.right(90)
    button.end_fill()
    button.goto(x + 70, y - 30)  
    button.color("white")
    button.write(text, align="center", font=("Arial", 14, "bold"))
    button.hideturtle()
    return (x, x + 140, y - 40, y)  

start_button_area = draw_button(-200, -150, "Start Race")
restart_button_area = draw_button(50, -150, "Restart")

def check_click(x, y):
    
    if start_button_area[0] < x < start_button_area[1] and start_button_area[2] < y < start_button_area[3]:
        start_race()

    elif restart_button_area[0] < x < restart_button_area[1] and restart_button_area[2] < y < restart_button_area[3]:
        restart()

screen.listen()
screen.onclick(check_click)

screen.mainloop()
