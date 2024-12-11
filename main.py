import tkinter as tk
from tkinter import messagebox


def count_e_in_words():
    words = ["elephant", "envelope", "exercise", "cheese", "engine", "tree", "ember", "bee", "enter", "example"]
    result = ""
    total_count = 0

    for word in words:
        count = word.count("e")
        total_count += count
        result += f"Slovo '{word}' má {count} písmen 'e'.\n"

    result += f"\nCelkový počet písmen 'e' vo všetkých slovách: {total_count}"
    messagebox.showinfo("Výsledok", result)


def create_gradient(canvas, width, height, color1, color2):
    """
    Vytvára gradient na Canvas.
    """
    for i in range(height):
        ratio = i / height
        r = int(color1[0] + ratio * (color2[0] - color1[0]))
        g = int(color1[1] + ratio * (color2[1] - color1[1]))
        b = int(color1[2] + ratio * (color2[2] - color1[2]))
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)


# Hlavné okno
app = tk.Tk()
app.title("Programovacie techniky")
app.geometry("500x400")

# Canvas pre gradient
canvas = tk.Canvas(app, width=500, height=400)
canvas.pack(fill="both", expand=True)

# Vytvorenie gradientu (farebné prechody)
color_start = (85, 120, 255)  # Svetlomodrá
color_end = (255, 150, 200)   # Svetloružová
create_gradient(canvas, 500, 400, color_start, color_end)

# Popisné texty
header = tk.Label(app, text="Programovacie techniky", font=("Arial", 18, "bold"), bg="#5578ff", fg="white")
header.place(relx=0.5, y=30, anchor="center")

author_info = tk.Label(
    app,
    text="Meno: Vladyslav Kysil\nZadanie úlohy: Spočítanie 'e' v slovách",
    font=("Arial", 12),
    bg="#5578ff",
    fg="white",
)
author_info.place(relx=0.5, y=100, anchor="center")

# Tlačidlo na spustenie programu
run_button = tk.Button(
    app,
    text="Spustiť program",
    font=("Arial", 14),
    bg="#ff96c8",
    fg="white",
    activebackground="#ff96c8",
    activeforeground="white",
    command=count_e_in_words,
)
run_button.place(relx=0.5, y=250, anchor="center")

# Spustenie hlavnej slučky GUI
app.mainloop()