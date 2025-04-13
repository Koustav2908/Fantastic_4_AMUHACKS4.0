import random
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"


class FlashCards:
    def __init__(self, question_list):
        self.question_list = question_list
        self.current_question = None
        self.score = 0
        self.question_index = 0

        self.window = tk.Tk()
        self.window.title(string="Flash Cards")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.canvas = tk.Canvas(width=800, height=526, highlightthickness=0)
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_front_img = tk.PhotoImage(file="images/card_front.png")
        self.card_back_img = tk.PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(
            400, 263, image=self.card_front_img
        )
        self.card_title = self.canvas.create_text(
            400, 150, text="", font=("Ariel", 40, "italic")
        )
        self.card_question = self.canvas.create_text(
            400, 263, text="", font=("Ariel", 24, "bold"), width=600
        )
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.score_label = tk.Label(
            text="Score: 0", bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold")
        )
        self.score_label.grid(row=1, column=0, columnspan=2)

        self.correct_button = tk.Button(
            text="",
            command=self.choose_correct,
            width=30,
            height=3,
            font=("Ariel", 12, "bold"),
            wraplength=200,
            justify="center",
        )
        self.correct_button.grid(row=2, column=0)

        self.wrong_button = tk.Button(
            text="",
            command=self.choose_wrong,
            width=30,
            height=3,
            font=("Ariel", 12, "bold"),
            wraplength=200,
            justify="center",
        )
        self.wrong_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.question_index >= len(self.question_list):
            self.game_over()
            return

        self.canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.canvas.itemconfig(self.card_title, text="Question", fill="black")
        self.canvas.itemconfig(self.card_question, fill="black")

        self.current_question = self.question_list[self.question_index]
        self.question_index += 1

        if random.choice([True, False]):
            self.correct_button.config(text=self.current_question.correct_answer)
            self.wrong_button.config(text=self.current_question.wrong_answer)
        else:
            self.correct_button.config(text=self.current_question.wrong_answer)
            self.wrong_button.config(text=self.current_question.correct_answer)

        self.canvas.itemconfig(self.card_question, text=self.current_question.question)

    def choose_correct(self):
        selected = self.correct_button["text"]
        self.reveal_answer(selected)

    def choose_wrong(self):
        selected = self.wrong_button["text"]
        self.reveal_answer(selected)

    def reveal_answer(self, selected):
        is_correct = selected == self.current_question.correct_answer
        if is_correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.itemconfig(self.card_title, text="Correct!", fill="white")
        else:
            self.canvas.itemconfig(self.card_title, text="Wrong!", fill="white")

        # Flip to back side
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)
        self.canvas.itemconfig(self.card_title, text="Answer", fill="white")
        self.canvas.itemconfig(
            self.card_question, text=self.current_question.correct_answer, fill="white"
        )

        # Disable buttons temporarily
        self.correct_button.config(state="disabled")
        self.wrong_button.config(state="disabled")

        self.window.after(1000, lambda: self.show_answer(is_correct))

    def show_answer(self, is_correct):
        feedback = "Correct!" if is_correct else "Wrong!"
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)
        self.canvas.itemconfig(self.card_title, text=f"{feedback}", fill="white")
        self.canvas.itemconfig(
            self.card_question, text=self.current_question.correct_answer, fill="white"
        )

        # Wait another 5 seconds before moving on to the next question
        self.window.after(5000, self.load_next)

    def load_next(self):
        self.correct_button.config(state="normal")
        self.wrong_button.config(state="normal")
        self.next_question()

    def game_over(self):
        self.canvas.itemconfig(self.card_title, text="Game Over", fill="black")
        self.canvas.itemconfig(
            self.card_question, text=f"Final Score: {self.score}", fill="black"
        )
        self.correct_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
