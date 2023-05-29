# ------------------------------------------------------------------------------------------------ #
# *                                         compute module                                       * #
# ------------------------------------------------------------------------------------------------ #
import re  # hate that I have to do this
import time

from modules.settings import *


def process_file_contents(
    file_contents,
    remove_comments=False,
    remove_mcodes=False,
    remove_fecodes=False,
    remove_nontravel=False,
    remove_lone_gs=False,
    remove_whitelines=False,
):
    timer = time.process_time()

    if remove_comments:
        file_contents = re.sub(
            RE_PATTERNS["rm-comments"], "", file_contents, flags=re.MULTILINE
        )

    if remove_mcodes:
        file_contents = re.sub(
            RE_PATTERNS["rm-mcodes"], "", file_contents, flags=re.MULTILINE
        )

    if remove_fecodes:
        file_contents = re.sub(RE_PATTERNS["rm-fecodes"], "", file_contents)

    if remove_nontravel:
        file_contents = re.sub(
            RE_PATTERNS["rm-nontravel"], "", file_contents, flags=re.MULTILINE
        )

    if remove_lone_gs:
        file_contents = re.sub(
            RE_PATTERNS["rm-lone-gs"], "", file_contents, flags=re.MULTILINE
        )

    if remove_whitelines:
        file_contents = re.sub(
            RE_PATTERNS["rm-whitelines"], "", file_contents, flags=re.MULTILINE
        )

    elapsed_time = time.process_time() - timer

    return file_contents, elapsed_time
