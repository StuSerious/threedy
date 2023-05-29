import customtkinter as ctk
from modules.settings import *


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, import_event, export_event, **kwargs):
        super().__init__(master=parent, **kwargs)

        # defaults
        self.normal_font = ctk.CTkFont(
            family=FONT, size=FONT_SIZE, weight=FONT_WEIGHT[0]
        )
        self.import_event = import_event
        self.export_event = export_event

        # grid layout
        self.grid(row=0, rowspan=5, column=0, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        # threedy text logo
        self.logo_label = ctk.CTkLabel(
            self,
            text="threedy",
            font=ctk.CTkFont(family=FONT, size=35, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=PADDING["large"], pady=(20, 10))

        # select file button
        self.select_file_button = ctk.CTkButton(
            self,
            text="1) Select file",
            font=self.normal_font,
            command=self.select_file,
        )
        self.select_file_button.grid(
            row=1,
            column=0,
            padx=PADDING["large"],
            pady=10,
        )

        # export file button
        self.export_file_button = ctk.CTkButton(
            self,
            text="3) Export file",
            font=self.normal_font,
            command=self.export_file,
        )
        self.export_file_button.grid(
            row=2,
            column=0,
            padx=PADDING["large"],
            pady=10,
        )

        # theme selector
        self.select_theme_label = ctk.CTkLabel(
            self, text="Appearance Mode:", anchor="w"
        )
        self.select_theme_label.grid(row=5, column=0, padx=PADDING["large"], pady=0)
        self.select_theme_optionmenu = ctk.CTkOptionMenu(
            self,
            values=["Light", "Dark", "System"],
            command=self.change_theme,
        )
        self.select_theme_optionmenu.grid(
            row=6, column=0, padx=PADDING["large"], pady=(0, 10)
        )

        # scaling selector
        self.scaling_factor_label = ctk.CTkLabel(self, text="UI Scaling:", anchor="w")
        self.scaling_factor_label.grid(row=7, column=0, padx=PADDING["large"], pady=0)
        self.scaling_factor_optionmenu = ctk.CTkOptionMenu(
            self,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling,
        )
        self.scaling_factor_optionmenu.grid(
            row=8, column=0, padx=PADDING["large"], pady=(0, 10)
        )

    # select and load file
    def select_file(self):
        self.import_event()

    # export modified file
    def export_file(self):
        self.export_event()

    def change_theme(self, new_theme: str):
        ctk.set_appearance_mode(new_theme)

    def change_scaling(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
