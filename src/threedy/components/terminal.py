from datetime import datetime

import customtkinter as ctk
from modules.settings import *


class Terminal(ctk.CTkTextbox):
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)

        # configure layout
        self.grid(
            row=1,
            column=1,
            padx=PADDING_M,
            pady=(PADDING_M, 0),
            sticky="nsew",
        )

    # line insertion method
    def newline(self, line):
        self.now = datetime.now().strftime("%H:%M:%S")
        self.configure(state="normal")
        self.insert("0.0", f"$ {self.now} >   {line}")
        self.configure(state="disabled")
