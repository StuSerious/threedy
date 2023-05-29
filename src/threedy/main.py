import customtkinter as ctk
from components.commandbar import Commandbar
from components.sidebar import Sidebar
from components.tabview import Tabview
from components.terminal import Terminal
from modules.compute import process_file_contents
from modules.dialogs import export_file_dialog, select_file_dialog
from modules.settings import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # start in dark mode
        ctk.set_appearance_mode("dark")

        # setup window
        self.geometry(f"{APP_SIZE['width']}x{APP_SIZE['height']}")
        self.iconbitmap("src/threedy/resources/logo.ico")
        self.title("threedy")

        # setup grid
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # setup sidebar
        self.sidebar = Sidebar(
            self, self.on_file_select, self.on_file_export, corner_radius=0
        )

        # setup tabview
        self.tabview = Tabview(self)

        # setup terminal
        self.terminal = Terminal(
            self, fg_color=TERMINAL_BG_COLOR, text_color=TERMINAL_TEXT_COLOR
        )

        # setup commandbar
        self.commandbar = Commandbar(self, self.on_compute, fg_color="#242424")

        # startup defaults
        self.sidebar.select_theme_optionmenu.set("System")
        self.sidebar.scaling_factor_optionmenu.set("100%")
        self.terminal.newline("Welcome! To begin, please select a file.")
        self.commandbar.cli_entry.configure(state="disabled")

    def on_file_select(self):
        self.file_path, self.file_contents = select_file_dialog()
        self.terminal.newline("File selected: " + self.file_path + "\n\n")

    def on_file_export(self):
        self.focused_tab = self.tabview.focused_tab()
        export_file_dialog(self.focused_tab, self.file_contents)
        self.terminal.newline("File exported successfully!\n\n")

    # compute changes
    def on_compute(self):
        self.remove_comments = self.tabview.remove_comments_switch.get()
        self.remove_m_codes = self.tabview.remove_m_codes_switch.get()
        self.insert_spacing = self.tabview.insert_spacing_switch.get()
        self.remove_empty_lines = self.tabview.remove_empty_lines_switch.get()

        self.terminal.newline("Vars OK. Compute started...\n\n")

        self.file_contents, self.compute_time_taken = process_file_contents(
            self.file_contents,
            self.remove_comments,
            self.remove_m_codes,
            self.insert_spacing,
            self.remove_empty_lines,
        )
        self.terminal.newline(
            "Compute done! Took " + f"{self.compute_time_taken}" + " seconds\n\n"
        )


if __name__ == "__main__":
    threedy = App()
    threedy.mainloop()
