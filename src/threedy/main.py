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


# PyInstaller `--onefile` helper
# https://github.com/TomSchimansky/CustomTkinter/discussions/939
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # setup window
        self.geometry(f"{APP_SIZE['width']}x{APP_SIZE['height']}")
        self.iconbitmap(resource_path("resources\\logo.ico"))
        self.title(f"threedy {VERSION}")

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
        try:
            self.file_path, self.file_contents = select_file_dialog()
            self.terminal.newline("IMPORT: File selected: " + self.file_path)
        except TypeError:  # (if no file is selected in the dialog)
            self.file_path = None
            self.file_contents = None
            self.terminal.newline("IMPORT: ERROR!!! -- No file selected.")

    def on_file_export(self):
        self.selected_tab = self.tabview.selected_tab()
        export_file_dialog(self.selected_tab, self.file_contents)
        self.terminal.newline("EXPORT: File exported successfully!")

    def on_compute(self):
        try:
            remove_comments = self.tabview.remove_comments_switch.get()
            remove_mcodes = self.tabview.remove_mcodes_switch.get()
            remove_fecodes = self.tabview.remove_fecodes_switch.get()
            remove_nontravel = self.tabview.remove_nontravel_switch.get()
            remove_lone_gs = self.tabview.remove_lone_gs_switch.get()
            remove_coordname = self.tabview.remove_coordname_switch.get()

            self.file_contents, self.compute_time_taken = process_file_contents(
                self.file_contents,
                remove_comments,
                remove_mcodes,
                remove_fecodes,
                remove_nontravel,
                remove_lone_gs,
                remove_coordname,
            )
            self.terminal.newline(
                "COMPUTE: Done! -- Took " + f"{self.compute_time_taken}" + " seconds"
            )
        except AttributeError:
            self.terminal.newline(
                "COMPUTE: ERROR!!! -- No file is selected, select a file first."
            )


def main() -> None:
    threedy = App()
    threedy.mainloop()


if __name__ == "__main__":
    main()
