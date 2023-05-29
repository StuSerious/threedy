import customtkinter as ctk
from modules.settings import *


class Tabview(ctk.CTkTabview):
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)

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
            (
                0,
                1,
            ),
            weight=1,
        )

        # defaults
        self.normal_font = ctk.CTkFont(family=FONT, size=FONT_SIZE)

        # configure switches
        self.switch_configs = [
            ("Remove Comments", "remove_comments_switch"),
            ("Remove M-Codes", "remove_mcodes_switch"),
            ("Remove F/E-Codes", "remove_fecodes_switch"),
            ("Keep only G0 & G1 moves", "remove_nontravel_switch"),
            ("Remove lines with lonely G0/G1s", "remove_lone_gs_switch"),
        ]

        # create switches
        for row, (text, switch_attr) in enumerate(self.switch_configs):
            switch = ctk.CTkSwitch(
                self.tab("G-Code Tools"),
                text=text,
                font=self.normal_font,
                onvalue=True,
                offvalue=False,
            )
            setattr(self, switch_attr, switch)
            switch.grid(
                row=row,
                column=1,
                padx=PADDING["medium"],
                pady=PADDING["medium"],
                sticky="W",
            )

    def focused_tab(self):
        return self.get()
