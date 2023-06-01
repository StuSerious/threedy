from datetime import datetime

import customtkinter as ctk
from modules.settings import *


class Terminal(ctk.CTkTextbox):
    def __init__(self, parent, **kwargs):
        super().__init__(
            master=parent,
            fg_color=TERMINAL_BG_COLOR,
            text_color=TERMINAL_TEXT_COLOR,
            **kwargs,
        )

        # configure layout
        self.grid(
            row=1,
            column=1,
            padx=PADDING["medium"],
            pady=PADDING["medium"],
            sticky="nsew",
        )

    # line insertion method
    def newline(self, line):
        """Inserts a new line at the top of the terminal, pushing the existing lines down the stack.
        Can also insert replacement patterns and f-strings.
        This method will also add time and terminal formatting.

        Args:
            line (string): the text that will be diplayed
        """
        self.now = datetime.now().strftime("%H:%M:%S")

        self.configure(state="normal")
        self.insert("0.0", f"{self.now} | $  {line}\n")
        self.configure(state="disabled")

        print(line)
