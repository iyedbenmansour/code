import tkinter as tk
from PIL import Image, ImageTk

tasks = []

def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_list.insert("end", task)
    task_entry.delete(0, "end")

def delete_task():
    current_selection = task_list.curselection()
    if current_selection:
        task_index = current_selection[0]
        task_list.delete(task_index)
        tasks.pop(task_index)

root = tk.Tk()
root.title("To-Do List")

img = Image.open("bg.jpg")
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(img)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

task_frame = tk.Frame(root, bg="#d3d3d3")
task_frame.pack(pady=5)

task_entry = tk.Entry(task_frame, font=("Segoe UI", 14), bg="#d3d3d3")
task_entry.pack(side="left", fill="x", expand=True)

add_icon = tk.PhotoImage(file="check.png")
add_button = tk.Button(task_frame, image=add_icon, bd=0, bg="#0078d7", fg="#ffffff", command=add_task, height=20, width=20)
add_button.pack(side="left")

task_list = tk.Listbox(root, font=("Segoe UI", 12))
task_list.pack()

delete_icon = Image.open("C:/Users/iyed/Desktop/code/delete.png")
delete_icon = delete_icon.resize((30, 30), Image.ANTIALIAS)
delete_icon = ImageTk.PhotoImage(delete_icon)

delete_button = tk.Button(root, bd=0, bg="#0078d7", fg="#ffffff", width=30, height=30, command=delete_task)
delete_button.pack(pady=5)

delete_image = tk.Label(delete_button, image=delete_icon)
delete_image.pack()

root.mainloop()
