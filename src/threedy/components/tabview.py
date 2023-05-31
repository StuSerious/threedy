import customtkinter as ctk
from modules.settings import *


class Tabview(ctk.CTkTabview):
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)
        # defaults
        self.normal_font = ctk.CTkFont(family=FONT, size=FONT_SIZE)

        # setup layout
        self.grid(
            row=0,
            column=1,
            columnspan=2,
            padx=PADDING["medium"],
            pady=PADDING["none"],
            sticky="nsew",
        )
        self.grid_rowconfigure(3, weight=1)

        # add tabs
        self.add("G-Code Tools")
        self.add("CSV Tools")

        # setup tabs
        self.tab("G-Code Tools").grid_columnconfigure(
            (0, 1),
            weight=1,
        )

        self.ansys_prep_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Tabulate G-Code for Ansys",
            onvalue=True,
            offvalue=False,
        )
        self.ansys_prep_switch.grid(row=0, column=0)

    def focused_tab(self):
        """Returns the currently selected tab

        Returns:
            string: current tab name
        """
        return self.get()
