from tkinter import *
from functools import partial
import csv
import random


class Menu:

    def __init__(self):
        # common format for all buttons
        # Arial size 14 bold with white text
        button_font = ("Arial", "12")
        button_fg = "#000000"

        # Set up GUI Frame
        self.chose_rounds_frame = Frame(padx=10, pady=10)
        self.chose_rounds_frame.grid()

        self.menu_heading = Label(self.chose_rounds_frame,
                                  text="Movie Quote Quiz",
                                  font=("Arial", "18", "bold"))
        self.menu_heading.grid(row=0)

        instructions = "Welcome to the Movie Quote Quiz! In this quiz " \
                       "a quote from a movie will appear and 4 different " \
                       "movies will appear below. You will have to guess which " \
                       "movie you think the quote comes from. Your stats will " \
                       "appear when you hit the 'statistics' button while in game.\n\n" \
                       "Please enter the amount of rounds in bar below or leave blank " \
                       "for infinite mode!"
        self.menu_instructions = Label(self.chose_rounds_frame,
                                       text=instructions,
                                       wraplength=220, width=35,
                                       justify="left",
                                       pady=10, bg="#DAE8FC",
                                       highlightbackground="#728fb8",
                                       highlightthickness=1)
        self.menu_instructions.grid(row=1)

        self.error_label = Label(self.chose_rounds_frame,
                                 text="Leave blank for infinite mode",
                                 fg="#00b816", padx=10, pady=10,
                                 font=("Arial", "12", "bold"),
                                 wraplength=220)
        self.error_label.grid(row=2)

        self.entry_button_frame = Frame(self.chose_rounds_frame)
        self.entry_button_frame.grid(row=3)

        self.rounds_entry = Entry(self.entry_button_frame, width=10,
                                  font=("Arial", 18))
        self.rounds_entry.grid(row=0, column=0)

        self.start_button = Button(self.entry_button_frame,
                                   text="Start",
                                   font=button_font, width=10,
                                   bg="#8af29b",
                                   fg=button_fg,
                                   activebackground="#6bcf7d",
                                   command=lambda: self.check_rounds())
        self.start_button.grid(row=0, column=1,
                               padx=5, pady=5)

    def check_rounds(self):
        has_error = "no"
        error = "Please enter a number above 0"

        response = self.rounds_entry.get()

        if response == "":
            self.error_label.config(text="Number of rounds: infinite",
                                    fg="#00b816")
            self.to_play("infinite")

        # check that user has entered a valid number...
        try:
            response = int(response)

            if response <= 0:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # give response if there is error or not
        if has_error == "yes":
            self.error_label.config(text=error,
                                    fg="#b30000")
        else:
            self.error_label.config(text="Number of rounds: {}".format(response),
                                    fg="#00b816")
            self.to_play(response)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # hide Menu
        root.withdraw()


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        # if users press cross at tip, closes help and
        # 'refuses' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        self.in_quiz_frame = Frame(self.play_box, padx=10, pady=10)
        self.in_quiz_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.in_quiz_frame,
                                    text=rounds_heading,
                                    font=("Arial", "16", "bold"))
        self.choose_heading.grid(row=0)

        self.question = self.generate_quote_answers()
        self.quote = self.question[0]

        self.quote_label = Label(self.in_quiz_frame,
                                 text='Quote:\n"{}"'.format(self.quote),
                                 justify="left", wraplength=290, width=31,
                                 font=("Arial", "12"),
                                 bg="#D5E8D4", pady=5, padx=10,
                                 highlightbackground="#77a674",
                                 highlightthickness=1)
        self.quote_label.grid(row=1, column=0)

        self.options_frame = Frame(self.in_quiz_frame)
        self.options_frame.grid(row=2)

        # A list of buttons to make a for loop that calls
        answers = self.question[2]
        # randomise a list of 4 positions to make the answers randomise positions'
        position_list = [0, 1, 2, 3]
        random.shuffle(position_list)
        # the list and makes the button
        option_button_list = [
            [0, 0, answers[0]],
            [0, 1, answers[1]],
            [1, 0, answers[2]],
            [1, 1, self.question[1]]
        ]

        for item in range(0, 4):
            self.option_button = Button(self.options_frame,
                                        width=16, height=3,
                                        bg="#FFF2CC", text=option_button_list[item][2],
                                        font=("Arial", 11),
                                        wraplength=150, activebackground="#FFF2CC",
                                        highlightbackground="#C9BFA1",
                                        highlightthickness=1)
            self.option_button.grid(row=option_button_list[position_list[item - 1]][0],
                                    column=option_button_list[position_list[item - 1]][1],
                                    padx=5, pady=5)

        # recycling from colour game the control buttons stay the same
        self.control_frame = Frame(self.in_quiz_frame)
        self.control_frame.grid(row=7)

        # a list to make my control buttons at the bottom vary
        control_buttons = [
            ["#99CCFF", "Help", "get help"],
            ["#FFB366", "Statistics", "get stats"],
            ["#B3FF66", "Start Over", "start over"]
        ]

        # list to hold  references for control buttons
        # so that the text of the 'start over' button
        # con easily be configured when the game
        self.control_button_ref = []

        for item in range(0, 3):
            self.make_control_button = Button(self.control_frame,
                                              bg=control_buttons[item][0],
                                              text=control_buttons[item][1],
                                              width=9, font=("Arial", 12, "bold"))
            self.make_control_button.grid(row=0, column=item, padx=5, pady=5)

            # add buttons to control list
            self.control_button_ref.append(self.make_control_button)

        # disable help button
        self.to_help_btn = self.control_button_ref[0]
        self.to_stats_btn = self.control_button_ref[1]

        self.to_stats_btn.config(state=DISABLED)

        self.temp_state_frame = Frame(self.in_quiz_frame)
        self.temp_state_frame.grid(row=6, padx=10, pady=10)

        self.next_round_button = Button(self.temp_state_frame,
                                        text="Next Round",
                                        font=("Arial", "12"),
                                        bg="#e88cff")
        self.next_round_button.grid(row=0, column=1, padx=10)

        self.stats_label = Label(self.temp_state_frame,
                                 text="Correct:     Incorrect:   ",
                                 justify="left",
                                 font=("Arial", "12"),
                                 bg="#ffe380", pady=5, padx=10,
                                 highlightbackground="#e3c96f",
                                 highlightthickness=1)
        self.stats_label.grid(row=0, column=0)

    def close_play(self):
        # reshow menu
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


    def generate_quote_answers(self):
        file = open("movie_quotes.csv", "r")
        movie_quotes = list(csv.reader(file, delimiter=","))
        file.close()

        # remove the first row (header values
        movie_quotes.pop(0)

        # get a random row to get the question and correct answer from
        correct_info = random.choice(movie_quotes)

        question = correct_info[0]
        self.answer = correct_info[1]
        answers = []
        # make a new list to put all the quotes in
        all_movies = []
        for item in movie_quotes:
            all_movies.append(item[1])

        # pick three random answers
        for i in range(0, 3):
            while True:
                rand_movie = random.choice(all_movies)
                print(rand_movie)
                # check if answer is the same as correct
                if rand_movie != self.answer and rand_movie not in answers:
                    answers.append(rand_movie)
                    break

        return [question, self.answer, answers]


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    Menu()
    root.mainloop()
