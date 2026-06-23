import turtle


def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    artist = turtle.Turtle()
    artist.speed(0)
    colors = ["red", "yellow", "blue", "green"]

    for i in range(180):
        artist.color(colors[i % 4])
        artist.forward(i * 2)
        artist.left(90)

    window.mainloop()


draw_art()
