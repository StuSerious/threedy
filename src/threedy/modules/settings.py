# size
APP_SIZE = {"width": 1280, "height": 720}

# text
FONT = "Calibri"
FONT_SIZE = 14

# styling
PADDING = {"none": 0, "medium": 10, "large": 20}

# terminal
TERMINAL_BG_COLOR = "#000000"
TERMINAL_TEXT_COLOR = "#90cf00"

# patterns
RE_PATTERNS = {
    "remove_comments": r"\s*;.*$",
    "remove_mcodes": r"^M.*$",
    "remove_fecodes": r"\s*[FE]-?\d*\.?\d*",
    "remove_nontravel": r"^(?!G[10]).*$[\r\n]*",
    "remove_lone_gs": r"^[G10]+$[\r\n]*",
    "remove_coordname": r"G([01])\s+X(\S+)\s+Y(\S+)(?:\s+Z(\S+))?(\n|$)",
}
