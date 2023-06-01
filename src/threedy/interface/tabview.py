import customtkinter as ctk
from interface.terminal import Terminal
from modules.settings import *


class Tabview(ctk.CTkTabview):
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)
        # defaults
        self.normal_font = ctk.CTkFont(family=FONT, size=FONT_SIZE)
        self.terminal = Terminal
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

        # setup G-Code tab
        self.add("G-Code Tools")
        self.tab("G-Code Tools").grid_columnconfigure(
            0,
            weight=1,
        )
        self.tab("G-Code Tools").grid_columnconfigure(
            (1, 2),
            weight=2,
        )

        # select all switch
        self.select_all_gcode_label = ctk.CTkLabel(
            self.tab("G-Code Tools"),
            text="Select All:",
            font=ctk.CTkFont(family=FONT, size=FONT_SIZE, weight="bold"),
        )
        self.select_all_gcode_label.grid(
            row=0,
            column=0,
            padx=PADDING["medium"],
            pady=(PADDING["none"], PADDING["none"]),
            sticky="nw",
        )
        self.select_all_gcode_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="",
            command=self.toggle_all_switches,
        )
        self.select_all_gcode_switch.grid(
            row=1,
            column=0,
            padx=PADDING["medium"],
            pady=(PADDING["none"], PADDING["medium"]),
            sticky="nw",
        )

        self.gcode_switch_data = [
            {
                "text": "Remove Comments",
                "variable": "remove_comments_switch",
                "row": 0,
                "column": 1,
            },
            {
                "text": "Remove M-Codes",
                "variable": "remove_mcodes_switch",
                "row": 1,
                "column": 1,
            },
            {
                "text": "Remove F/E-Codes",
                "variable": "remove_fecodes_switch",
                "row": 2,
                "column": 1,
            },
            {
                "text": "Keep only G0 & G1 moves",
                "variable": "remove_nontravel_switch",
                "row": 0,
                "column": 2,
            },
            {
                "text": "Remove lines with lonely G0/G1s",
                "variable": "remove_lone_gs_switch",
                "row": 1,
                "column": 2,
            },
            {
                "text": "Remove coordinate names",
                "variable": "remove_coordname_switch",
                "row": 2,
                "column": 2,
            },
        ]

        for data in self.gcode_switch_data:
            switch_variable = data["variable"]
            switch = ctk.CTkCheckBox(
                self.tab("G-Code Tools"),
                text=data["text"],
                font=self.normal_font,
                onvalue=True,
                offvalue=False,
            )
            setattr(self, switch_variable, switch)
            switch.grid(
                row=data["row"],
                column=data["column"],
                padx=PADDING["small"],
                pady=PADDING["small"],
                sticky="W",
            )

    def toggle_all_switches(self):
        """iterates over every switch and toggles it"""
        for data in self.gcode_switch_data:
            switch_variable = data["variable"]
            if isinstance(switch_variable, str):
                # Get the actual variable object based on its name
                switch_variable = getattr(self, switch_variable)
            if self.select_all_gcode_switch.get() == False:
                switch_variable.deselect()
                self.select_all_gcode_label.configure(text="Select All:")
            else:
                switch_variable.select()
                self.select_all_gcode_label.configure(text="Deselect All:")
        # self.terminal.newline("Selected all G-Code modifiers")

    def selected_tab(self):
        """Returns the currently selected tab

        Returns:
            string: current tab name
        """
        return self.get()
