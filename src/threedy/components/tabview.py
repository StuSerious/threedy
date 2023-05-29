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

        # rm comments
        self.remove_comments_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Remove Comments",
            font=self.normal_font,
            onvalue=True,
            offvalue=False,
        )
        self.remove_comments_switch.grid(
            row=0,
            column=1,
            padx=PADDING["medium"],
            pady=PADDING["medium"],
            sticky="W",
        )

        # rm M-Codes
        self.remove_mcodes_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Remove M-Codes",
            font=self.normal_font,
            onvalue=True,
            offvalue=False,
        )
        self.remove_mcodes_switch.grid(
            row=1,
            column=1,
            padx=PADDING["medium"],
            pady=PADDING["medium"],
            sticky="W",
        )

        # rm FE-Codes
        self.remove_fecodes_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Remove F/E-Codes",
            font=self.normal_font,
            onvalue=True,
            offvalue=False,
        )
        self.remove_fecodes_switch.grid(
            row=2,
            column=1,
            padx=PADDING["medium"],
            pady=PADDING["medium"],
            sticky="W",
        )

        # remove non trafel G-Codes (keep only G0 & G1 moves)
        self.remove_nontravel_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Keep only G0 & G1 moves",
            font=self.normal_font,
            onvalue=True,
            offvalue=False,
        )
        self.remove_nontravel_switch.grid(
            row=3,
            column=1,
            padx=PADDING["medium"],
            pady=PADDING["medium"],
            sticky="W",
        )

        # remove lonely G1s
        self.remove_lone_gs_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Remove lines with lonely G0/G1s",
            font=self.normal_font,
            onvalue=True,
            offvalue=False,
        )
        self.remove_lone_gs_switch.grid(
            row=4,
            column=1,
            padx=PADDING["medium"],
            pady=PADDING["medium"],
            sticky="W",
        )

        # remove lonely G1s
        self.remove_coordname_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Remove coordinate names",
            font=self.normal_font,
            onvalue=True,
            offvalue=False,
        )
        self.remove_coordname_switch.grid(
            row=5,
            column=1,
            padx=PADDING["medium"],
            pady=PADDING["medium"],
            sticky="W",
        )

    def focused_tab(self):
        return self.get()
