import customtkinter as ctk
from modules.settings import *


class Tabview(ctk.CTkTabview):
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)

        # defaults
        self.normal_font = ctk.CTkFont(
            family=FONT, size=FONT_SIZE, weight=FONT_WEIGHT[0]
        )
        # setup layout
        self.grid(
            row=0,
            rowspan=1,
            column=1,
            columnspan=3,
            padx=(PADDING_M),
            pady=0,
            sticky="nsew",
        )
        self.grid_rowconfigure(3, weight=1)

        # add tabs
        self.add("G-Code Tools")
        self.add("CSV Tools")

        # setup tabs
        self.tab("G-Code Tools").grid_columnconfigure(0, weight=1)

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
            column=0,
            padx=PADDING_M,
            pady=PADDING_M,
            sticky="W",
        )

        # rm M-Codes
        self.remove_m_codes_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Remove M-Codes",
            font=self.normal_font,
            onvalue=True,
            offvalue=False,
        )
        self.remove_m_codes_switch.grid(
            row=1,
            column=0,
            padx=PADDING_M,
            pady=PADDING_M,
            sticky="W",
        )

        # ins spacing
        self.insert_spacing_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Insert Spacing",
            font=self.normal_font,
            onvalue=True,
            offvalue=False,
        )
        self.insert_spacing_switch.grid(
            row=2,
            column=0,
            padx=PADDING_M,
            pady=PADDING_M,
            sticky="W",
        )

        # rm whitelines
        self.remove_empty_lines_switch = ctk.CTkSwitch(
            self.tab("G-Code Tools"),
            text="Remove Empty Lines",
            font=self.normal_font,
            onvalue=True,
            offvalue=False,
        )
        self.remove_empty_lines_switch.grid(
            row=3,
            column=0,
            padx=PADDING_M,
            pady=PADDING_M,
            sticky="W",
        )

    def focused_tab(self):
        return self.get()
