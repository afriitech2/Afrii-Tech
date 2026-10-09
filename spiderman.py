import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

# Window setup
root = tk.Tk()
root.title("Real Aesthetic Spider-Man - Live Step Drawing")
root.geometry("700x850")
root.configure(bg="#0b1322")

canvas = tk.Canvas(root, width=700, height=850, bg="#0b1322", highlightthickness=0)
canvas.pack(fill="both", expand=True)

img_w, img_h = 700, 850
image = Image.new("RGBA", (img_w, img_h), "#0b1322")
draw = ImageDraw.Draw(image)

photo_img = ImageTk.PhotoImage(image)
canvas_image_id = canvas.create_image(0, 0, image=photo_img, anchor="nw")

def update_canvas():
    """পিল ক্যানভাসে ড্র করার পর স্ক্রিন আপডেট করার ফাংশন"""
    global photo_img
    photo_img = ImageTk.PhotoImage(image)
    canvas.itemconfig(canvas_image_id, image=photo_img)

# ---------------- DRAWING STEPS LIST ----------------
drawing_tasks = []

# 1. Background Gradient (Chunked for performance)
def draw_bg_chunk(start_y, end_y):
    for y in range(start_y, end_y):
        r = int(11 + (y / img_h) * 10)
        g = int(19 + (y / img_h) * 15)
        b = int(34 + (y / img_h) * 20)
        draw.line([(0, y), (img_w, y)], fill=(r, g, b, 255))
    update_canvas()

for y_idx in range(0, img_h, 25):
    drawing_tasks.append((draw_bg_chunk, (y_idx, min(y_idx + 25, img_h))))

# 2. Torso & Shoulders
def draw_poly(points, fill, outline, width):
    draw.polygon(points, fill=fill, outline=outline, width=width)
    update_canvas()

drawing_tasks.append((draw_poly, ([(180, 520), (50, 850), (-20, 850), (100, 580)], "#112236", "#070e17", 3))) # Left Shoulder
drawing_tasks.append((draw_poly, ([(420, 500), (680, 850), (750, 850), (520, 550)], "#112236", "#070e17", 3))) # Right Shoulder
drawing_tasks.append((draw_poly, ([(180, 520), (50, 850), (680, 850), (420, 500), (310, 420)], "#960d1b", "#1a0003", 4))) # Chest Red Base

# 3. Head & Jawline
head_points = [
    (310, 100), (220, 130), (170, 200), (160, 290), (180, 370), 
    (240, 440), (310, 470), (380, 440), (440, 370), (450, 290), 
    (430, 200), (380, 130), (310, 100)
]
drawing_tasks.append((draw_poly, (head_points, "#be1223", "#1a0003", 4)))

# 4. Mask Webbing
def draw_line(p1, p2, fill, width):
    draw.line([p1, p2], fill=fill, width=width)
    update_canvas()

web_nodes = [
    (310, 100), (240, 120), (180, 170), (160, 250), (170, 340),
    (230, 420), (310, 470), (380, 420), (440, 340), (450, 250),
    (430, 170), (370, 120)
]

for node in web_nodes:
    drawing_tasks.append((draw_line, ((300, 280), node, "#2b0407", 2)))

def draw_arc_step(bbox, fill, width):
    draw.arc(bbox, start=0, end=360, fill=fill, width=width)
    update_canvas()

for r in [40, 80, 120, 160]:
    bbox = [300 - r * 0.9, 280 - r, 300 + r * 0.9, 280 + r]
    drawing_tasks.append((draw_arc_step, (bbox, "#2b0407", 2)))

# 5. Eyes
drawing_tasks.append((draw_poly, ([(180, 270), (270, 310), (290, 230), (210, 210)], "#0a0a0a", "#000000", 3))) # Left Outer
drawing_tasks.append((draw_poly, ([(190, 268), (265, 303), (282, 232), (215, 215)], "#edf4f8", "#8fa4b3", 2))) # Left Inner
drawing_tasks.append((draw_poly, ([(320, 230), (340, 310), (420, 270), (400, 210)], "#0a0a0a", "#000000", 3))) # Right Outer
drawing_tasks.append((draw_poly, ([(328, 232), (345, 303), (410, 268), (392, 215)], "#edf4f8", "#8fa4b3", 2))) # Right Inner

# 6. Chest Emblem & Webs
chest_radials = [(50, 850), (200, 850), (350, 850), (500, 850), (680, 850)]
for target in chest_radials:
    drawing_tasks.append((draw_line, ((310, 420), target, "#2b0407", 2)))

def draw_ellipse_step(bbox, fill):
    draw.ellipse(bbox, fill=fill)
    update_canvas()

drawing_tasks.append((draw_ellipse_step, ([300, 560, 320, 580], "#080a0e")))

legs = [
    [(305, 565), (260, 530), (220, 510)], [(305, 570), (250, 550), (200, 540)],
    [(305, 575), (255, 600), (210, 640)], [(305, 580), (270, 620), (230, 670)],
    [(315, 565), (360, 530), (400, 510)], [(315, 570), (370, 550), (420, 540)],
    [(315, 575), (365, 600), (410, 640)], [(315, 580), (350, 620), (390, 670)]
]

for leg in legs:
    drawing_tasks.append((draw_line, (leg[0], leg[1], "#080a0e", 3)))
    drawing_tasks.append((draw_line, (leg[1], leg[2], "#080a0e", 3)))

# ---------------- ANIMATION EXECUTION LOOP ----------------
current_task = 0

def execute_next_step():
    global current_task
    if current_task < len(drawing_tasks):
        func, args = drawing_tasks[current_task]
        func(*args)
        current_task += 1
        # Delay in milliseconds between steps (50ms = Smooth Live Animation)
        root.after(50, execute_next_step)

# Start drawing after 300ms window launch
root.after(300, execute_next_step)
root.mainloop()