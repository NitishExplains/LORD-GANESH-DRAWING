# Shree Ganeshay Namah 🙏
# =====================================
# Author: Nitish Singh
# GitHub: https://github.com/your-username

from turtle import *
import random

# Setup the screen
title('श्री गणेश जी - आशीर्वाद संस्करण')
bgcolor("black")
speed(0)  # Fast Drawing speed
pensize(2)

# Define color schemes
color_schemes = [
    {"primary": "red", "secondary": "orange", "accent": "gold"},
    {"primary": "darkblue", "secondary": "lightblue", "accent": "white"},
    {"primary": "darkgreen", "secondary": "lightgreen", "accent": "yellow"},
    {"primary": "purple", "secondary": "violet", "accent": "pink"}
]

# Select a random color scheme
scheme = random.choice(color_schemes)
primary_color = scheme["primary"]
secondary_color = scheme["secondary"]
accent_color = scheme["accent"]

# Function to move turtle without drawing
def move_to(x, y):
    penup()
    goto(x, y)
    pendown()

# Function to draw filled circles
def draw_circle(radius, color):
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

# Function to draw decorative patterns
def draw_pattern(x, y, size, color):
    move_to(x, y)
    fillcolor(color)
    begin_fill()
    for _ in range(8):
        forward(size)
        left(45)
    end_fill()

# Draw background elements (stars)
def draw_stars():
    move_to(-300, 250)
    pencolor("white")
    for _ in range(30):
        move_to(random.randint(-300, 300), random.randint(-300, 300))
        dot(2, "white")

# Draw decorative border
def draw_border():
    move_to(-300, -300)
    pencolor(accent_color)
    for i in range(4):
        forward(600)
        left(90)

