import random
import json
import tkinter as tk
from tkinter import messagebox

class Flashcard:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question}\nOptions: {', '.join(self.options)}\nAnswer: {self.answer}"

class FlashcardDeck:
    def __init__(self):
        self.cards = []
        self.score = 0

    def add_card(self, card):
        self.cards.append(card)

    def save_deck(self, filename):
        with open(filename, 'w') as file:
            json.dump([{'question': card.question, 'options': card.options, 'answer': card.answer} for card in self.cards], file)

    def load_deck(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.cards = [Flashcard(card['question'], card['options'], card['answer']) for card in data]

    def study(self):
        random.shuffle(self.cards)
        for card in self.cards:
            response = self.study_card(card)
            if response.lower() == card.answer.lower():
                self.score += 1
                messagebox.showinfo("Correct", "Correct!")
            else:
                messagebox.showerror("Incorrect", f"Incorrect. The correct answer is: {card.answer}")

        messagebox.showinfo("Study Complete", f"Study session completed. Your score: {self.score}/{len(self.cards)}")

    def study_card(self, card):
        root = tk.Tk()
        root.title("Flashcard")
        question_label = tk.Label(root, text=card.question)
        question_label.pack()

        def on_submit():
            selected_option = options_var.get()
            root.destroy()
            return selected_option

        options_var = tk.StringVar(value=card.options)
        options_radio = [tk.Radiobutton(root, text=option, variable=options_var, value=option) for option in card.options]
        for option_radio in options_radio:
            option_radio.pack()

        submit_button = tk.Button(root, text="Submit", command=on_submit)
        submit_button.pack()

        root.mainloop()

        return options_var.get()

# Example usage:
deck = FlashcardDeck()
deck.add_card(Flashcard("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris"))
deck.add_card(Flashcard("What is 2 + 2?", ["3", "4", "5", "6"], "4"))

# Save flashcards to a file
deck.save_deck("flashcards.json")

# Load flashcards from file
deck.load_deck("flashcards.json")

# Study flashcards
deck.study()