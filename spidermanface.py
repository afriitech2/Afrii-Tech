import turtle

# স্ক্রিন সেটআপ
screen = turtle.Screen()
screen.setup(width=650, height=700)
screen.bgcolor("black")
screen.title("Spiderman Turtle Art")

t = turtle.Turtle()

# 🎬 রিল রেকর্ডিংয়ের জন্য আঁকার গতি (Speed):
# ১ = খুব ধীর (Slow), ৩ = মাঝারি (Medium), ১০ = দ্রুত (Fast)
t.speed(2) 

# --- ১. লাল মাস্ক বা ফেস (Red Mask Base) ---
t.penup()
t.goto(0, -220)
t.pendown()
t.color("#E50914", "#E50914") # স্পাইডারম্যানের মার্ভেল রেড কালার
t.begin_fill()
t.circle(220)
t.end_fill()

# --- ২. মুখের ওপর মাকড়সার জাল (Spider Web Pattern) ---
t.color("black")
t.pensize(2)

# কেন্দ্র থেকে বাইরে ছড়ানো রেখা (Straight Lines)
angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
for angle in angles:
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.forward(218)

# জালের বৃত্তাকার রিং (Web Rings)
for radius in [40, 85, 130, 175, 215]:
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.circle(radius)

# --- ৩. বাম চোখ (Left Eye) ---
t.penup()
t.goto(-15, 15)
t.pendown()
t.color("black", "white")
t.pensize(7)
t.begin_fill()
t.setheading(130)
t.circle(100, 75)
t.left(105)
t.circle(130, 65)
t.end_fill()

# --- ৪. ডান চোখ (Right Eye) ---
t.penup()
t.goto(15, 15)
t.pendown()
t.color("black", "white")
t.pensize(7)
t.begin_fill()
t.setheading(50)
t.circle(-100, 75)
t.right(105)
t.circle(-130, 65)
t.end_fill()

# কার্সার লুকানো ও স্ক্রিন ধরে রাখা
t.hideturtle()
turtle.done()