# Draw the main figure
def draw_figure():
    pencolor(primary_color)
    fillcolor(secondary_color)

    # Trunk    
    move_to(-130, 150)
    seth(-120)
    begin_fill()
    circle(100, 90)
    circle(280, 10)
    circle(-120, 90)
    circle(-60, 150)
    circle(-30, 60)
    seth(-120)
    circle(30, 60)
    circle(55, 150)
    circle(120, 77)
    circle(-100, 115)
    end_fill()
    
    move_to(0, 50)
    seth(20)
    begin_fill()
    circle(-50, 80)
    circle(-200, 70)
    circle(-50, 60)
    seth(-20)
    circle(50, 70)
    circle(205, 70)
    circle(50, 85)
    end_fill()
    
    move_to(70, 10)
    seth(15)
    begin_fill()
    circle(90, 120)
    seth(-52)
    circle(-90, 110)
    end_fill()

    # Eyes
    def draw_eye(x, y):
        move_to(x, y)
        seth(-55)
        begin_fill()
        circle(20, 120)
        seth(-90)
        circle(-17, 165)
        end_fill()
        # Add eye details
        move_to(x+5, y+5)
        draw_circle(5, "white")
        move_to(x+7, y+7)
        draw_circle(2, "black")
    
    draw_eye(-100, 110)
    draw_eye(40, 110)

    # Tilak (forehead marking)
    move_to(0, 150)
    draw_circle(10, accent_color)
    move_to(-2, 125)
    draw_circle(8, accent_color)
    move_to(-4, 105)
    draw_circle(5, accent_color)

    # Crown
    move_to(-80, 200)
    seth(30)
    fillcolor(accent_color)
    begin_fill()
    circle(-150, 60)
    seth(141)
    circle(120, 80)
    end_fill()
    
    move_to(-70, 225)
    seth(30)
    begin_fill()
    circle(-120, 60)
    seth(141)
    circle(95, 80)
    end_fill()
    
    move_to(-30, 280)
    seth(-120)
    begin_fill()
    circle(20, 250)
    circle(-50, 40)
    seth(-100)
    circle(50, 42)
    circle(-15, 240)
    end_fill()
    
    move_to(-5, 268)
    draw_circle(9, "yellow")

    # Add jewel to crown
    move_to(-10, 290)
    draw_circle(5, "red")

    # Left ear
    move_to(-160, 130)
    seth(120)
    begin_fill()
    circle(70, 60)
    circle(15, 100)
    circle(90, 30)
    circle(-15, 40)
    circle(90, 30)
    circle(20, 100)
    seth(-130)
    circle(-20, 100)
    circle(-90, 30)
    circle(15, 35)
    circle(-90, 50)
    circle(-18, 80)
    circle(-70, 80)
    end_fill()

    # Right ear
    move_to(140, 130)
    seth(60)
    begin_fill()
    circle(-70, 60)
    circle(-15, 100)
    circle(-90, 30)
    circle(15, 40)
    circle(-90, 30)
    circle(-20, 100)
    seth(-50)
    circle(20, 100)
    circle(90, 30)
    circle(-15, 35)
    circle(90, 50)
    circle(18, 80)
    circle(70, 80)
    end_fill()

    # Add earrings
    move_to(-180, 80)
    draw_circle(8, "yellow")
    move_to(180, 80)
    draw_circle(8, "yellow")

    # Belly
    move_to(-130, -20)
    seth(-60)
    begin_fill()
    circle(-20, 60)
    circle(150, 50)
    circle(60, 60)
    seth(175)
    circle(-70, 70)
    circle(-132, 50)
    circle(40, 40)
    end_fill()

    # Add decorative pattern on belly
    draw_pattern(-30, -50, 15, accent_color)

    # Left leg
    move_to(-90, -250)
    seth(180)
    begin_fill()
    circle(-100, 60)
    circle(20, 90)
    circle(40, 40)
    circle(20, 60)
    circle(120, 40)
    seth(178)
    circle(-120, 40)
    circle(-25, 60)
    circle(-50, 50)
    circle(-30, 90)
    circle(70, 50)
    end_fill()

    # Right leg
    move_to(120, -260)
    seth(15)
    begin_fill()
    circle(120, 50)
    circle(20, 90)
    circle(70, 40)
    circle(120, 40)
    circle(-60, 60)
    circle(70, 60)
    circle(20, 90)
    seth(-120)
    circle(20, 120)
    circle(40, 50)
    circle(-70, 40)
    seth(180)
    circle(65, 40)
    circle(-35, 40)
    circle(-17, 120)
    seth(120)
    circle(-14, 70)
    circle(-65, 60)
    circle(40, 70)
    circle(-115, 50)
    circle(-60, 20)
    circle(-15, 98)
    circle(-110, 50)
    end_fill()

    # Left hand
    move_to(-170, -60)
    seth(180)
    begin_fill()
    circle(20, 80)
    circle(-30, 150)
    circle(20, 80)
    seth(0)
    circle(-20, 80)
    circle(32, 170)
    circle(-20, 80)
    end_fill()
    
    move_to(-205, -80)
    seth(75)
    begin_fill()
    circle(40, 60)
    seth(-150)
    circle(40, 60)
    seth(65)
    circle(-40, 40)
    seth(-45)
    circle(-40, 35)
    end_fill()

    # Right hand
    move_to(240, -60)
    seth(180)
    begin_fill()
    circle(20, 80)
    circle(-30, 150)
    circle(20, 80)
    seth(0)
    circle(-20, 80)
    circle(32, 170)
    circle(-20, 80)
    end_fill()
    
    move_to(205, -80)
    seth(75)
    begin_fill()
    circle(40, 60)
    seth(-150)
    circle(40, 60)
    seth(65)
    circle(-40, 40)
    seth(-45)
    circle(-40, 35)
    end_fill()

    # Add decorative bangles
    for i in range(3):
        move_to(-220, -60 - i*10)
        draw_circle(5, ["gold", "silver", "red"][i])
        move_to(220, -60 - i*10)
        draw_circle(5, ["gold", "silver", "red"][i])

# Draw title text
def draw_title():
    move_to(-120, 320)
    pencolor(accent_color)
    write("ॐ गण गणपतये नमः", font=("Arial", 20, "bold"))

    # Draw mandala-like patterns in corners
    for x, y in [(-250, 250), (250, 250), (-250, -250), (250, -250)]:
        move_to(x, y)
        for i in range(8):
            circle(i*5, 90)
            left(45)

# Main drawing function
def main():
    # Draw background elements first
    draw_stars()
    draw_border()
    
    # Draw the main figure
    draw_figure()
    
    # Draw title
    draw_title()
    
    # Hide turtle and display
    hideturtle()
    done()

# Run the program
if __name__ == "__main__":
    main()
