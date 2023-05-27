from tkinter import filedialog


# --------------------------------------- import file logic -------------------------------------- #
def select_file_dialog():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("G-code files", "*.gcode *.txt"),
            ("CSV files", "*.csv"),
            ("All files", "*.*"),
        ]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_contents = file.read()
            return file_contents, file_path
        except FileNotFoundError:
            print("File not found.")
            return None
        except IOError:
            print("Error reading the file.")
            return None


# --------------------------------------- export file logic -------------------------------------- #
def export_file_dialog(current_tab, file_contents):
    if current_tab == "Ansys Prep":
        extension = ".gcode"
    elif current_tab == "CSV Tools":
        extension = ".csv"

    file_path = filedialog.asksaveasfilename(
        defaultextension=f"{extension}",
        filetypes=[
            ("G-code files", "*.gcode *.txt"),
            ("CSV files", "*.csv"),
            ("All files", "*.*"),
        ],
    )

    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(file_contents)
            print("File saved successfully!")
        except IOError as e:
            print("Error saving file:", str(e))
