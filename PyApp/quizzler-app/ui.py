import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizUI(tk.Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.quiz = quiz_brain
        self.title("Quizzler")
        self.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = tk.Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            float(self.canvas['width'])/2,
            float(self.canvas['height'])/2,
            width=float(self.canvas['width']) - 20,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_img, highlightthickness=0, command=lambda: self.validate_ans(True))
        self.true_button.grid(row=2, column=0)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0, command=lambda: self.validate_ans(False))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def validate_ans(self, ans: bool):
        if self.quiz.check_answer(ans):
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.after(1000, self.get_next_question)


