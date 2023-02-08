import tkinter as tk

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

task_frame = tk.Frame(root)
task_frame.pack(pady=5)

task_entry = tk.Entry(task_frame, font=("Segoe UI", 14))
task_entry.pack(side="left", fill="x", expand=True)

add_icon = tk.PhotoImage(file=r"C:\Users\iyed\Desktop\code\check.png")
add_button = tk.Button(task_frame, image=add_icon, bd=0, bg="#0078d7", fg="#ffffff", command=add_task)
add_button.pack(side="left")

delete_button = tk.Button(root, text="Delete Task", font=("Segoe UI", 12), bd=0, bg="#0078d7", fg="#ffffff", command=delete_task)
delete_button.pack(pady=5)

task_list = tk.Listbox(root, font=("Segoe UI", 12))
task_list.pack()

root.mainloop()
