import tkinter
import threading
from tkinter import simpledialog
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime, timedelta
import sys

tasks = []
timer = threading
real_timer = threading
ok_thread = True


def get_entry(event=""):
    text = todo.get()
    selected_date = date_calendar.get_date()
    selected_time = get_selected_time()

    selected_datetime = datetime.combine(selected_date, selected_time)
    current_datetime = datetime.now()
    time_difference = selected_datetime - current_datetime
    seconds = int(time_difference.total_seconds())

    todo.delete(0, tkinter.END)
    date_calendar.set_date(datetime.now())  # Reset to the current date
    todo.focus_set()
    add_list(text, seconds)
    if 0 < seconds < 999:
        update_list()


def get_selected_time():
    result = simpledialog.askstring("Time Selection", "Enter time in HH:MM format:")
    try:
        selected_time = datetime.strptime(result, "%H:%M").time()
    except (ValueError, TypeError):
        selected_time = datetime.now().time()  # Default to the current time if invalid input
    return selected_time


def add_list(text, seconds):
    tasks.append([text, seconds])
    timer = threading.Timer(seconds, time_passed, [text])
    timer.start()


def update_list():
    if todolist.size() > 0:
        todolist.delete(0, "end")
    for task in tasks:
        hours_left = task[1] // 3600  # Convert seconds to hours
        minutes_left = (task[1] % 3600) // 60  # Convert remaining seconds to minutes
        seconds_left = task[1] % 60  # Remaining seconds
        todolist.insert("end", "[{}] Time left: {:02}:{:02}:{:02}".format(task[0], hours_left, minutes_left,
                                                                           seconds_left))


def time_passed(task):
    tkinter.messagebox.showinfo("Notification", "Time for : " + task)


def real_time():
    if ok_thread:
        real_timer = threading.Timer(1.0, real_time)
        real_timer.start()
    for task in tasks:
        if task[1] == 0:
            tasks.remove(task)
        task[1] -= 1
    update_list()


def track_list():
    track_window = tkinter.Toplevel(app)
    track_window.title("CodSoft To-Do List")

    track_listbox = tkinter.Listbox(track_window)
    track_listbox.pack(padx=20, pady=20)

    for task in tasks:
        hours_left = task[1] // 3600  # Convert seconds to hours
        minutes_left = (task[1] % 3600) // 60  # Convert remaining seconds to minutes
        seconds_left = task[1] % 60  # Remaining seconds
        track_listbox.insert("end", "[{}] Time left: {:02}:{:02}:{:02}".format(task[0], hours_left, minutes_left,
                                                                               seconds_left))

    delete_task_button = tkinter.Button(track_window, text='Delete Task', fg="#ffffff", bg='#EB6464', height=2, width=20,
                                        command=lambda: delete_task(track_listbox))
    delete_task_button.pack()


def delete_task(listbox):
    selected_index = listbox.curselection()
    if selected_index:
        task_index = selected_index[0]
        deleted_task = tasks.pop(task_index)
        update_list()
        tkinter.messagebox.showinfo("Deleted", "Task deleted: " + str(deleted_task))


if __name__ == '__main__':
    # application
    app = tkinter.Tk()
    app.geometry("480x680")
    app.title("Todolist Remainder")
    app.rowconfigure(0, weight=1)

    # Set background color
    app.configure(bg="#5DA271")  # Green color

    # fenetre
    frame = tkinter.Frame(app)
    frame.pack()

    # widgets
    label = tkinter.Label(app, text="Enter Task Here:", fg="#000000", wraplength=200, justify=tkinter.LEFT)
    label_datetime = tkinter.Label(app, text="Select Date:", fg="#000000", wraplength=200, justify=tkinter.LEFT)
    todo = tkinter.Entry(app, width=30)
    date_calendar = DateEntry(app, width=17, background='darkblue', foreground='white', borderwidth=2)
    send = tkinter.Button(app, text='Add task', fg="#ffffff", bg='#6186AC', height=3, width=40, command=get_entry)
    quit = tkinter.Button(app, text='Exit', fg="#ffffff", bg='#EB6464', height=3, width=30, command=app.destroy)
    todolist = tkinter.Listbox(app)
    track_list_button = tkinter.Button(app, text='Track List', fg="#ffffff", bg='#6186AC', height=3, width=30,
                                       command=track_list)

    if tasks != "":
        real_time()

    # binding
    app.bind('<Return>', get_entry)

    # widgets placement
    label.place(x=0, y=10, width=200, height=25)
    label_datetime.place(x=235, y=10, width=200, height=25)
    todo.place(x=62, y=30, width=200, height=25)
    date_calendar.place(x=275, y=30, width=150, height=25)
    send.place(x=62, y=60, width=60, height=25)
    quit.place(x=302, y=60, width=50, height=25)
    todolist.place(x=60, y=100, width=300, height=300)
    track_list_button.place(x=162, y=60, width=120, height=25)

    app.mainloop()
    ok_thread = False
    sys.exit("FINISHED")
