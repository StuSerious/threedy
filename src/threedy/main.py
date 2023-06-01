import os
import sys

import customtkinter as ctk
from interface.commandbar import Commandbar
from interface.sidebar import Sidebar
from interface.tabview import Tabview
from interface.terminal import Terminal
from modules.compute import process_file_contents
from modules.dialogs import export_file_dialog, select_file_dialog
from modules.settings import *


# PyInstaller helper
# https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
def resource_path(relative_path):
    try:  # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # setup window
        self.geometry(f"{APP_SIZE['width']}x{APP_SIZE['height']}")
        self.iconbitmap(resource_path("src\\threedy\\resources\\logo.ico"))
        self.title("threedy")

        # setup grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # setup sidebar
        self.sidebar = Sidebar(
            self,
            self.on_file_select,
            self.on_file_export,
        )
        # setup commandbar
        self.commandbar = Commandbar(
            self,
            self.on_compute,
        )
        # setup terminal
        self.terminal = Terminal(
            self,
        )
        # setup tabview
        self.tabview = Tabview(
            self,
        )

        # startup defaults
        self.sidebar.select_theme_optionmenu.set("System")
        self.sidebar.scaling_factor_optionmenu.set("100%")
        self.commandbar.cli_entry.configure(state="disabled")
        self.terminal.newline("Welcome! To begin, please select a file.")

    def on_file_select(self):
        self.file_path, self.file_contents = select_file_dialog()
        self.terminal.newline("File selected: " + self.file_path + "\n\n")

    def on_file_export(self):
        self.selected_tab = self.tabview.selected_tab()
        export_file_dialog(self.selected_tab, self.file_contents)
        self.terminal.newline("File exported successfully!\n\n")

    def on_compute(self):
        print()


if __name__ == "__main__":
    threedy = App()
    threedy.mainloop()
