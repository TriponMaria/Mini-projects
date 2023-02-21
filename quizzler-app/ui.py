from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_TEXT = ("Arial", 15, "italic")


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question text",
            fill=THEME_COLOR,
            font=FONT_TEXT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.true_clicked, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.false_clicked, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text=f"Score: {self.quiz.score} ", background=THEME_COLOR, foreground="white")
        self.score_label.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
