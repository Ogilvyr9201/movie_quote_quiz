from tkinter import *


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
                                 text="Press the Green button to Start",
                                 fg="#00b816", padx=10, pady=10,
                                 font=("Arial", "12", "bold"))
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
                                   activebackground="#6bcf7d")
        self.start_button.grid(row=0, column=1,
                               padx=5, pady=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    Menu()
    root.mainloop()
