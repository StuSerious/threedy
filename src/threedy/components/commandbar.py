import customtkinter as ctk
from modules.settings import *


class Commandbar(ctk.CTkFrame):
    def __init__(self, parent, compute_event, **kwargs):
        super().__init__(master=parent, **kwargs)
        self.compute_event = compute_event

        self.normal_font = ctk.CTkFont(
            family=FONT, size=FONT_SIZE, weight=FONT_WEIGHT[0]
        )
        # grid layout
        self.grid(row=4, column=1, columnspan=4, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # setup commandbar
        self.cli_entry = ctk.CTkEntry(
            self,
            placeholder_text="[WIP] - Optional CLI arguments:",
            font=self.normal_font,
        )
        self.cli_entry.grid(
            row=0,
            column=0,
            padx=(PADDING["medium"], PADDING["none"]),
            pady=PADDING["medium"],
            sticky="nsew",
        )

        # compute button
        self.compute_button = ctk.CTkButton(
            self,
            text="2) Compute",
            font=self.normal_font,
            command=self.compute_changes,
        )
        self.compute_button.grid(
            row=0,
            column=1,
            padx=PADDING["medium"],
            pady=PADDING["medium"],
            sticky="NSEW",
        )

    def compute_changes(self):
        self.compute_event()
