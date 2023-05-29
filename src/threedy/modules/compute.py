# ------------------------------------------------------------------------------------------------ #
# *                                         compute module                                       * #
# ------------------------------------------------------------------------------------------------ #
import re  # hate that I have to do this
import time

from modules.settings import *


def process_file_contents(file_contents, **options):
    timer = time.process_time()

    multiline_options = [
        "remove_comments",
        "remove_nontravel",
        "remove_lone_gs",
    ]

    for option, regex_pattern in RE_PATTERNS.items():
        if options.get(option, False):
            flags = re.MULTILINE if option in multiline_options else 0
            file_contents = re.sub(regex_pattern, "", file_contents, flags=flags)

    # Remove empty lines after processing
    file_contents = re.sub(r"^\s*$\n?", "", file_contents, flags=re.MULTILINE)

    elapsed_time = time.process_time() - timer

    return file_contents, elapsed_time
