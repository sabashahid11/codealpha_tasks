#hangman game 
import tkinter as tk
import random

words = ["apple", "table", "study", "chair", "cloud"]

def new_game():
    global secret_word, guessed_letters, tries, used_hint

    secret_word = random.choice(words)
    guessed_letters = []
    tries = 6
    used_hint = False

    tries_label.config(text="Tries left: " + str(tries))
    message_label.config(text="")
    guess_button.config(state="normal")
    hint_button.config(state="normal")
    replay_button.pack_forget()
    update_display()

def update_display():
    display_text = ""
    for ch in secret_word:
        if ch in guessed_letters:
            display_text += ch + " "
        else:
            display_text += "_ "
    word_label.config(text=display_text)

def guess_letter():
    global tries
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter or len(letter) != 1:
        message_label.config(text="Please enter one letter")
        return

    if letter in guessed_letters:
        message_label.config(text="This letter is already used")
        return

    guessed_letters.append(letter)

    if letter not in secret_word:
        tries -= 1
        tries_label.config(text="Tries left: " + str(tries))
        message_label.config(text="Wrong guess")
    else:
        message_label.config(text="Good guess")

    update_display()
    check_win_or_loss()

def use_hint():
    global used_hint

    if used_hint:
        message_label.config(text="You already used your hint")
        return

    remaining = [ch for ch in secret_word if ch not in guessed_letters]

    if not remaining:
        message_label.config(text="No hint needed")
        return

    hint_letter = random.choice(remaining)
    guessed_letters.append(hint_letter)
    used_hint = True

    message_label.config(text="Your hint letter is: " + hint_letter)
    update_display()
    check_win_or_loss()

def check_win_or_loss():
    global tries

    if all(ch in guessed_letters for ch in secret_word):
        message_label.config(text="You won")
        congratulate()
        guess_button.config(state="disabled")
        hint_button.config(state="disabled")
        replay_button.pack(pady=10)

    if tries == 0:
        message_label.config(text="You lost. Word was: " + secret_word)
        guess_button.config(state="disabled")
        hint_button.config(state="disabled")
        replay_button.pack(pady=10)

def congratulate():
    win_window = tk.Toplevel(root)
    win_window.title("Congrats")
    win_window.config(bg="lavender")
    msg = tk.Label(win_window, text="You won the game", font=("Arial", 18), bg="lavender", fg="purple")
    msg.pack(pady=20)
    msg2 = tk.Label(win_window, text="A tiny victory spark just floated in your direction", font=("Arial", 12), bg="lavender", fg="dark blue")
    msg2.pack(pady=10)
    ok_btn = tk.Button(win_window, text="Nice", command=win_window.destroy, bg="white", fg="black")
    ok_btn.pack(pady=10)

root = tk.Tk()
root.title("Hangman Game")
root.config(bg="lavender")

word_label = tk.Label(root, font=("Arial", 24), bg="lavender", fg="dark blue")
word_label.pack(pady=10)

tries_label = tk.Label(root, text="", font=("Arial", 14), bg="lavender", fg="black")
tries_label.pack()

entry = tk.Entry(root, font=("Arial", 14), bg="white", fg="black")
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Arial", 14), bg="white", fg="black")
guess_button.pack()

hint_button = tk.Button(root, text="Hint", command=use_hint, font=("Arial", 14), bg="light yellow", fg="black")
hint_button.pack(pady=5)

replay_button = tk.Button(root, text="Play again", command=new_game, font=("Arial", 14), bg="light green", fg="black")

message_label = tk.Label(root, font=("Arial", 12), bg="lavender", fg="purple")
message_label.pack(pady=10)

new_game()
root.mainloop()

