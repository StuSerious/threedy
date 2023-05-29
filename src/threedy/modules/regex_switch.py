class RegexSwitch:
    def __init__(self, text, attr_name, row, column, pattern, multiline=False):
        self.text = text
        self.attr_name = attr_name
        self.row = row
        self.column = column
        self.pattern = pattern
        self.multiline = multiline


# easy to add configs
switch_configs = [
    RegexSwitch(
        "Remove Comments",
        "remove_comments_switch",
        0,
        1,
        r"\s*;.*$",
        multiline=True
    ),
    RegexSwitch(
        "Remove M-Codes",
        "remove_mcodes_switch",
        1,
        1,
        r"^M.*$"
    ),
    RegexSwitch(
        "Remove F/E-Codes",
        "remove_fecodes_switch",
        2,
        1,
        r"\s*[FE]\d*\.?\d*"
    ),
    RegexSwitch(
        "Keep only G0 & G1 moves",
        "remove_nontravel_switch",
        3,
        1,
        r"^(?!G[10]).*$[\r\n]*",
        multiline=True
    ),
    RegexSwitch(
        "Remove lines with lonely G0/G1s",
        "remove_lone_gs_switch",
        4,
        1,
        r"^[G10]+$[\r\n]*",
        multiline=True
    ),
]

# Create the options dictionary in main.py
self.options = {
    config.attr_name: getattr(self.tabview, config.attr_name)
    for config in switch_configs
}

# Create the multiline_options list in compute.py
multiline_options = [
    config.attr_name
    for config in switch_configs
    if config.multiline
]

# Use the switch_configs in settings.py for regex patterns
RE_PATTERNS = {
    config.attr_name: config.pattern
    for config in switch_configs
}
