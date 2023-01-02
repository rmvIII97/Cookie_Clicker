import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker by Michael Vick")
wn.bgpic("Cookie_Clicker\Background.gif")


wn.register_shape("Cookie_Clicker\Cookie.gif")

cookie = turtle.Turtle()
cookie.shape("Cookie_Clicker\Cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Impact", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Impact", 32, "normal"))

cookie.onclick(clicked)

wn.mainloop()