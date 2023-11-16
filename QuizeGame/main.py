import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("600x400")

        # Quiz questions and answers
        self.questions = [
            {
                'question': 'What is the output of the following code?\n\nsampleSet = {"Jodi", "Eric", "Garry"}\nsampleSet.add(1, "Vicki")\nprint(sampleSet)',
                'choices': [
                    '{‘Vicki’, ‘Jodi’, ‘Garry’, ‘Eric’}',
                    '{‘Jodi’, ‘Vicki’, ‘Garry’, ‘Eric’}',
                    'The program executed with error'
                ],
                'correct_answer': '{‘Jodi’, ‘Vicki’, ‘Garry’, ‘Eric’}'
            },
            {
                'question': 'Can we use the “else” block for for loop?\n\nfor i in range(1, 5):\nprint(i)\nelse:\n    print("this is else block statement")',
                'choices': [
                    'No',
                    'Yes'
                ],
                'correct_answer': 'No'
            },
            {
                'question': 'What is the output of the following code?\n\ndef calculate(num1, num2=4):\n    res = num1 * num2\n    print(res)\n\ncalculate(5, 6)',
                'choices': [
                    '20',
                    'The program executed with errors',
                    '30'
                ],
                'correct_answer': '30'
            },
            {
                'question': 'Which operator has higher precedence in the following list\n\n% (Modulus)\n& (BitWise AND)\n** (Exponent)\n> (Comparison)',
                'choices': [
                    '% (Modulus)',
                    '& (BitWise AND)',
                    '** (Exponent)',
                    '> (Comparison)'
                ],
                'correct_answer': '** (Exponent)'
            },
            {
                'question': 'What is the Output of the following code?\n\nfor x in range(0.5, 5.5, 0.5):\n    print(x)',
                'choices': [
                    '[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]',
                    '[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]',
                    'The Program executed with errors'
                ],
                'correct_answer': '[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]'
            },
        ]

        self.current_question = 0
        self.score = 0

        # Create widgets
        self.label_question = tk.Label(self.master, text="")
        self.label_question.pack(pady=10)

        self.var_choice = tk.StringVar()
        self.radio_buttons = []
        for i in range(3):  # Adjusted to match the maximum number of choices in any question
            radio_button = tk.Radiobutton(self.master, text="", variable=self.var_choice, value=str(i))
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        self.button_submit = tk.Button(self.master, text="Submit", command=self.submit_answer)
        self.button_submit.pack(pady=10)

        # Load the first question
        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.label_question.config(text=question_data['question'])

            for i in range(len(question_data['choices'])):
                self.radio_buttons[i].config(text=question_data['choices'][i])

            self.var_choice.set(None)  # Clear previous selection
        else:
            self.display_final_results()

    def submit_answer(self):
        if self.var_choice.get() is not None:
            user_answer = self.questions[self.current_question]['choices'][int(self.var_choice.get())]
            correct_answer = self.questions[self.current_question]['correct_answer']

            if user_answer == correct_answer:
                self.score += 1

            self.display_feedback(correct_answer)
            self.current_question += 1
            self.load_question()

    def display_feedback(self, correct_answer):
        user_answer = self.questions[self.current_question]['choices'][int(self.var_choice.get())]
        feedback = f"Your answer: {user_answer}\n"

        if user_answer == correct_answer:
            feedback += "Correct!"
        else:
            feedback += f"Incorrect. The correct answer is: {correct_answer}"

        messagebox.showinfo("Feedback", feedback)

    def display_final_results(self):
        messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}")
        self.ask_play_again()

    def ask_play_again(self):
        response = messagebox.askquestion("Play Again", "Do you want to play again?")
        if response == 'yes':
            self.current_question = 0
            self.score = 0
            self.load_question()
        else:
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
