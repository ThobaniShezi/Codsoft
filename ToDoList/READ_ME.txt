To-Do List App
This application allows users to create, track, and receive notifications for tasks with specific due dates and times.

Features
Adding Tasks: Users can input tasks along with their due dates and times.
Real-time Tracking: The application provides real-time tracking of tasks and updates the remaining time dynamically.
Notification: When a task's time is up, a notification window pops up to remind the user.
Task Deletion: Users can delete tasks from the list either individually or by tracking all tasks.
Usage
Adding a Task:

Enter the task in the "Enter Task Here" entry field.
Select the due date using the date picker.
Press the "Add task" button or hit Enter.
Tracking Tasks:

Press the "Track List" button to open a new window displaying the current task list and remaining time for each task.
Tasks are automatically removed from the list once their time is up.
Deleting a Task:

In the tracking window, select a task from the list.
Press the "Delete Task" button to remove the selected task.
Exiting the App:

Press the "Exit" button to close the application.
Dependencies
Tkinter: Python's standard GUI (Graphical User Interface) package.
Threading: Used for handling background tasks and timers.
Tkcalendar: A DateEntry widget for Tkinter.
Running the App
Ensure you have Python and the required packages installed. Run the script, and the GUI application will appear.

bash
Copy code
python main.py

Note
The application uses threading for real-time updates. When exiting the application, the main thread is terminated along with the program.

