import tkinter as tk
import random

root = tk.Tk()
root.title("ShakilAI - Fun Clicker Game")
root.geometry("400x300")
root.configure(bg="#222")

score = 0
def on_click():
    global score
    score += 1
    label.config(text=f"স্কোর: {score}")
    btn.place(x=random.randint(20, 300), y=random.randint(50, 220))

label = tk.Label(root, text="স্কোর: 0", font=("Arial", 18, "bold"), fg="#00ffcc", bg="#222")
label.pack(pady=20)

btn = tk.Button(root, text="ক্লিক করো!", font=("Arial", 14, "bold"), bg="#ff5722", fg="#fff", command=on_click)
btn.place(x=150, y=130)

root.mainloop()