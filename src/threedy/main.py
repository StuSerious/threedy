import customtkinter as ctk
from modules.compute import process_file_contents
from modules.dialogs import export_file_dialog, select_file_dialog
from modules.settings import *


class ThreedyGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.normal_font = ctk.CTkFont(
            family=FONT, size=FONT_SIZE, weight=FONT_WEIGHT[0]
        )
        # setup - window
        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}")
        self.iconbitmap("src/threedy/resources/logo.ico")
        self.title("threedy")
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_columnconfigure(0, weight=0)
        # setup - Terminal
        self.terminal = ctk.CTkTextbox(self)
        self.terminal.grid(
            row=1,
            rowspan=2,
            column=1,
            columnspan=4,
            padx=PADDING_M,
            pady=(PADDING_M, 0),
            sticky="NSEW",
        )
        self.terminal.insert("0.0", "Welcome! To begin, please select a file.")

        # setup - sidebar
        self.sidebar = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)
        # sidebar - logo
        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text="threedy",
            font=ctk.CTkFont(family=FONT, size=35, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # sidebar - select file
        self.select_file_button = ctk.CTkButton(
            self.sidebar,
            text="1) Select file",
            font=self.normal_font,
            command=self.select_file,
        )
        self.select_file_button.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
        )

        # sidebar - export file
        self.export_file_button = ctk.CTkButton(
            self.sidebar,
            text="3) Export file",
            font=self.normal_font,
            command=self.export_file,
        )
        self.export_file_button.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
        )

        # sidebar - appearence
        self.appearance_mode_label = ctk.CTkLabel(
            self.sidebar, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=0)
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(
            self.sidebar,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(0, 10))

        # sidebar - scaling
        self.scaling_label = ctk.CTkLabel(self.sidebar, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=0)
        self.scaling_optionmenu = ctk.CTkOptionMenu(
            self.sidebar,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionmenu.grid(row=8, column=0, padx=20, pady=(0, 10))

        # setup - tabview
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(
            row=0,
            rowspan=1,
            column=1,
            columnspan=3,
            padx=(PADDING_M),
            pady=0,
            sticky="nsew",
        )
        self.tabview.grid_rowconfigure(3, weight=1)

        # tabview - add tabs
        self.tabview.add("G-Code Tools")
        self.tabview.add("CSV Tools")
        # tabview - setup tabs
        self.tabview.tab("G-Code Tools").grid_columnconfigure(0, weight=1)
        # TODO: create second tab

        # tabview - rm comments
        self.remove_comments_switch = ctk.CTkSwitch(
            self.tabview.tab("G-Code Tools"),
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

        # tabview - rm M-Codes
        self.remove_m_codes_switch = ctk.CTkSwitch(
            self.tabview.tab("G-Code Tools"),
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

        # tabview - ins spacing
        self.insert_spacing_switch = ctk.CTkSwitch(
            self.tabview.tab("G-Code Tools"),
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

        # tabview - rm whitelines
        self.remove_empty_lines_switch = ctk.CTkSwitch(
            self.tabview.tab("G-Code Tools"),
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

        # CLI field
        self.cli_entry = ctk.CTkEntry(
            self,
            placeholder_text="[WIP] - Optional CLI arguments:",
            font=self.normal_font,
        )
        self.cli_entry.grid(
            row=3,
            column=1,
            columnspan=2,
            padx=(PADDING_M, 0),
            pady=PADDING_M,
            sticky="NSEW",
        )

        # compute button
        self.compute_button = ctk.CTkButton(
            master=self,
            text="2) Compute",
            font=self.normal_font,
            command=self.compute_changes,
        )
        self.compute_button.grid(
            row=3, column=3, padx=PADDING_M, pady=PADDING_M, sticky="NSEW"
        )

        # setup - defaults
        self.cli_entry.configure(state="disabled")

        self.appearance_mode_optionmenu.set("System")
        self.scaling_optionmenu.set("100%")

        # self.compute_button.configure(state="disabled")
        # self.export_file_button.configure(state="disabled")

    # select and load file
    def select_file(self):
        self.file_contents, self.file_path = select_file_dialog()
        self.terminal.insert("0.0", "File selected: " + self.file_path + "\n\n")

    # compute changes
    def compute_changes(self):
        self.remove_comments = self.remove_comments_switch.get()
        self.remove_m_codes = self.remove_m_codes_switch.get()
        self.insert_spacing = self.insert_spacing_switch.get()
        self.remove_empty_lines = self.remove_empty_lines_switch.get()
        self.terminal.insert("0.0", "Vars OK. Compute started...\n\n")
        self.file_contents = process_file_contents(
            self.file_contents,
            self.remove_comments,
            self.remove_m_codes,
            self.insert_spacing,
            self.remove_empty_lines,
        )
        self.terminal.insert("0.0", "Compute done!\n\n")

    # export modified file
    def export_file(self):
        self.current_tab = self.tabview.get()
        export_file_dialog(self.current_tab, self.file_contents)
        self.terminal.insert("0.0", "File exported successfully!\n\n")

    # apply appearence
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    # apply scaling
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def testcmd():
        print("ok")


if __name__ == "__main__":
    threedy = ThreedyGUI()
    threedy.mainloop()
