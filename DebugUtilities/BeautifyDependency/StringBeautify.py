from enum import Enum


class Justify(Enum):
    CENTER = 0
    LEFT = 0
    RIGHT = 0


def pad_str(string_to_pad: str,
            available_length_for_string: int,
            string_justify: Justify = Justify.CENTER,
            pad_char_to_start_and_end_only: bool = False,
            horizontal_padding_char: str = '-',
            vertical_padding_character: str = '+',
            sub_section: int = 0) -> str:
    space_count = 4
    # '({v-pad}{create spaces by space_count times} create by subsection times) append v-pad'
    padding = (f'{vertical_padding_character}{" " * space_count}' * sub_section) + vertical_padding_character
    # remove the padding length from the total available length
    available_length_for_string -= len(padding) * 2
    justified_string = ''
    horizontal_padding_char = " " if pad_char_to_start_and_end_only else horizontal_padding_char
    if string_justify is Justify.CENTER:
        justified_string = f'{string_to_pad.center(available_length_for_string, horizontal_padding_char)}'
    elif string_justify is Justify.LEFT:
        justified_string = f'{string_to_pad.ljust(available_length_for_string, horizontal_padding_char)}'
    elif string_justify is Justify.CENTER:
        justified_string = f'{string_to_pad.rjust(available_length_for_string, horizontal_padding_char)}'
    return f'{padding}{justified_string}{padding}'


def print_by_padding(string: str, length: int, justify: Justify = Justify.CENTER, start_end_only: bool = False,
                     padding_char_hor: str = '-', padding_char_ver: str = '+', sub_part: int = 0):
    print(pad_str(string, length, justify, start_end_only, padding_char_hor, padding_char_ver, sub_part))


def pad_str_list(string_lst: list[str], total_length: int, justify: Justify = Justify.CENTER,
                 padding_char_hor: str = '-',
                 padding_char_ver: str = '+') -> str:
    padded_str = ''
    for string in string_lst:
        padded_str += pad_str(string_to_pad=string, available_length_for_string=int(total_length / len(string_lst)),
                              string_justify=justify,
                              pad_char_to_start_and_end_only=True,
                              horizontal_padding_char=padding_char_hor,
                              vertical_padding_character=padding_char_ver)[:-1]
    return padded_str + padding_char_ver


def bool_to_str(is_true: bool) -> str:
    return 'Yes' if is_true else 'No'
