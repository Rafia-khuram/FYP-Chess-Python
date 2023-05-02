from DebugUtilities.BeautifyDependency.StringBeautify import print_by_padding, Justify


class UnitTest:
    def __init__(self, passed: bool, desired_output: str, output: str, case_id: int):
        self.case_id = case_id
        self.passed = passed
        self.required_output = desired_output
        self.output = output

    def print_data(self, sub_part_id: int, padding_length: int, justify: Justify):
        print_by_padding(
            string=f'',
            length=padding_length, start_end_only=False, justify=justify,
            sub_part=sub_part_id)
        print_by_padding(
            string=f' Desired Output :',
            length=padding_length, start_end_only=True, justify=justify,
            sub_part=sub_part_id)
        print_by_padding(
            string=f' {self.required_output}',
            length=padding_length, start_end_only=True, justify=justify,
            sub_part=sub_part_id)
        print_by_padding(
            string=f' Output :',
            length=padding_length, start_end_only=True, justify=justify,
            sub_part=sub_part_id)
        print_by_padding(
            string=f' {self.output}',
            length=padding_length, start_end_only=True, justify=justify,
            sub_part=sub_part_id)
        print_by_padding(
            string=f'',
            length=padding_length, start_end_only=False, justify=justify,
            sub_part=sub_part_id)
