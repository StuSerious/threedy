import customtkinter as ctk
from modules.settings import *


class Tabview(ctk.CTkTabview):
    def __init__(self, parent, select_all_event, **kwargs):
        super().__init__(master=parent, **kwargs)
        # defaults
        self.select_all_event = select_all_event
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
            (
                0,
                1,
            ),
            weight=1,
        )

        self.select_all_gcode = ctk.CTkCheckBox(
            self.tab("G-Code Tools"),
            text="Select All",
            command=self.enable_all_switches,
        )
        self.select_all_gcode.grid(row=0, column=0)

        self.switch_data = [
            {
                "text": "Remove Comments",
                "variable": "remove_comments_switch",
                "row": 0,
            },
            {
                "text": "Remove M-Codes",
                "variable": "remove_mcodes_switch",
                "row": 1,
            },
            {
                "text": "Remove F/E-Codes",
                "variable": "remove_fecodes_switch",
                "row": 2,
            },
            {
                "text": "Keep only G0 & G1 moves",
                "variable": "remove_nontravel_switch",
                "row": 3,
            },
            {
                "text": "Remove lines with lonely G0/G1s",
                "variable": "remove_lone_gs_switch",
                "row": 4,
            },
            {
                "text": "Remove coordinate names",
                "variable": "remove_coordname_switch",
                "row": 5,
            },
        ]

        for data in self.switch_data:
            switch_variable = data["variable"]
            switch = ctk.CTkSwitch(
                self.tab("G-Code Tools"),
                text=data["text"],
                font=self.normal_font,
                onvalue=True,
                offvalue=False,
            )
            setattr(self, switch_variable, switch)
            switch.grid(
                row=data["row"],
                column=1,
                padx=PADDING["medium"],
                pady=PADDING["medium"],
                sticky="W",
            )

    def enable_all_switches(self):
        self.select_all_event()

    def focused_tab(self):
        return self.get()
