import re
import time

from interface.tabview import gcode_switch_data
from modules.settings import RE_PATTERNS


def process_file_contents(
    file_contents,
    remove_comments=False,
    remove_mcodes=False,
    remove_fecodes=False,
    remove_nontravel=False,
    remove_lone_gs=False,
    remove_coordname=False,
):
    timer = time.process_time()

    if remove_comments:
        file_contents = re.sub(
            RE_PATTERNS["remove_comments"],
            "",
            file_contents,
            flags=re.MULTILINE,
        )

    if remove_mcodes:
        file_contents = re.sub(
            RE_PATTERNS["remove_mcodes"],
            "",
            file_contents,
            flags=re.MULTILINE,
        )

    if remove_fecodes:
        file_contents = re.sub(
            RE_PATTERNS["remove_fecodes"],
            "",
            file_contents,
        )

    if remove_nontravel:
        file_contents = re.sub(
            RE_PATTERNS["remove_nontravel"],
            "",
            file_contents,
            flags=re.MULTILINE,
        )

    if remove_lone_gs:
        file_contents = re.sub(
            RE_PATTERNS["remove_lone_gs"],
            "",
            file_contents,
            flags=re.MULTILINE,
        )

    if remove_coordname:
        file_contents = re.sub(
            RE_PATTERNS["remove_coordname"],
            r"\2 \3 \4 \1\5",
            file_contents,
        )
        file_contents = re.sub(r"G", "", file_contents)

    elapsed_time = time.process_time() - timer

    return file_contents, elapsed_time
