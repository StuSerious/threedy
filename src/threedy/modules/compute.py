# ------------------------------------------------------------------------------------------------ #
# *                                         compute module                                       * #
# ------------------------------------------------------------------------------------------------ #
import re  # hate that I have to do this


def process_file_contents(
    file_contents,
    remove_comments=False,
    remove_m_codes=False,
    insert_space=False,
    remove_empty_lines=False,
):
    if remove_comments:
        comment_pattern = r".*;.*$"
        file_contents = re.sub(comment_pattern, "", file_contents, flags=re.MULTILINE)

    if remove_m_codes:
        remove_m_codes_pattern = r"^.*\bM\d+\b.*$\n?"
        file_contents = re.sub(
            remove_m_codes_pattern, "", file_contents, flags=re.MULTILINE
        )

    if insert_space:
        insert_space_pattern = r"([A-Za-z])(\d)"
        file_contents = re.sub(insert_space_pattern, r"\1 \2", file_contents)

    if remove_empty_lines:
        empty_line_pattern = r"^\s*$\n?"
        file_contents = re.sub(
            empty_line_pattern, "", file_contents, flags=re.MULTILINE
        )

    return file_contents
