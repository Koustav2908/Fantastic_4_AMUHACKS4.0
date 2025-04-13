import random
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"


class FlashCards:
    """
    A class-based flashcard quiz app using Tkinter.
    Displays questions with one correct and one incorrect answer button.
    """

    def __init__(self, question_list):
        """
        Initializes the GUI window, question data, buttons, canvas, and score tracking.

        Args:
            question_list (list): List of Question objects to be displayed.
        """

        self.question_list = question_list
        self.current_question = None
        self.score = 0
        self.question_index = 0

        # Initialize the main window
        self.window = tk.Tk()
        self.window.title(string="Flash Cards")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        # Canvas for card image and question text
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

        # Score label
        self.score_label = tk.Label(
            text="Score: 0", bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold")
        )
        self.score_label.grid(row=1, column=0, columnspan=2)

        # Buttons for answers (correct and wrong)
        self.correct_button = tk.Button(
            text="",
            command=self.choose_correct,
            width=30,
            height=4,
            font=("Ariel", 12, "bold"),
            wraplength=200,
            justify="center",
        )
        self.correct_button.grid(row=2, column=0)

        self.wrong_button = tk.Button(
            text="",
            command=self.choose_wrong,
            width=30,
            height=4,
            font=("Ariel", 12, "bold"),
            wraplength=200,
            justify="center",
        )
        self.wrong_button.grid(row=2, column=1)

        # Load the first question
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        """
        Loads the next question from the list and randomly places the correct answer
        on either the left or right button.
        """

        if self.question_index >= len(self.question_list):
            self.game_over()
            return

        # Reset card to front face
        self.canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.canvas.itemconfig(self.card_title, text="Question", fill="black")
        self.canvas.itemconfig(self.card_question, fill="black")

        self.current_question = self.question_list[self.question_index]
        self.question_index += 1

        # Randomly assign correct/wrong answer to buttons
        if random.choice([True, False]):
            self.correct_button.config(text=self.current_question.correct_answer)
            self.wrong_button.config(text=self.current_question.wrong_answer)
        else:
            self.correct_button.config(text=self.current_question.wrong_answer)
            self.wrong_button.config(text=self.current_question.correct_answer)

        self.canvas.itemconfig(self.card_question, text=self.current_question.question)

    def choose_correct(self):
        """
        Handles the correct answer button click event.
        """

        selected = self.correct_button["text"]
        self.reveal_answer(selected)

    def choose_wrong(self):
        """
        Handles the wrong answer button click event.
        """

        selected = self.wrong_button["text"]
        self.reveal_answer(selected)

    def reveal_answer(self, selected):
        """
        Reveals the correct answer, updates score if necessary, and shows feedback.

        Args:
            selected (str): The answer selected by the user.
        """

        is_correct = selected == self.current_question.correct_answer
        if is_correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.itemconfig(self.card_title, text="Correct!", fill="white")
        else:
            self.canvas.itemconfig(self.card_title, text="Wrong!", fill="white")

        # Flip card to show the back with the correct answer
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)
        self.canvas.itemconfig(self.card_title, text="Answer", fill="white")
        self.canvas.itemconfig(
            self.card_question, text=self.current_question.correct_answer, fill="white"
        )

        # Disable buttons temporarily
        self.correct_button.config(state="disabled")
        self.wrong_button.config(state="disabled")

        # Show feedback
        self.window.after(0, lambda: self.show_answer(is_correct))

    def show_answer(self, is_correct):
        """
        Displays final feedback ("Correct!" or "Wrong!") for the question.

        Args:
            is_correct (bool): Whether the user's answer was correct.
        """

        feedback = "Correct!" if is_correct else "Wrong!"
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)
        self.canvas.itemconfig(self.card_title, text=f"{feedback}", fill="white")
        self.canvas.itemconfig(
            self.card_question, text=self.current_question.correct_answer, fill="white"
        )

        # Wait another 3 seconds before moving on to the next question
        self.window.after(3000, self.load_next)

    def load_next(self):
        """
        Re-enables the answer buttons and moves on to the next question.
        """

        self.correct_button.config(state="normal")
        self.wrong_button.config(state="normal")
        self.next_question()

    def game_over(self):
        """
        Displays the game over message and final score.
        """

        self.canvas.itemconfig(self.card_title, text="Game Over", fill="black")
        self.canvas.itemconfig(
            self.card_question, text=f"Final Score: {self.score}", fill="black"
        )
        self.correct_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
